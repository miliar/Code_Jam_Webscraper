#include <fstream>
#include <iostream>
using namespace std;

#define int64 __int64

const int MaxDigits = 300;
const int PLUS  =  1;
const int MINUS = -1;


class Bigint
{
public:
//	static const int SmallBound = 129;	
private:
	char Digits[MaxDigits];
	int  DigitCount;
	int  Signbit;


public:
	//constructors
	Bigint();
	Bigint(const Bigint&);
	Bigint(int);
	Bigint(int64);
	Bigint(const char*);

	//input/output
	friend istream& operator >> (istream&, Bigint&);
	friend ostream& operator << (ostream&, const Bigint&);

	//assignment
	const Bigint& operator=(const Bigint&);
	Bigint  operator=(int);
	Bigint  operator=(int64);
	Bigint  operator=(const char*);
	void StringToBigint(const char*);

	//addition
	Bigint operator+(const Bigint&)   const;
	Bigint operator+(int)       const;
	Bigint operator+(int64) const;
	friend Bigint operator+(int, const Bigint&);
	friend Bigint operator+(int64, const Bigint&);

	//substraction
	Bigint operator-(const Bigint&)   const;
	Bigint operator-(int)       const;
	Bigint operator-(int64) const;
	friend Bigint operator-(int, const Bigint&);
	friend Bigint operator-(int64, const Bigint&);

	//Unary Minus/Plus
	Bigint operator-() const;
	Bigint operator+() const;
	

	//multiplication
	Bigint operator*(const Bigint&)   const;
	Bigint operator*(int)       const;
	Bigint operator*(int64) const;
	friend Bigint operator*(int, const Bigint&);
	friend Bigint operator*(int64, const Bigint&);

	//division(integer)
	Bigint operator/(const Bigint&) const ;
	Bigint operator/(int) const;
	Bigint operator/(int64) const;
	friend Bigint operator/(int, const Bigint&);
	friend Bigint operator/(int64, const Bigint&);

	//rest
	Bigint operator%(const Bigint&) const;
	Bigint operator%(int) const;
	Bigint operator%(int64) const;
	friend Bigint operator%(int, const Bigint&);
	friend Bigint operator%(int64, const Bigint&);
	

	//Comparison
	bool operator==(const Bigint&) const;
	bool operator==(int) const;
	bool operator==(int64) const;
	friend bool operator==(int , const Bigint&);
	friend bool operator==(int64, const Bigint&);
	
	bool operator!=(const Bigint&) const;
	bool operator!=(int) const;
	bool operator!=( int64) const;
	friend bool operator!=(int , const Bigint&);
	friend bool operator!=(int64, const Bigint&);

	bool operator<(const Bigint&) const;
	bool operator<(int) const;
	bool operator<(int64) const;
	friend bool operator<(int , const Bigint&);
	friend bool operator<(int64, const Bigint&);

	bool operator>(const Bigint&) const;
	bool operator>(int) const;
	bool operator>(int64) const;
	friend bool operator>(int , const Bigint&);
	friend bool operator>(int64, const Bigint&);


	bool operator<=(const Bigint&) const;
	bool operator<=(int) const;
	bool operator<=(int64) const;
	friend bool operator<=(int , const Bigint&);
	friend bool operator<=(int64, const Bigint&);

	bool operator>=(const Bigint&) const;
	bool operator>=(int) const;
	bool operator>=(int64) const;
	friend bool operator>=(int , const Bigint&);
	friend bool operator>=(int64, const Bigint&);

	//Operation+Assign
	void operator+=(const Bigint&);	
	void operator+=(int);
	void operator+=(int64);

	void operator-=(const Bigint&);	
	void operator-=(int);
	void operator-=(int64);

	void operator*=(const Bigint&);	
	void operator*=(int);
	void operator*=(int64);


	void operator/=(const Bigint&);	
	void operator/=(int);
	void operator/=(int64);

	void operator%=(const Bigint&);	
	void operator%=(int);
	void operator%=(int64);


	//Convertion
	operator int();
	operator int64();
	operator bool();

	//GetFunctions
	int GetLastDigit()  const; 
	char& Digit(int);
	int GetDigit(int)   const;
	int GetDigitCount() const;
	int GetSign()       const;
	bool isZero()       const;

	//Mul and Div by 10
	void Mulby10 (int = 1);
	void Divby10 (int = 1);

	//FullDivision (integer part and rest)
	void Divide(int,           Bigint*, Bigint*) const;
	void Divide(int64,     Bigint*, Bigint*) const;
	void Divide(const Bigint&, Bigint*, Bigint*) const;

private:
	//Auxiliary Fns
	Bigint MultiplyBySmallNumber(const int) const;
	Bigint AddUnsigned(const Bigint&) const;
	Bigint SubstractUnsigned(const Bigint&) const;
	int CompareUnsigned(const Bigint&) const;
	void MakeZeroPlusSigned();

};


//Bigint.cpp//////////////////////////////////////////

//////////////
//Constructors
Bigint::Bigint()
{
	(*this)=0;
}

Bigint::Bigint(const Bigint& Operand)
{
	(*this) = Operand;
}

Bigint::Bigint(int Operand)
{
	(*this) = Operand;
}

Bigint::Bigint(int64 Operand)
{
	(*this) = Operand;
}

Bigint::Bigint(const char* Str)
{
	StringToBigint(Str);
}
//Constructors
//////////////



//////////////
//Input/Output
istream& operator >> (istream& in, Bigint& Num)
{
	char Str[MaxDigits];
	in>>Str;
	Num.StringToBigint(Str);
	return in;
}
ostream& operator << (ostream& out, const Bigint& Num)
{
//	Num.MakeZeroPlusSigned();
	if(Num.Signbit == MINUS)
	{
		out<<'-';
	}
	if(Num.isZero())
	{
		out<<'0';
		return out;
	}

	int i;
	for(i = Num.DigitCount-1; i>=0; i--)
	{
		out<<char(Num.Digits[i]+'0');
	}
	return out;
}
//Input/Output
//////////////

////////////
//assignment
const Bigint& Bigint::operator=(const Bigint& Operand)
{
	this->DigitCount = Operand.DigitCount;
	this->Signbit    = Operand.Signbit;
	int i;
	for(i = 0; i<this->DigitCount; i++)
		this->Digits[i] = Operand.Digits[i];
	MakeZeroPlusSigned();
	return (*this);
}
Bigint Bigint::operator=(int Operand)
{
	this->DigitCount = 0;
	if(Operand==0)
	{
		MakeZeroPlusSigned();
		return (*this);
	}
	this->Signbit = PLUS;
	if(Operand<0)
	{
		this->Signbit = MINUS;
		Operand*=-1;
	}
	while(Operand>0)
	{
		this->Digits[this->DigitCount++]=Operand%10;
		Operand/=10;
	}
	MakeZeroPlusSigned();
	return (*this);
}
Bigint Bigint::operator=(int64 Operand)
{
	this->DigitCount = 0;
	if(Operand==0)
	{
		MakeZeroPlusSigned();
		return (*this);
	}
	this->Signbit = PLUS;
	if(Operand<0)
	{
		this->Signbit = MINUS;
		Operand*=-1;
	}
	while(Operand>0)
	{
		this->Digits[this->DigitCount++]=(int)(Operand%10);
		Operand/=10;
	}
	MakeZeroPlusSigned();
	return (*this);
}
Bigint  Bigint::operator=(const char* Str)
{
	this->StringToBigint(Str);
	return (*this);
}
void Bigint::StringToBigint(const char* Str)
{
	int pp = 0;
	while(Str[pp]==' ' || Str[pp]=='\t' || Str[pp]=='\n')
		pp++;
	if(!Str[pp])
	{
		(*this) = 0;
		 return;
	}
	if(Str[0]=='+')
	{
		this->Signbit = PLUS;
		pp++;
	}
	else
	{
		if(Str[0]=='-')
		{
			this->Signbit = MINUS;
			pp++;
		}
		else
		{
			this->Signbit = PLUS;
		}
	}
	

	while(Str[pp]=='0')
	{
		pp++;
	}

	this->DigitCount = 0;
	int tt = pp;
	while(Str[tt] && Str[tt]<='9' && Str[tt]>='0')
	{
//	    this->Digits[this->DigitCount++] = Str[pp]-'0';
		tt++;
	}
	int i;
	for(i = tt-1; i>=pp; i--)
		this->Digits[this->DigitCount++] = Str[i]-'0';
	MakeZeroPlusSigned();
}
//assignment
////////////


//////////
//Addition
Bigint Bigint::operator+(const Bigint& Operand2)   const
{
	if(isZero())
		return Operand2;
	if(Operand2.isZero())
		return (*this);
	Bigint Result;
	if(this->Signbit*Operand2.Signbit==PLUS)
	{
		Result = AddUnsigned(Operand2);
		Result.Signbit = this->Signbit;
		Result. MakeZeroPlusSigned();
		return Result;
	}
	else
	{
		if(CompareUnsigned(Operand2)==PLUS)
		{
			Result = SubstractUnsigned(Operand2);
			Result.Signbit = this->Signbit;
			Result. MakeZeroPlusSigned();
			return Result;
		}
		else
		{
			Result = Operand2.SubstractUnsigned((*this));
			Result.Signbit = Operand2.Signbit;
			Result. MakeZeroPlusSigned();
			return Result;
		}
	}
	return 0;
}
Bigint Bigint::operator+(int Operand2) const
{
	Bigint T(Operand2);
	return (*this)+T;
}
Bigint Bigint::operator+(int64 Operand2) const
{
	Bigint T(Operand2);
	return (*this)+T;
}
Bigint operator+(int Operand1, const Bigint& Operand2)
{
	return Operand2+Operand1;
}
Bigint operator+(int64 Operand1, const Bigint& Operand2)
{
	return Operand2+Operand1;
}
//Addition
//////////




//////////////
//substraction
Bigint Bigint::operator-(const Bigint& Operand2) const
{
	return (*this)+(-Operand2);
}
Bigint Bigint::operator-(int Operand2) const
{
	return (*this)+(-Operand2);
}
Bigint Bigint::operator-(int64 Operand2) const
{
	return (*this)+(-Operand2);
}
Bigint operator-(int Operand1, const Bigint& Operand2)
{
	return (Operand1)+(-Operand2);
}
Bigint operator-(int64 Operand1, const Bigint& Operand2)
{
	return (Operand1)+(-Operand2);
}
//substraction
//////////////


//////////////////
//Unary Minus/Plus
Bigint Bigint::operator-() const
{
	Bigint Result = (*this);
	Result.Signbit*=-1;
	Result. MakeZeroPlusSigned();
	return Result;
}
Bigint Bigint::operator+() const
{
	return (*this);
}
//Unary Minus/Plus
//////////////////


////////////////
//Multiplication
Bigint Bigint::operator*(const Bigint& Operand2)   const
{
	Bigint Result = 0;
	Bigint Tmp;
	int i;
	if(this->DigitCount>Operand2.DigitCount)
	{
		return Operand2*(*this);
	}
	for(i = 0; i<DigitCount; i++)
	{
		Tmp = Operand2.MultiplyBySmallNumber(this->Digits[i]);
		Tmp.Mulby10(i);
		Result+=Tmp;
	}
	Result.Signbit = this->Signbit*Operand2.Signbit;
	Result. MakeZeroPlusSigned();
	return Result;

}
Bigint Bigint::operator*(int Operand2) const
{
/*	if(Operand2<SmallBound && Operand2>-SmallBound)
	{
		Bigint Result = MultiplyBySmallNumber(Operand2);
		if(Operand2<0)
		{
			Result.Signbit = MINUS*this->Signbit;
		}
		else
		{
			Result.Signbit = PLUS*this->Signbit;
		}
		Result. MakeZeroPlusSigned();
		return Result;
	}
	*/
	Bigint T(Operand2);
	return (*this)*T;
}
Bigint Bigint::operator*(int64 Operand2) const
{
/*	if(Operand2<SmallBound && Operand2>-SmallBound)
	{
		Bigint Result = MultiplyBySmallNumber((int)Operand2);
		if(Operand2<0)
		{
			Result.Signbit = MINUS;
		}
		else
		{
			Result.Signbit = PLUS;
		}
		Result. MakeZeroPlusSigned();
		return Result;
	}
	*/
	Bigint T(Operand2);
	return (*this)*T;
}
Bigint operator*(int Operand1, const Bigint& Operand2)
{
	return Operand2*Operand1;
}
Bigint operator*(int64 Operand1, const Bigint& Operand2)
{
	return Operand2*Operand1;
}
//Multiplication
////////////////


//////////////////
//division(integer)
Bigint  Bigint::operator/(const Bigint& Operand2) const
{
	Bigint Quotient;
	Bigint Remainder;
	Divide(Operand2, &Quotient, &Remainder);
	Quotient.MakeZeroPlusSigned();
	return Quotient;
}
Bigint  Bigint::operator/(int Operand2) const
{ 
	Bigint Quotient;
	Bigint Remainder;
	Divide(Operand2, &Quotient, &Remainder);
	Quotient.MakeZeroPlusSigned();
	return Quotient;
}
Bigint  Bigint::operator/(int64 Operand2) const
{
	Bigint Quotient;
	Bigint Remainder;
	Divide(Operand2, &Quotient, &Remainder);
	Quotient.MakeZeroPlusSigned();
	return Quotient;
}
Bigint operator/(int Operand1, const Bigint& Operand2)
{
	Bigint T(Operand1);
	return T/Operand2;
}
Bigint operator/(int64 Operand1, const Bigint& Operand2)
{
	Bigint T(Operand1);
	return T/Operand2;
}
//division(integer)
//////////////////


//////
//rest
Bigint  Bigint::operator%(const Bigint& Operand2) const
{
	Bigint Quotient;
	Bigint Remainder;
	Divide(Operand2, &Quotient, &Remainder);
	Remainder. MakeZeroPlusSigned();
	return Remainder;
}
Bigint  Bigint::operator%(int Operand2) const
{ 
	Bigint Quotient;
	Bigint Remainder;
	Divide(Operand2, &Quotient, &Remainder);
	Remainder. MakeZeroPlusSigned();
	return Remainder;
}
Bigint  Bigint::operator%(int64 Operand2) const
{
	Bigint Quotient;
	Bigint Remainder;
	Divide(Operand2, &Quotient, &Remainder);
	Remainder. MakeZeroPlusSigned();
	return Remainder;
}
Bigint operator%(int Operand1, const Bigint& Operand2)
{
	Bigint T(Operand1);
	return T%Operand2;
}
Bigint operator%(int64 Operand1, const Bigint& Operand2)
{
	Bigint T(Operand1);
	return T%Operand2;
}
//rest
//////



////////////
//Comparison
bool Bigint::operator==(const Bigint& Operand2) const
{
//	MakeZeroPlusSigned();
	if(this->Signbit!=Operand2.Signbit)
	{
		return false;
	}
	int t = CompareUnsigned(Operand2);
	if(t==0)
		return true;
	return false;
}
bool Bigint::operator==(int Operand2) const
{
	Bigint T(Operand2);
	return ((*this)==T);
}
bool Bigint::operator==(int64 Operand2) const
{
	Bigint T(Operand2);
	return ((*this)==T);
}
bool operator==(int Operand1, const Bigint& Operand2)
{
	return Operand2==Operand1;
}
bool operator==(int64 Operand1, const Bigint& Operand2)
{
	return Operand2==Operand1;
}
////
////
bool Bigint::operator!=(const Bigint& Operand2) const
{
	return !((*this)==Operand2);
}
bool Bigint::operator!=(int Operand2) const
{
	Bigint T(Operand2);
	return ((*this)!=T);
}
bool Bigint::operator!=( int64 Operand2) const
{
	Bigint T(Operand2);
	return ((*this)!=T);
}
bool operator!=(int Operand1, const Bigint& Operand2)
{
	return Operand2!=Operand1;
}
bool operator!=(int64 Operand1, const Bigint& Operand2)
{
	return Operand2!=Operand1;;
}
////
////
bool Bigint::operator<(const Bigint& Operand2) const
{
//	MakeZeroPlusSigned();
	if(this->Signbit<Operand2.Signbit)
	{
		return true;
	}
	
	if(this->Signbit>Operand2.Signbit)
	{
		return false;
	}

	int t = CompareUnsigned(Operand2);
	if(this->Signbit==MINUS)
	{
		if(t==PLUS)
		{
			return true;
		}
		return false;
	}
	else
	{
		if(t==MINUS)
			return true;
		return false;
	}
}
bool Bigint::operator<(int Operand2) const
{
	Bigint T(Operand2);
	return ((*this)<T);
}
bool Bigint::operator<(int64 Operand2) const
{
	Bigint T(Operand2);
	return ((*this)<T);;
}
bool operator<(int Operand1, const Bigint& Operand2)
{
	return Operand2>Operand1;
}
bool operator<(int64 Operand1, const Bigint& Operand2)
{
	return Operand2>Operand1;
}
////
////
bool Bigint::operator>(const Bigint& Operand2) const
{
//	MakeZeroPlusSigned();
	if(this->Signbit>Operand2.Signbit)
	{
		return true;
	}
	
	if(this->Signbit<Operand2.Signbit)
	{
		return false;
	}

	int t = CompareUnsigned(Operand2);
	if(this->Signbit==MINUS)
	{
		if(t==MINUS)
		{
			return true;
		}
		return false;
	}
	else
	{
		if(t==PLUS)
			return true;
		return false;
	}
}
bool Bigint::operator>(int Operand2) const
{
	Bigint T(Operand2);
	return ((*this)>T);
}
bool Bigint::operator>(int64 Operand2) const
{
	Bigint T(Operand2);
	return ((*this)>T);
}
bool operator>(int Operand1, const Bigint& Operand2)
{
	return Operand2<Operand1;
}
bool operator>(int64 Operand1, const Bigint& Operand2)
{
	return Operand2<Operand1;
}
////
////
bool Bigint::operator<=(const Bigint& Operand2) const
{
	return !((*this)>Operand2);
}
bool Bigint::operator<=(int Operand2) const
{
	Bigint T(Operand2);
	return ((*this)<=T);
}
bool Bigint::operator<=(int64 Operand2) const
{
	Bigint T(Operand2);
	return ((*this)<=T);
}
bool operator<=(int Operand1, const Bigint& Operand2)
{
	return Operand2>=Operand1;
}
bool operator<=(int64 Operand1, const Bigint& Operand2)
{
	return Operand2>=Operand1;
}
////
////
bool Bigint::operator>=(const Bigint& Operand2) const
{
	return !((*this)<Operand2);
}
bool Bigint::operator>=(int Operand2) const
{
	Bigint T(Operand2);
	return ((*this)>=T);
}
bool Bigint::operator>=(int64 Operand2) const
{
	Bigint T(Operand2);
	return ((*this)>=T);
}
bool operator>=(int Operand1, const Bigint& Operand2)
{
	return Operand2<=Operand1;
}
bool operator>=(int64 Operand1, const Bigint& Operand2)
{
	return Operand2<=Operand1;
}
////////////
//Comparison


//////////////////
//Operation+Assign
void Bigint::operator+=(const Bigint& Operand2)
{
	(*this)	= (*this)+Operand2;
}
void Bigint::operator+=(int Operand2)
{
	(*this)	= (*this)+Operand2;
}
void Bigint::operator+=(int64 Operand2)
{
	(*this)	= (*this)+Operand2;
}

void Bigint::operator-=(const Bigint& Operand2)
{
	(*this)	= (*this)-Operand2;
}
void Bigint::operator-=(int Operand2)
{
	(*this)	= (*this)-Operand2;
}
void Bigint::operator-=(int64 Operand2)
{
	(*this)	= (*this)-Operand2;
}

void Bigint::operator*=(const Bigint& Operand2)
{
	(*this)	= (*this)*Operand2;
}
void Bigint::operator*=(int Operand2)
{
	(*this)	= (*this)*Operand2;
}
void Bigint::operator*=(int64 Operand2)
{
	(*this)	= (*this)*Operand2;
}

void Bigint::operator/=(const Bigint& Operand2)
{
	(*this)	= (*this)/Operand2;
}
void Bigint::operator/=(int Operand2)
{
	(*this)	= (*this)/Operand2;
}
void Bigint::operator/=(int64 Operand2)
{
	(*this)	= (*this)/Operand2;
}

void Bigint::operator%=(const Bigint& Operand2)
{
	(*this)	= (*this)%Operand2;
}
void Bigint::operator%=(int Operand2)
{
	(*this)	= (*this)%Operand2;
}
void Bigint::operator%=(int64 Operand2)
{
	(*this)	= (*this)%Operand2;
}
//Operation+Assign
//////////////////


////////////
//Convertion
Bigint::operator int()
{
	int N, i, t;
	N = 0;
	t = 1;
	for(i = 0; i<DigitCount; i++)
	{
		N+=(Digits[i]*t);
		t*=10;
	}
	if(Signbit==MINUS)
		N*=-1;
	return N;
}
Bigint::operator int64()
{
	int N, i, t;
	N = 0;
	t = 1;
	for(i = 0; i<DigitCount; i++)
	{
		N+=(Digits[i]*t);
		t*=10;
	}
	if(Signbit==MINUS)
		N*=-1;
	return N;
}
Bigint::operator bool()
{
	return ((*this)!=0);
}
///////////
//Convertion


//////////////
//GetFunctions
int  Bigint::GetLastDigit()  const
{
	return Digits[0];
}
char& Bigint::Digit(int nIndex)
{
	if(nIndex<0 || nIndex>=MaxDigits)
		return Digits[0];
	return Digits[nIndex];
}
int  Bigint::GetDigit(int nIndex) const
{
	if(nIndex<0 || nIndex>=MaxDigits)
		return -1;
	return Digits[nIndex];
}
int  Bigint::GetDigitCount() const
{
	return DigitCount;
	
}
int  Bigint::GetSign() const
{
	if(isZero())
		return 0;
	return Signbit;
	
}
bool Bigint::isZero()  const
{
	return (DigitCount==0);
}
//////////////
//GetFunctions


///////////////////
//Mul and Div by 10
void Bigint::Mulby10 (int  d)
{
	if(isZero())
		return;
	int i;
	for(i = DigitCount-1; i >=0; i--)
	{
		Digits[i+d] = Digits[i];
	}
	for(i = 0; i<d; i++)
	{
		Digits[i] = 0;
	}
	DigitCount+=d;
	MakeZeroPlusSigned();
}
void Bigint::Divby10 (int d )
{
	if(isZero())
		return;
	int i;
	for(i = 0; i <DigitCount-d; i++)
	{
		Digits[i] = Digits[i+d];
	}
	DigitCount-=d;
	if(DigitCount<0)
		DigitCount = 0;
	MakeZeroPlusSigned();
}
//Mul and Div by 10
///////////////////

//////////////////////////////////////
//FullDivision (integer part and rest)
void Bigint::Divide(int Operand2,   Bigint* Q, Bigint* R) const
{
	Divide(Bigint(Operand2), Q, R);
}
void Bigint::Divide(int64 Operand2,     Bigint* Q, Bigint* R) const
{
	Divide(Bigint(Operand2), Q, R);
}
void Bigint::Divide(const Bigint& Operand2, Bigint* Q, Bigint* R) const
{
	if(isZero() || Operand2.isZero())
	{
		*Q = 0;
		*R = 0;
		Q->MakeZeroPlusSigned();
		R->MakeZeroPlusSigned();
		return;
	}
	int i;
	(*R) = 0;
	
	int k;
	for(i = DigitCount-1; i>=0; i--)
	{
		R->Mulby10();
		R->Digits[0] = Digits[i];
		if(R->DigitCount==0 && R->Digits[0]!=0)
			R->DigitCount++;
		k = 0;
		while(R->CompareUnsigned(Operand2)>=0)
		{
			(*R) = (*R).SubstractUnsigned(Operand2);
			k++;
		}
		Q->Digits[i] = k;
	}
	i = DigitCount;
	while(i>0 && (Q->Digits[i-1]==0))
	{
		i--;
	}
	Q->DigitCount = i;
	R->Signbit = PLUS;
	if(this->Signbit == PLUS && Operand2.Signbit == PLUS)
	{
		Q->Signbit = PLUS;
		Q->MakeZeroPlusSigned();
		R->MakeZeroPlusSigned();
		return;
	}
	if(this->Signbit == PLUS && Operand2.Signbit == MINUS)
	{
		Q->Signbit = MINUS;
		Q->MakeZeroPlusSigned();
		R->MakeZeroPlusSigned();
		return;
	}
	if(this->Signbit == MINUS &&  Operand2.Signbit == PLUS)
	{
		if(R->isZero())
		{
			Q->Signbit = MINUS;
			Q->MakeZeroPlusSigned();
			R->MakeZeroPlusSigned();
			return;
		}
		(*R) = (Operand2 - (*R));
		Q->Signbit = PLUS;
		(*Q)+=1;
		Q->Signbit = MINUS;
		Q->MakeZeroPlusSigned();
		R->MakeZeroPlusSigned();
		return;
	}
	if(this->Signbit == MINUS &&  Operand2.Signbit == MINUS)
	{
		if(R->isZero())
		{
			Q->Signbit = PLUS;
			Q->MakeZeroPlusSigned();
			R->MakeZeroPlusSigned();
			return;
		}
		(*R) = (Operand2 - (*R));
		Q->Signbit = PLUS;
		(*Q)+=1;
		Q->MakeZeroPlusSigned();
		R->MakeZeroPlusSigned();
		return;
	}
	Q->MakeZeroPlusSigned();
	R->MakeZeroPlusSigned();
}
//FullDivision (integer part and rest)
//////////////////////////////////////


///////////////
//Auxiliary Fns
Bigint Bigint::MultiplyBySmallNumber(const int Operand2) const
{
	
	if(isZero() || Operand2 == 0)
		return 0;
	Bigint Result;
	int i, t, c;
	for(i = 0, c = 0; i<DigitCount; i++)
	{
		t = Digits[i]*Operand2 + c;
		c = t/10;
		Result.Digits[i] = t%10;
	}
	Result.DigitCount = this->DigitCount;
	while(c)
	{
		Result.Digits[Result.DigitCount++] = c%10;
		c/=10;
	}
	Result.MakeZeroPlusSigned();
	return Result;
}
Bigint Bigint::AddUnsigned(const Bigint& Operand2) const
{
	Bigint Result;
	int i, c, t, l;
	if(this->DigitCount>Operand2.DigitCount)
	{
		l = this->DigitCount;
	}
	else
	{
		l = Operand2.DigitCount; 
	}

	c = 0;
	for(i = 0; i<l ; i++)
	{
		t = c;
		if(i<this->DigitCount)
		{
			t += this->Digits[i];
		}
		if(i< Operand2.DigitCount)
		{
			 t += Operand2.Digits[i];
		}
		Result.Digits[i] = t%10;
		c = t/10;
	}
	Result.DigitCount = l;
	while(c)
	{
		Result.Digits[Result.DigitCount++] = c%10;
		c/=10;
	}
	Result.MakeZeroPlusSigned();
	return Result;
}

Bigint Bigint::SubstractUnsigned(const Bigint& Operand2) const
{
	Bigint Result;
	Bigint A = (*this);
	Bigint B = Operand2;
	int i;
	for(i = 0; i<this->DigitCount; i++)
	{
		if(i>=Operand2.DigitCount)
			B.Digits[B.DigitCount++] = 0;
	}
	for(i = 0; i<this->DigitCount; i++)
	{
		if(A.Digits[i]<B.Digits[i])
		{
			A.Digits[i+1]-=1;
			A.Digits[i]+=10;
		}
		Result.Digits[i] = A.Digits[i]-B.Digits[i];
	}
	Result.DigitCount = DigitCount;
	while((Result.DigitCount>0) && (Result.Digits[Result.DigitCount-1]==0))
	{
		Result.DigitCount--;	
	}
	Result.MakeZeroPlusSigned();
	return Result;
}

int Bigint::CompareUnsigned(const Bigint& Operand2) const
{
	if(DigitCount>Operand2.DigitCount)
	{
		return PLUS;
	}
	if(DigitCount<Operand2.DigitCount)
	{
		return MINUS;
	}
	int i;
	for(i = DigitCount-1; i>=0; i--)
	{
		if(Digits[i]>Operand2.Digits[i])
			return PLUS;
		if(Digits[i]<Operand2.Digits[i])
			return MINUS;
	}
	return 0;
}

void Bigint::MakeZeroPlusSigned() 
{
	if(isZero())
		Signbit = PLUS;
}
//Auxiliary Fns
///////////////


Bigint a[1010];

Bigint GCD(Bigint a,Bigint b)
{	
	Bigint zero(0);
	while (a!=zero && b!=zero)	
		if (a<b) b%=a; else		
			a%=b;				
	if (a==zero) return b;
	return a;
}

ifstream in("large.in");
ofstream out("large.out");

int gcd(int a,int b)
{	
	int zero = 0;
	while (a!=zero && b!=zero)	
		if (a<b) b%=a; else		
			a%=b;				
	if (a==zero) return b;
	return a;
}

/*
int main()
{
	int a[1100];
	int test,i,j,n;
	in >> test;
	for (int t = 1; t <= test; t++)
	{
		in >> n;
		for (i = 0 ; i < n; i++)
			in >> a[i];
		int ans = 0,ans1;
		for (i = 0 ; i < n ; i++)
			for (j = 0 ; j < n; j++)
				if (a[i] < a[j])
					ans = gcd(ans,(a[j] - a[i]));
		ans1 = a[0] % ans;
		ans = ans - ans1;
		out << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}*/

int main()
{
	int test,i,j,n;
	in >> test;
	for (int t = 1; t <= test; t++)
	{
		in >> n;
		for (i = 0 ; i < n; i++)
			in >> a[i];
		Bigint ans(0),ans1;
		for (i = 0 ; i < n ; i++)
			for (j = 0 ; j < n; j++)
				if (a[i] < a[j])
					ans = GCD(ans,(a[j] - a[i]));
		ans1 = a[0] % ans;
		if (ans1 == 0)
			ans = 0;
		else
			ans = ans - ans1;
		out << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
