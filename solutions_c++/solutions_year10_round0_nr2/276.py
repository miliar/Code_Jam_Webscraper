//The implementation of class BigInt
//Author: Nianchen Deng (5080379114)

#include "BigInt.h"

typedef unsigned int uint;
typedef long long unsigned int lluint;
const uint MAX = 1000000000;                                                //The maximum of number stored in each element (not include)


//Default constructor
//Create a BigInt with value of zero
BigInt::BigInt(void)
{
	_Data = new uint[1];
	_Start = _Data;
	_Data[0] = 0;
	_Size = 1;
	_Length = 0;
	_Negative = false;
}

//Create from ordinary int
//the max number of an int is about 2 * 10 ^ 10
//So it will need one or two elements
BigInt::BigInt (int source)
{
	_Negative = source >> 31;                                               //Decide the sign of source.
	_Size = 2;                                                              //Assign an array of _Size 2.
	_Data = new uint[_Size];
	_Start = _Data;

	if (source == 0)                                                        //source = 0: set the BigInt with value of 0.
	{
		_Length = 0;
	}
	else if (abs (source) < MAX)                                            //source only needs _Length 1.
	{
		_Data[0] = abs (source);
		_Length = 1;
	}
	else                                                                    //source needs _Length 2.
	{
		_Data[0] = abs (source) % MAX;
		_Data[1] = abs (source) / MAX;
		_Length = 2;
	}
}

//Create from a C-style string
BigInt::BigInt (const char *source)
{
	_Start = new uint[0];
	create_from_string (source);                                            //Convert string to BigInt.
}

//Copy constructor
BigInt::BigInt (const BigInt &source)
{
	_Size = _Length = source._Length;                                       //Copy _Length, _Negative.
	_Negative = source._Negative;
	_Data = new uint[_Size];                                                //Assigned proper size of space.
	_Start = _Data;
	for (uint i = 0; i < _Length; ++i)                                      //Copy elements one by one.
		_Data[i] = source._Data[i];
}

//Default destructor
BigInt::~BigInt(void)
{
	delete []_Start;
}

//Assignment operator over-loading
BigInt & BigInt::operator =(const BigInt &right)
{
	if (_Size < right._Length)                                              //If the space is not enough,
		resize_without_old_data (right._Length);                            //reassign an enough space.
	else
		_Data = _Start;                                                     //Reset the position of _Data. (Why the _Data doesn't equal to _Start? See divide operator)

	_Negative = right._Negative;                                            //Copy _Length and _Negative.
	_Length = right._Length;
	for (uint i = 0; i < _Length; ++i)                                      //Copy elements one by one.
		_Data[i] = right._Data[i];

	return (*this);
}


//Negative operator over-loading
BigInt BigInt::operator -() const
{
	BigInt result (*this);                                                  //Copy a new BigInt.
	result._Negative = !result._Negative;                                   //Change the sign.
	return result;
}

//Add-to-itself operator over-loading
BigInt & BigInt::operator+= (const BigInt &right)
{
	if (_Negative ^ right._Negative)                                        //If their sign are different,
		return (*this) -= (-right);                                         //call minus-to-itself operator. (a + b = a - (-b))

	if (_Length < right._Length)                                            //If the space is apparently not enough,
		resize_with_old_data (right._Length + 1);                           //assign a enough space and transfer data.

	return unsigned_add (*this, right);                                     //Add (Ignoring the sign) right operand to left and return left.
}

//Minus-to-itself operator over-loading
BigInt & BigInt::operator-= (const BigInt &right)
{
	if (_Negative ^ right._Negative)                                        //If their sign are different,
		return (*this) += (-right);                                         //call add-to-itself operator. (a - b = a + (-b))

	if ((*this) == right)                                                   //If left operand equals to right, result is zero.
	{
		_Length = 0;
		return *this;
	}

	if (unsigned_less_than (right, *this))                                  //If left operand is larger than right,
		return unsigned_minus (*this, right);                               //do minus (Ignoring the sign) directly and return.

	BigInt temp(*this);                                                     //Exchange left and right operand when left is less than right,
	*this = right;
	_Negative = !_Negative;
	return unsigned_minus (*this, temp);                                    //then do minus (Ignoring the sign) and return.
}

//Add operator over-loading
BigInt operator +(const BigInt &left, const BigInt &right)
{
	if (left._Negative ^ right._Negative)                                   //If their sign are different,
		return left - (-right);                                             //call minus operator. (a + b = a - (-b))
	BigInt result;
	result.resize_without_old_data (max (left._Length, right._Length) + 1); //The max length of result is the max length of left and right plus one.
	result._Negative = left._Negative;                                      //Copy data from left to result.
	result._Length = left._Length;
	for (unsigned int i = 0; i < left._Length; ++i)
		result._Data[i] = left._Data[i];

	return unsigned_add (result, right);                                    //Do add (Ignoring the sign) and return the result.
}

//Minus operator over-loading
BigInt operator -(const BigInt &left, const BigInt &right)
{
	if (left._Negative ^ right._Negative)                                   //If their sign are different,
		return left + (-right);                                             //call minus operator. (a - b = a + (-b))

	BigInt result;
	if (unsigned_less_than (left, right))                                   //If left < right, |result| = |right| - |left|
	{
		result = right;
		unsigned_minus (result, left);
		result._Negative = !left._Negative;                                 //--The sign of result is opposite to left
	}
	else                                                                    //If left > right, |result| = |left| - |right|
	{
		result = left;
		unsigned_minus (result, right);
		result._Negative = left._Negative;                                  //--The sign of result is same as left
	}

	return result;
}

//Multiply operator over-loading
//The way to implement this operator
//is just like the way we do it by our hand
BigInt operator *(const BigInt &left, const BigInt &right)
{
	if (left == 0 || right == 0)                                            //A number multiply zero is zero
		return 0;
	BigInt result;
	result.resize_without_old_data (left._Length + right._Length);          //The max length of result is the sum of the length of left and right
	if (left._Negative ^ right._Negative)                                   //Decide the sign of result
		result._Negative = true;
	else
		result._Negative = false;
	for (uint i = 0; i < result._Size; ++i)                                 //Initialize every element of result
		result._Data[i] = 0;
	uint carry = 0;
	for (uint pos1 = 0; pos1 < left._Length; ++pos1)                        //Iterate the digits of left
	{
		uint pos2;
		for (pos2 = 0; pos2 < right._Length; ++pos2)                        //--Iterate the digits of right
		{
			lluint current =                                                //----Use a temp variable (9 digits * 9 digits < the length of long long unsigned int)
				(lluint)left._Data[pos1] * (lluint)right._Data[pos2];       //----to store the value of current digit in left multiplying current digit in right 
			current += result._Data[pos1 + pos2] + carry;                   //----and plus the carry passed from the lower digits
			carry = current / MAX;                                          //----Get the carry of current 9 digits
			result._Data[pos1 + pos2] = current % MAX;                      //----Store the number of current 9 digits
		}
		if (carry != 0)                                                     //--Store carry passed from the highest 9 digits if exists
		{
			result._Data[pos1 + pos2] = carry;
			carry = 0;
		}
	}
	if (result._Data[result._Size - 1] == 0)                                //Decide the actual length of result
		result._Length = result._Size - 1;
	else
		result._Length = result._Size;
	return result;
}

//Divide operator over-loading
//First calculate the value of result ignoring its sign
//And then decide the sign of result
BigInt operator /(const BigInt &left, const BigInt &right)
{
	if (right == 0)                                                         //If divided by zero, it's an error
		throw ("Divide zero.");
	BigInt result;
	if (unsigned_less_than (right, left))                                   //If right > left, calculate right / left and get result
	{
		pair <BigInt *, BigInt *> result_and_remainder
		                = unsigned_divide (left, right);
		BigInt *temp = result_and_remainder.first;
		BigInt *remainder = result_and_remainder.second;
		result = *temp;
		delete temp;
		delete remainder;
	}
	else if (!unsigned_less_than (left, right))                             //If right < left, value of result is 1
		result = 1;
	if (left._Negative ^ right._Negative)                                   //If the sign of right is the same as left,
		result._Negative = true;                                            //sign of result is negative. Or it's positive
	else
		result._Negative = false;
	return result;
}

//Mod operator over-loading
//First calculate the value of result ignoring its sign
//And then decide the sign of result
BigInt operator %(const BigInt &left, const BigInt &right)
{
	if (right == 0)                                                         //If mod zero, it's an error
		throw ("Divide zero.");
	BigInt remainder;
	if (unsigned_less_than (right, left))                                   //If right > left, calculate right / left and get remainder
	{
		pair <BigInt *, BigInt *> result_and_remainder
			= unsigned_divide (left, right);
		BigInt *temp = result_and_remainder.second;
		BigInt *result = result_and_remainder.first;
		remainder = *temp;
		delete temp;
		delete result;
	}
	else if (unsigned_less_than (left, right))                              //If right < left, remainder = left
		remainder = left;
	remainder._Negative = left._Negative;                                      //The sign of remainder is the same as left
	return remainder;
}

//Equal operator over-loading
bool operator ==(const BigInt &left, const BigInt &right)
{
	if (left._Negative != right._Negative)
		return false;
	if (left._Length != right._Length)
		return false;
	for (uint i = 0; i < right._Length; ++i)                                //When the sign and length of left and right are equal
		if (left._Data[i] != right._Data[i])                                //compare every 9 digits to find whether there is a difference
			return false;
	return true;
}

//Less operator over-loading
bool operator <(const BigInt &left, const BigInt &right)
{
	if (left._Negative ^ right._Negative)                                   //If left is negative and right is positive, return true
		return left._Negative;                                              //Or if left is positive and right is negative, return false
	if (left._Negative)                                                     //If both are negative, find whether |right| < |left|
	{
		return unsigned_less_than (right, left);
	}
	return unsigned_less_than (left, right);                                //If both are positive, find whether |left| < |right|
}

//Less-or-equal operator over-loading
bool operator <=(const BigInt &left, const BigInt &right)
{
	if (left._Negative ^ right._Negative)                                   //If left is negative and right is positive, return true
		return left._Negative;                                              //Or if left is positive and right is negative, return false
	if (left._Negative)                                                     //If both are negative, find whether |right| <= |left|
		return !unsigned_less_than (left, right);                           //(Opposite to |left| < |right|)
	return !unsigned_less_than (right, left);                               //If both are positive, find whether |left| <= |right|
}                                                                           //(Opposite to |right| < |left|)

//Larger operator over-loading
//Opposite to less-or-equal operator
bool operator >(const BigInt &left, const BigInt &right)
{
	return !(left <= right);
}

//Larger-or-equal operator over-loading
//Opposite to less operator
bool operator >=(const BigInt &left, const BigInt &right)
{
	return !(left < right);
}




//Move-left operator over-loading
//In charge of writing data to ostream
ostream & operator <<(ostream &left, const BigInt &right)
{
	if (right._Length == 0)                                                 //Handle the zero condition
	{
		left << '0';
		return left;
	}
	if (right._Negative)                                                    //Output the sign
		left << '-';
	left << right._Data[right._Length - 1];                                 //Output the highest several digits in the last element
	for (int i = right._Length - 2; i >= 0; --i)                            //Output the digits left from high to low
	{
		for (uint j = MAX / 10; j >= 10; j /= 10)                           //--Output zeros in front of the number to make sure it will output nine digits
		{                                                                   //--like this: 12345 to 000012345
			left.width ();
			if (right._Data[i] >= j)
				break;
			left << '0';
		}
		left << right._Data[i];
	}
	return left;
}

//Move-right operator over-loading
//In charge of reading data from istream
istream & operator >>(istream &left, BigInt &right)
{
	string temp;                                                            //Use string to get data
	left >> temp;
	right.create_from_string (temp.c_str ());                               //Convert string to BigInt
	return left;
}




//Resize the array _Data
//that is, deleting the old space
//and reassigning a new space of specified size
//This operator will throw all the old data
void BigInt::resize_without_old_data (unsigned int size)
{
	delete []_Start;
	_Size = size;
	_Length = 0;
	_Data = new uint[_Size];
	_Start = _Data;
}

//Resize the array _Data
//that is, deleting the old space
//and reassigning a new space of specified size
//This operator will transfer the data,
//so be sure that the new size is larger than the length of number
void BigInt::resize_with_old_data (unsigned int size)
{
	if (_Length > size)
		throw ("Resize with old data error: size is not enough");
	uint *old = _Data;
	_Size = size;
	_Data = new uint[_Size];
	for (uint i = 0; i < _Length; ++i)
		_Data[i] = old[i];
	delete []_Start;
	_Start = _Data;

}

//Convert a C-style string to a BigInt
//by reading character one by one and converting it into its digit
bool BigInt::create_from_string (const char *source)
{
	if (source[0] == '\0')                                                  //If is a null string, regard as a string of value zero
		source = "0";

	int start = 0;

	_Negative = false;
	if (source[0] == '-')                                                   //Extract sign if exists
	{
		_Negative = true;
		++start;
	}

	uint pos = start;
	uint num = 0;

	bool zero = true;
	while (source[pos] != '\0')                                             //Read through the string to count the digits (without the meaningless zeros)
	{
		if (!isalnum (source[pos]))                                         //--If the string contains other characters, it's an error
			return false;
		if (source[pos] != '0' && zero == true)                             //--The first number that is not zero is the end of meaningless zeros
			zero = false;                                                   //----For example: 0000123, number "1" is the end of meaningless zeros
		if (zero == false)                                                  //--If it's not a meaningless zero
			++num;                                                          //--the number of digits increase
		++pos;
	}
	if (zero)                                                               //If all the number in the string are zeros, the value is zero
	{
		resize_without_old_data (1);
		return true;
	}
	if (num % 9 == 0)                                                       //Decide the amount of elements that is needed to store the value
		_Size = num / 9;
	else
		_Size = num / 9 + 1;
	resize_without_old_data (_Size);
	_Length = _Size;

	uint digit = 1, i = 0;
	_Data[0] = 0;
	for (pos = pos - 1; num > 0; --pos, --num, digit *= 10)                   //Read data via iteration
	{
		if (digit >= MAX)                                                     //--Decide the current digit in one element
		{                                                                   //--For example: 12345, the digit of number 3 is 100
			digit /= MAX;
			++i;
			_Data[i] = 0;
		}
		_Data[i] += (source[pos] - '0') * digit;                              //--Store current digit
	}

	return true;
}

//Compare two BigInts ignoring the sign
//If |left| < |right| return true
//First compare the length,
//then compare the number in every element from high to low
bool unsigned_less_than (const BigInt &left, const BigInt &right)
{
	if (left._Length > right._Length)
		return false;
	else if (left._Length < right._Length)
		return true;

	for (int i = right._Length - 1; i >= 0; --i)
	{
		if (left._Data[i] > right._Data[i])
			return false;
		else if (left._Data[i] < right._Data[i])
			return true;
	}

	return false;                                                           //They are equal
}

//Add ignoring sign and store back into the first parameter
//The way to implement this operator
//is just like the way we do it by our hand
BigInt & unsigned_add (BigInt &result, const BigInt &right)
{
	uint min_length = min (result._Length, right._Length);

	uint carry = 0;
	for (uint i = 0; i < min_length; ++i)                                   //Add common digits of two number, one by one, from low to high
	{
		result._Data[i] += right._Data[i] + carry;
		carry = 0;
		if (result._Data[i] >= MAX)                                         //--If larger than MAX, carry exists
		{
			carry = 1;
			result._Data[i] -= MAX;
		}
	}

	if (min_length == right._Length)                                        //If the length of left operand is longer than the right,
		for (uint i = min_length; i <result._Length; ++i)                   //go on iterate left digits of the left operand
		{
			result._Data[i] += carry;
			carry = 0;
			if (result._Data[i] == MAX)                                     //--If there is still a carry cause another carry
			{                                                               //--pass the carry to next digit
				carry = 1;
				result._Data[i] = 0;
			}
		}
	else                                                                    //If the length of left operand is shorter than the right,
		for (uint i = min_length; i < right._Length; ++i)                   //go one iterate left digits of the right operand
		{
			result._Data[i] = right._Data[i] + carry;                       //--Add with carry and store into result
			carry = 0;
			if (result._Data[i] == MAX)                                     //--If there is still a carry cause another carry
			{                                                               //--pass the carry to next digit
				carry = 1;
				result._Data[i] = 0;
			}
		}

	result._Length = max (result._Length, right._Length);                   //The min length of result is the max length of two operands.

	if (carry != 0)                                                         //If there is still a carry exist,
	{                                                                       //the carry needs another element to store
		if (result._Length == result._Size)                                 //--If there are no enough space
			result.resize_with_old_data (result._Size + 1);                 //--assign an enough space and transfer data

		else if (result._Data != result._Start)                             //--If there are some space before _Data
		{                                                                   //--move all the elements backward to spare the space
			for (uint i = 0; i < result._Length; ++i)
				result._Data[i - 1] = result._Data[i];
			--result._Data;
		}

		result._Data[result._Length] = 1;                                   //--Store the carry at the highest digit
		++result._Length;                                                   //--and the length of result should increase by one
	}

	return result;
}

//Minus ignoring sign and store back into the first parameter.
//The way to implement this operator
//is just like the way we do it by our hand.
//Note that the first parameter should
//be larger than the second ignoring the sign.
BigInt & unsigned_minus (BigInt &larger, const BigInt &smaller)
{
	uint min_length = smaller._Length;
	uint carry = 0;
	for (uint i = 0; i < min_length; ++i)                                   //Minus the common digits
	{                                                                       //For example: abcde - fgh, here handles cde - fgh
		if (larger._Data[i] < smaller._Data[i] + carry)                     //If a - b - carry < 0 (a is the current 9 digits of the larger
		{                                                                   //and b is the one of the smaller)
			larger._Data[i] += MAX - smaller._Data[i] - carry;              //current number = 1a - b - carry
			carry = 1;                                                      //and there is a carry to the higher digits
		}
		else
		{
			larger._Data[i] -= smaller._Data[i] + carry;
			carry = 0;
		}
	}

	for (uint i = min_length; i < larger._Length; ++i)                      //Handle the left digits of larger
	{                                                                       //For example: abcde - fgh, here handles ab - carry
		if (larger._Data[i] == 0 && carry != 0)
		{
			larger._Data[i] = MAX - 1;
			carry = 1;
		}
		else
		{
			larger._Data[i] -= carry;
			carry = 0;
			break;
		}
	}

	for (;larger._Length > 0; --larger._Length)                             //Remove meaningless zeros
	{                                                                       //For example: 0000abced to abcde
		if (larger._Data[larger._Length - 1] != 0)
			break;
	}
	return larger;
}

//Divide ignoring sign and store back into the first parameter.
//The way to implement this operator
//is just like the way we do it by our hand.
//Note that the first parameter should
//be larger than the second ignoring the sign.
//The algorithm is like follow:
//            p00q0
//        __________
// abcde )fghijklmn
//        fghi         <--after step 0
//        fghij        <--after step 1 (iteration 1)
//           rs        <--after step 2, p is the result of fghij / abcde and ij is the remainer
//           rsk       <--after step 1 (iteration 2)
//           rsk       <--after step 2, ijk < abcde so do nothing, current 9 digits of result is zero
//         ......      <--......
//           rsklm     <--after step 1 (iteration 4)
//               m     <--after step 2
//               mn    <--after step 1 (iteration 5)
//               mn    <--after step 2
//               mn    <--iteration finish, the result is p00q0 and remainder is mn
//The data stored in memery will be like follow: (Example, remainder of the example above)
// Start                               Data
//|     |     |     |     |     |     |......     <-- initial state
// Start       Data
//|     |     |  i  |  h  |  g  |  f  |......     <-- after step 0
// Start Data
//|     |  j  |  i  |  h  |  g  |  f  |......     <-- after step 1 (iteration 1)
// Start Data
//|     |  s  |  r  |     |     |     |......     <-- after calculate out the result in step 2
// Start                   Data
//|     |     |     |     |  s  |  r  |......     <-- after step 2
//  ......                                        <-- ......
pair <BigInt*, BigInt*> unsigned_divide (const BigInt &larger,
										 const BigInt &smaller)
{
	BigInt *result = new BigInt ();                                         //Assign enough space for result and remainder
	result->resize_without_old_data (larger._Length - smaller._Length + 1);
	result->_Data = result->_Start + result->_Size;
	BigInt *remainder = new BigInt();
	remainder->resize_without_old_data (smaller._Length + 1);
	remainder->_Data = remainder->_Start + remainder->_Size;

	for (uint pos = larger._Length - 1;                                     //Step 0: Pull some digits into remainder
		pos > larger._Length - smaller._Length; --pos)
	{
		--remainder->_Data;
		++remainder->_Length;
		remainder->_Data[0] = larger._Data[pos];
	}

	for (int pos = larger._Length - smaller._Length; pos >= 0; --pos)
	{
		if (remainder->_Data == remainder->_Start)                          //Actually this exception will not happened if my idea is right
			throw ("Error");
		if (result->_Data == result->_Start)
			throw ("Error");

		--remainder->_Data;                                                 //Step 1: Get new lower 9 digits from larger to remainder
		remainder->_Data[0] = larger._Data[pos];
		++remainder->_Length;
		if (remainder->_Length == 1 && remainder->_Data[0] == 0)
		{
			++remainder->_Data;
			--remainder->_Length;
		}
		--result->_Data;                                                    //Move to lower 9 digits in result and initialize
		result->_Data[0] = 0;
		++result->_Length;
		if (unsigned_less_than(smaller, (*remainder)))                      //Step 2: If |smaller| < |remainder|, calculate the result and remainder of remainder / smaller
		{
			for (uint i = MAX / 10; i > 0; i /= 10)                         //--Operation can be shown as follow:
			{                                                               //--Example: left / right = abcdefg + remainder
				BigInt temp = smaller * i;                                  //--So left = a * right * 1000000 + b * right * 100000 + ... + g * right + remainder
				temp._Negative = false;
				while (temp <= (*remainder))
				{
					result->_Data[0] += i;
					unsigned_minus (*remainder, temp);
				}
			}
			for (uint i = remainder->_Length; i > 0; --i)                   //--Pull data to last several elements.
			{
				remainder->_Start[remainder->_Size - remainder->_Length + i - 1] =
					remainder->_Data[i - 1];
			}
			remainder->_Data = remainder->_Start +
				remainder->_Size - remainder->_Length;
		}
	}

	for (;result->_Length > 0; --result->_Length)                           //Remove the meaningless zero
	{
		if (result->_Data[result->_Length - 1] != 0)
			break;
	}
	return make_pair (result, remainder);                                  //Return the result and remainder
}