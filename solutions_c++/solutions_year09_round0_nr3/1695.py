#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
using namespace std;

ifstream fin("C-small-attempt1.in");
//ofstream cout("out.txt");
FILE* fp;


#include <iostream>
#include <cstdio>	// for abs(a) function
#include <algorithm>	// for max(a,b) function

using namespace std;



const int MAX_DIGITS = 50;	// The maximum digits that can be stored in BigInt
const int PLUS = 1;		// Positive sign bit
const int MINUS = -1;	// Negative sign bit

class BigInt
{
	// BigInt Input
	friend istream& operator >>(istream &, BigInt &);
	// BigInt Output
	friend ostream& operator <<(ostream &, const BigInt &);
	// Adds Two BigInts
	friend BigInt operator +(const BigInt &, const BigInt &);
	// Subtracts Two BigInts
	friend BigInt operator -(const BigInt &, const BigInt &);
	// Multiply Two BigInts
	friend BigInt operator *(const BigInt &, const BigInt &);
	// Returns the absolute value of a BigInt
	friend BigInt abs(BigInt);

public:
	// Default Constructor
	BigInt();
	// Long integer Constructor
	BigInt(long);
	// Character array Constructor
	BigInt(const char *);

	// Compares Two BigInt values
	int compareTo(const BigInt &) const;
	// Negation
	BigInt operator -() const;

	// += operator
	const BigInt& operator +=(const BigInt &);
	// -= operator
	const BigInt& operator -=(const BigInt &);
	// *= operator
	const BigInt& operator *=(const BigInt &);
	// ++ pre-increment operator
	BigInt& operator ++();
	// ++ post-increment operator
	BigInt operator ++(int);
	// -- pre-decrement operator
	BigInt& operator --();
	// -- post-decrement operator
	BigInt operator --(int);
	// Various comparisons operator
	bool operator >(const BigInt &) const;
	bool operator >=(const BigInt &) const;
	bool operator <(const BigInt &) const;
	bool operator <=(const BigInt &) const;
	bool operator ==(const BigInt &) const;
	bool operator !=(const BigInt &) const;

public:
	short digits[MAX_DIGITS];	// the array to store each individual digit of the BigInt
	size_t numDigits;	// the total number of digits
	int signBit;	// PLUS for +, or MINUS for -

	// Initialize to zero
	void initToZero();
	// Trim leading zeros
	void zeroJustify();
	// True if it's zero
	bool isZero() const;
	// Compares two BigInt values irrespective of sign
	int unsignedCompareTo(const BigInt &) const;
	// Add two BigInt values irrespective of sign (gives |A| + |B|)
	BigInt add(const BigInt &) const;
	// Subtract two BigInt values irrespective of sign (condition |A| > |B|)
	BigInt subtract(const BigInt &) const;
	// Multiply two BigInt values irrespective of sign (condition |A| >= |B|)
	BigInt multiply(const BigInt &) const;
	// Shift all digits n place to the left
	void shiftDigits(int);
};


BigInt::BigInt()	// default is 0
{
	initToZero();
}

BigInt::BigInt(long val)
{
	if (val == 0)	// special case for 0
	{
		initToZero();
	}
	else	// not zero
	{
		signBit = (val < 0) ? MINUS : PLUS;

		val = ::abs(val);

		int i = 0;	// counter
		while (val > 0)
		{
			digits[i] = val % 10;
			val /= 10;
			i++;
		}
		numDigits = i;
	}
}

BigInt::BigInt(const char* val)
{
	size_t length = strlen(val);
	numDigits = length;

	if (val[0] == '-')	// starts with '-' sign
	{
		signBit = MINUS;
		numDigits--;
	}
	else if (val[0] == '+')	// starts with '+' sign
	{
		signBit = PLUS;
		numDigits--;
	}
	else	// no sign (default: +)
	{
		signBit = PLUS;
	}

	for (int i = 0; i < numDigits; i++)
	{
		digits[i] = val[length - i - 1] - '0';
	}

	zeroJustify();	// trims all leading zeros
}

/* 
   Compares Two BigInts

   Returns:
     1 if (a > b)
     0 if (a == b)
    -1 if (a < b)
*/
int BigInt::compareTo(const BigInt &b) const
{
	if (signBit == PLUS && b.signBit == MINUS)	// + -
	{
		return PLUS;
	}
	if (signBit == MINUS && b.signBit == PLUS)	// - +
	{
		return MINUS;
	}

	// Now, both are the same sign
	int cmp = unsignedCompareTo(b);

	return (cmp * signBit);
}

istream& operator >>(istream& input, BigInt& a)
{
	char temp[MAX_DIGITS + 2];
	input >> temp;

	a = BigInt(temp);

	return input;
}

ostream& operator <<(ostream& output, const BigInt& a)
{
	if (a.signBit == MINUS)
	{
		output << '-';
	}
	for (int i = a.numDigits - 1; i >= 0; i--)
	{
		output << a.digits[i];
	}

	return output;
}

BigInt operator +(const BigInt &a, const BigInt &b)
{
	if (a.signBit == PLUS && b.signBit == PLUS)	// + +	ie: 3 + 4
	{
		return a.add(b);
	}
	else if (a.signBit == MINUS && b.signBit == MINUS)	// - -	ie: -3 + (-4)
	{
		return -(a.add(b));
	}
	else if (a.signBit == PLUS && b.signBit == MINUS)	// + -	ie: 3 + (-4)
	{
		return a - abs(b);
	}
	else 	// - +	ie: -3 + 4
	{
		return b - abs(a);
	}
}

BigInt operator -(const BigInt &a, const BigInt &b)
{
	// both BigInts have the same signs (+ +  OR  - -)
	if ((a.signBit * b.signBit) == PLUS)
	{
		int cmp = a.unsignedCompareTo(b);
		if (cmp > 0)
		{
			if (a.signBit == PLUS)	// a > b, ie: 4 - 3
				return a.subtract(b);
			else	// |A| > |B|, ie: -4 - (-3)
				return -(a.subtract(b));
		}
		else if (cmp < 0)
		{
			if (a.signBit == PLUS)	// a < b, ie: 3 - 4
				return -(b.subtract(a));
			else	// |A| < |B|, ie: -3 - (-4)
				return b.subtract(a);
		}
		else	// a == b, ie: 3 - 3
		{
			return BigInt(0L);
		}
	}
	else if (a.signBit == PLUS && b.signBit == MINUS)	// + -
	{
		return a.add(abs(b));
	}
	else	// - +
	{
		return -((abs(a)).add(b));
	}
}

BigInt operator *(const BigInt &a, const BigInt &b)
{
	BigInt answer;

	answer = (a.unsignedCompareTo(b) > 0) ? a.multiply(b) : b.multiply(a);
	answer.signBit = a.signBit * b.signBit;

	return answer;
}

BigInt abs(BigInt a)
{
	a.signBit = PLUS;
	return a;
}

BigInt BigInt::operator -() const
{
	BigInt a = *this;

	if (!a.isZero()) 
	{
		a.signBit = (this->signBit == PLUS) ? MINUS : PLUS;
	}

	return a;
}

const BigInt& BigInt::operator +=(const BigInt &b)
{
	*this = *this + b;
	return *this;
}

const BigInt& BigInt::operator -=(const BigInt &b)
{
	*this = *this - b;
	return *this;
}

const BigInt& BigInt::operator *=(const BigInt &b)
{
	*this = *this * b;
	return *this;
}

BigInt& BigInt::operator ++()
{
	*this = *this + 1;
	return *this;
}

BigInt BigInt::operator ++(int)
{
	BigInt temp = *this;
	*this = *this + 1;
	return temp;
}

BigInt& BigInt::operator --()
{
	*this = *this - 1;
	return *this;
}

BigInt BigInt::operator --(int)
{
	BigInt temp = *this;
	*this = *this - 1;
	return temp;
}

bool BigInt::operator >(const BigInt &b) const
{
	return (compareTo(b) == PLUS);
}

bool BigInt::operator >=(const BigInt &b) const
{
	return (compareTo(b) >= 0);
}

bool BigInt::operator <(const BigInt &b) const
{
	return (compareTo(b) == MINUS);
}

bool BigInt::operator <=(const BigInt &b) const
{
	return (compareTo(b) <= 0);
}

bool BigInt::operator ==(const BigInt &b) const
{
	return (compareTo(b) == 0);
}

bool BigInt::operator !=(const BigInt &b) const
{
	return (compareTo(b) != 0);
}

// PRIVATE FUNCTIONS FOR INTERNAL USE
void BigInt::initToZero()
{
	this->signBit = PLUS;
	this->numDigits = 1;
	this->digits[0] = 0;
}

bool BigInt::isZero() const
{
	if (this->digits[numDigits - 1] == 0)
		return true;
	else
		return false;
}

void BigInt::zeroJustify()
{
	// Trim all zeros one by one starting from the left most digit
	while (numDigits > 0 && digits[numDigits - 1] == 0)
	{
		numDigits--;
	}

	if (numDigits == 0)	// means all digits are zeroes
	{
		initToZero();
	}
}

int BigInt::unsignedCompareTo(const BigInt &b) const
{
	if (numDigits > b.numDigits)	// a has more digits than b
	{
		return PLUS;
	}
	else if (numDigits < b.numDigits)	// b has more digits than a
	{
		return MINUS;
	}
	else	// a and b have the same number of digits
	{
		for (int i = numDigits - 1; i >= 0; i--)
		{
			if (digits[i] > b.digits[i])
			{
				return PLUS;
			}
			else if (digits[i] < b.digits[i])
			{
				return MINUS;
			}
		}
	}
	return 0;	// a == b
}

// Example of adding
//      a = 09245
//      b = 00823
// answer = 10068
BigInt BigInt::add(const BigInt& b) const
{
	BigInt answer;
	answer.numDigits = max(this->numDigits, b.numDigits) + 1;

	int carry = 0;
	for (int i = 0; i < answer.numDigits; i++)
	{
		int up = (i < this->numDigits) ? this->digits[i] : 0;
		int down = (i < b.numDigits) ? b.digits[i] : 0;
		
		int tempDigit = up + down + carry;
		if (tempDigit >= 10)
		{
			answer.digits[i] = tempDigit - 10;
			carry = 1;
		}
		else
		{
			answer.digits[i] = tempDigit;
			carry = 0;
		}
	}

	answer.zeroJustify();	// Trims leading zero (if it exist)

	return answer;
}

BigInt BigInt::subtract(const BigInt& b) const
{
	BigInt answer;
	answer.numDigits = this->numDigits;

	int borrow = 0;
	for (int i = 0; i < answer.numDigits; i++)
	{
		int up = this->digits[i];
		int down = (i < b.numDigits) ? b.digits[i] : 0;
		
		int tempDigit = up - down - borrow;

		if (tempDigit < 0)
		{
			answer.digits[i] = tempDigit + 10;
			borrow = 1;
		}
		else
		{
			answer.digits[i] = tempDigit;
			borrow = 0;
		}
	}

	answer.zeroJustify();	// trims all leading zeros in the answer

	return answer;
}

BigInt BigInt::multiply(const BigInt &b) const
{
	BigInt answer;
	BigInt temp;
	
	int carry = 0;
	for (int i = 0; i < b.numDigits; i++)
	{
		temp.numDigits = this->numDigits + 1;
		int down = b.digits[i];

		for (int j = 0; j <= this->numDigits; j++)
		{
			int up = (j < this->numDigits) ? this->digits[j] : 0;
			int tempDigit = up * down + carry;

			temp.digits[j] = tempDigit % 10;
			carry = tempDigit / 10;
		}

		temp.shiftDigits(i);
		temp.zeroJustify();
		answer = answer.add(temp);
	}

	return answer;
}

void BigInt::shiftDigits(int n)
{
	int i;
	for (i = numDigits - 1; i >= 0; i--)
	{
		digits[i + n] = digits[i];
	}
	for (i = n - 1; i >= 0; i--)
	{
		digits[i] = 0;
	}
	
	numDigits += n;
}



unsigned int str_count(const string &text ,const string &str)
{
        unsigned int count=0;
        string::size_type pos=text.find(str);
		int idx;
        while(pos!=string::npos)
        {
                count++;
                idx=text.find(str,pos+1);
        }
        return count;
}


int main()
{
	fp = fopen("out.txt", "w");
	int N;
	
	fin >> N;
	fin.get();
	string str;
	const int tokenLen = 19;
	char* token = "welcome to code jam";
	for (int i = 0; i < N; i++)
	{
		getline(fin, str);
		//cout << str << endl;
		int len = str.length();

		unsigned long long table[500][20] = {0};

		bool happen[256] = {false};
		for (int j = 1; j <= len; j++)
		{
			for (int k = 1; k <= 19; k++)
			{
				if (str[j-1] == token[k-1])
				{
					//cout << "j: " << j << "   k: " << k << "   token: " << token[k-1] << "   str: " << str[j-1] << endl;
					happen[token[k-1]] = true;
					if (k == 1)
					{
						table[j][k] = table[j-1][k] + 1;
					}
					else
					{
						table[j][k] = table[j-1][k-1] + table[j-1][k];
					}
				}
				else
				{
					//cout << "j: " << j << "   k: " << k << "   token: " << token[k-1] << "   str: " << str[j-1] << endl;
					if (happen[token[k-1]])
					{
						table[j][k] = table[j-1][k];
					}
				}
			}
		}

		/*for (int j = 1; j <= len; j++)
		{
			for (int k = 1; k <= 19; k++)
			{
				cout << table[j][k] << " ";
			}
			cout << endl;
		}*/
		//cout << endl;
		//cout << ans.numDigits << endl;

		if (table[len][19] > 2147483647)
		{
			cout << "Warning: " << table[len][19] << " might overflow\n";
		}
		//fout << "Case #" << i+1 << ": ";
		fprintf(fp, "Case #%d: ", i+1);
		//cout << table[len][19] << endl;
		fprintf(fp, "%.4d\n", table[len][19]);
		
	}
}