//BigInt.h
//Copyright by (wei dong dong) && (dong cheng cheng)
//All right not reserved!!
#ifndef BIG_INT
#define BIG_INT
#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include <strstream>
using namespace std; 

const int SEG_RESERVE=20;
const int BITS_PER_SEG=4;
const int SEG_UPPER=int(1e4);
const int SEG_DOWN=int(-1e4);
typedef int innertype;

class BigInt
{
public:
	BigInt();
	BigInt(const int& number);
	BigInt(const string& str);
	BigInt(const BigInt& other);

	void AbsMinus(const BigInt& other);
	void AbsPlus(const BigInt& other);
	bool AbsSmall(const BigInt& other) const;
	void Clear();
	void Copy(const BigInt& other);
	void Parse(const string& str);
	void Parse(const int& number);
	string ToString();
	int TotalBits();

	const BigInt& BigInt::operator- ();
	const BigInt &operator= (const int& number);
	const BigInt &operator= (const BigInt &other);
	BigInt& operator+= (const BigInt& other);
	BigInt& operator-= (const BigInt& other);
	const BigInt& operator*= (const int& multiple);
	BigInt& operator*= (const BigInt& multiple);
	const BigInt& operator/= (const int& divisor);
	BigInt& operator/= (const BigInt& divisor);
	BigInt& operator%= (const BigInt& divisor);

public:
	innertype segments[SEG_RESERVE];
	int nSegment;
	int sign;

};

ostream &operator << (ostream& os, const BigInt& out);
istream &operator >> (istream& is, BigInt& hfOprt);

bool operator> (const BigInt& lhs, const BigInt& rhs);
bool operator< (const BigInt& lhs, const BigInt& rhs);
bool operator== (const BigInt& lhs, const BigInt& rhs);
bool operator!= (const BigInt& lhs, const BigInt& rhs); 

BigInt operator+ (const BigInt& lhs, const BigInt& rhs);
BigInt operator- (const BigInt& lhs, const BigInt& rhs);
BigInt operator* (const BigInt& lhs, const int& rhs);
BigInt operator* (const BigInt& lhs, const BigInt& rhs);
BigInt operator/ (const BigInt& lhs, const int& rhs);
BigInt operator/ (const BigInt& lhs, const BigInt& rhs);
BigInt operator% (const BigInt& lhs, const BigInt& rhs);

#endif

//BigInt.cpp
//#include "BigInt.h"
//========================constructors======================
inline BigInt::BigInt()						{	Clear();		}
inline BigInt::BigInt(const int& number)	{	Parse(number);	}
inline BigInt::BigInt(const string& str)	{	Parse(str);		}
inline BigInt::BigInt(const BigInt& other)	{	Copy(other);	}

//========================member functions======================

void BigInt::AbsMinus(const BigInt& other){
	innertype carry = 0;
	for (int i=0; i<nSegment; i++){
		segments[i]-=other.segments[i]+carry;
		if (segments[i]<0){	segments[i]+=SEG_UPPER;	carry=1;}
		else	carry=0;
	}
	while (nSegment>1 && segments[nSegment-1] == 0)	nSegment--;
}

void BigInt::AbsPlus(const BigInt& other)
{
	innertype carry = 0;  
	if (nSegment<other.nSegment)	nSegment=other.nSegment;
	for (int i=0; i<nSegment; i++){
		segments[i] += other.segments[i]+carry;
		if ( segments[i] >= SEG_UPPER ){segments[i]-=SEG_UPPER;	carry=1;}
		else	carry = 0;
	}
	if (carry != 0) { segments[nSegment] += carry;	nSegment++;	}    
}

bool BigInt::AbsSmall(const BigInt& other) const{
	if (nSegment!=other.nSegment) return (nSegment<other.nSegment);
	for (int i=nSegment-1; i>=0; i--)
		if (segments[i]!=other.segments[i]) return segments[i]<other.segments[i];
	return false;
}

inline void BigInt::Clear()			{nSegment = sign = 1; memset(segments, 0, sizeof(segments));}

inline void  BigInt::Copy(const BigInt& other){
	Clear();
	sign=other.sign;	nSegment=other.nSegment;
	memcpy(segments, other.segments, sizeof(innertype)*other.nSegment);
}

void BigInt::Parse(const int& number){
	int temp=number;
	Clear();	nSegment=0;
	if(number<0)	{	sign=-1;		temp=-temp;	}
	while(temp!=0)	{	segments[nSegment]=temp%SEG_UPPER; temp/=SEG_UPPER; nSegment++;}
	if (nSegment==0) nSegment=1;
}

void BigInt::Parse(const string& str){
	Clear();
	int i=int(str.length()-1), j, start=0;
	if (str[0]=='-') sign=-1;
	if (str[0]<'0' || str[0]>'9') start=1;
	nSegment=0;

	while (str[start]=='0' && start<i) start++;

	while (i>=start){
		innertype carry=1;
		j=0;
		while (j<BITS_PER_SEG && i>=start){
			segments[nSegment]+=(str[i]-'0')* carry;
			carry*=10;
			j++, i--;
		}
		nSegment++;
	}
}

string BigInt::ToString(){	strstream strIn; string temp; strIn<<*this; strIn>>temp;	return temp; }

int BigInt::TotalBits(){
	int total=BITS_PER_SEG*(nSegment-1);
	if (segments[nSegment-1]>999)		total+=4;
	else if (segments[nSegment-1]>99)	total+=3;
	else if (segments[nSegment-1]>9)		total+=2;
	else	total+=1;
	return	total;
}

inline const BigInt& BigInt::operator= (const int& number)		{Parse(number);	return *this;	}
inline const BigInt& BigInt::operator= (const BigInt& other)	{Copy(other);	return *this;	}
inline const BigInt& BigInt::operator- ()						{sign*=-1;		return *this;	}

BigInt& BigInt::operator+= (const BigInt& other){
	if( sign==1 && other.sign==-1 )		{	BigInt temp(other);	temp.sign =1;	operator-=(temp); }
	else if(sign==-1 && other.sign==1)	{	sign=1;		operator-=(other); 		sign*=-1;	}
	else	AbsPlus(other);
	return  *this;
}

BigInt& BigInt::operator-= (const BigInt& other){
	if( other.sign * sign == -1 )	AbsPlus(other);
	else if (AbsSmall(other)) {	BigInt temp(*this);	Copy(other); AbsMinus(temp); sign*=-1;}
	else	AbsMinus(other);
	return  *this; 
}

const BigInt& BigInt::operator*= (const int& multiple){
	innertype carry = 0;
	for (int i=0; i <nSegment; i++)
	{
		segments[i]=segments[i]*multiple+carry;
		if (segments[i]>=SEG_UPPER) { carry=segments[i]/SEG_UPPER; segments[i]%=SEG_UPPER;}
		else	carry=0;
	}
	while(carry>0) {segments[nSegment]+=carry%SEG_UPPER; carry/=SEG_UPPER; nSegment++;}
	return  *this;
}

BigInt& BigInt::operator*= (const BigInt& other){
	BigInt temp(*this);
	Clear();
	for (int i=0; i<temp.nSegment; i++){
		for (int j=0; j<other.nSegment; j++) {
			segments[i+j]+=temp.segments[i]*other.segments[j];
			segments[i+j+1]+=segments[i+j]/SEG_UPPER;
			segments[i+j]=segments[i+j]%SEG_UPPER;
		}
	}
	nSegment = temp.nSegment+other.nSegment + 1;
	while (nSegment>1 && segments[nSegment-1] == 0) nSegment--;
	sign=temp.sign*other.sign;
	return *this;    
}

const BigInt& BigInt::operator /= (const int& divisor){
	int _divisor =abs(divisor);	
	innertype carry=0;
	if(divisor<0) sign *= -1;
	for (int i=nSegment-1; i>=0; i--) {	segments[i] += carry*SEG_UPPER;	carry = segments[i]%_divisor; segments[i]=segments[i]/_divisor; }
	while (nSegment>1 && segments[nSegment-1]==0) nSegment--;
	return  *this;
}

BigInt& BigInt::operator/= (const BigInt& divisor){
	BigInt dividend(*this), remainder;
	Clear();
	for (int i=dividend.nSegment-1; i>=0; i--){
		remainder *= SEG_UPPER;
		remainder.segments[0]=dividend.segments[i];
		while ( !remainder.AbsSmall(divisor) ) { remainder.AbsMinus(divisor); segments[i]++;}
	}
	while (nSegment>1 && segments[nSegment-1]==0) nSegment--;
	sign=dividend.sign*divisor.sign;
	return *this;
}

BigInt& BigInt::operator%= (const BigInt& divisor)
{
	BigInt dividend(*this);
	Clear();
	for (int i=dividend.nSegment-1; i>=0; i--) {
		operator*=(SEG_UPPER);
		segments[0] = dividend.segments[i];
		while ( !(AbsSmall(divisor)) )	AbsMinus(divisor);
	}
	if (dividend.sign==-1||divisor.sign==-1) 	sign=-1;
	while (nSegment>1 && segments[nSegment-1]==0) nSegment--;
	return *this;
}

//========================global functions======================
ostream& operator<< (ostream &os, const BigInt &out){
	os << out.segments[out.nSegment-1]*out.sign;
	for (int i=out.nSegment-2; i>=0; i--)
		os<<setw(BITS_PER_SEG)<<setfill('0')<<out.segments[i];
	return os;
} 

istream& operator>> (istream &is, BigInt &rhs){
	string str;	is>>str;	rhs.Parse(str);    
	return is;
}

bool operator< (const BigInt& lhs, const BigInt& rhs){
	if (lhs.sign*rhs.sign==-1)	return (lhs.sign==-1);
	bool absSmall=lhs.AbsSmall(rhs);
	return (lhs.sign==1) ? absSmall: !absSmall ;
}

bool operator== (const BigInt &lhs, const BigInt &rhs)
{
	if (lhs.nSegment!=rhs.nSegment)	return false;
	for (int i=0; i<lhs.nSegment; i++)
		if (lhs.segments[i]!=rhs.segments[i])
			return false;
	return true;
}

inline bool operator!= (const BigInt& lhs, const BigInt& rhs)	{	return !(lhs==rhs);	}
inline bool operator> (const BigInt &lhs, const BigInt &rhs)	{	return (rhs<lhs);	}
BigInt operator+ (const BigInt &lhs, const BigInt &rhs)			{	BigInt temp(lhs);	temp+=rhs;	return temp;}
BigInt operator- (const BigInt &lhs, const BigInt &rhs)			{	BigInt temp(lhs);	temp-=rhs;	return temp;}
BigInt operator* (const BigInt& lhs, const BigInt& rhs)			{	BigInt temp(lhs);	temp*=rhs;	return temp;}
BigInt operator* (const BigInt& lhs, const int& rhs)			{	BigInt temp(lhs);	temp*=rhs;	return temp;}
BigInt operator/ (const BigInt &lhs, const BigInt& rhs)			{	BigInt temp(lhs);	temp/=rhs;	return temp;}
BigInt operator/ (const BigInt &lhs, const int& rhs)			{	BigInt temp(lhs);	temp/=rhs;	return temp;}
BigInt operator% (const BigInt &lhs, const BigInt& rhs)			{	BigInt temp(lhs);	temp%=rhs;	return temp;}

template<class T> inline T gcd(T a,T b)//NOTES:gcd(
{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}

BigInt s[1005];
int n;

int main()
{

	freopen("B-large.in", "r",stdin);
	freopen("B-large.out", "w",stdout);

	int i, nCase;
	BigInt minb, res;
	scanf("%d", &nCase);
	for(int cc=1; cc<=nCase; cc++)
	{
		cin>>n;
		minb = 1;
		for(i=0; i<55; i++) minb *= 10;

		for(i=0; i<n; i++){
			cin>>s[i];
			if(s[i]<minb) minb=s[i];
		}
		
		res = 0;
		for(i=0; i<n; i++){
			if(s[i]>minb){
				res = s[i]-minb;
				break;
			}
		}

		for(; i<n; i++)
		{
			if(s[i]>minb)
			{
				res = gcd(res, s[i]-minb);
			}
		}
		printf("Case #%d: ", cc);
		cout<< (res-s[0]%res)%res << endl;

	}
	return 0;
}