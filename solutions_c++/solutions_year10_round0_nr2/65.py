#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;

typedef vector<bool> VB;

string extract0sstring(const string & s){
	int i=0;
	for(;i<s.sz && s[i]=='0';i++);
	if(i!=s.sz)	return s.substr(i);
	return "0";
}

void addstring1(string & s){
	for(int i=int(s.sz)-1;i>=0;i--){
		if(s[i]!='9')	{s[i]++;return ;}
		s[i]='0';
	}
	s=(char)('1')+s;
}

string subtractstrings(const char *s1, const char *s2) {
	string res = "";
	int i = strlen(s1) - 1, j  = strlen(s2) - 1, borrow = 0;
	while (i >= 0 && j >= 0) {
		int t = s1[i] - s2[j] - borrow;
		if (t < 0) {
			borrow = 1;
			t += 10;
		}
		else borrow = 0;
		res = (char)(t + '0') + res;
		i--; j--;
	}
	while (i >= 0) {
		int t = s1[i] - borrow;
		if(t < 0) {
			borrow = 1;
			t += 10;
		}
		else borrow = 0;
		res = (char)t + res;
		i--;
	}
	return extract0sstring(res);
}

string intmultiplystring(const char *s, int n) {
	int i = strlen(s) - 1, carry = 0;
	string res = "";
	if(n == 0) return "0";
	while(i >= 0) {
		int t = (s[i] - '0') * n + carry;
		carry = t / 10;
		t %= 10;
		res = (char)(t + '0') + res;
		i--;
	}
	while(carry) {
		res = (char)(carry % 10 + '0') + res;
		carry /= 10;
	}
	return res;
}

inline bool gestrings(const string &s1, const string &s2) {
	if (s1.sz != s2.sz) return s1.sz > s2.sz;
	REP (i, s1.sz)
		if (s1[i] != s2[i])
			return s1[i] > s2[i];
	return true;
}

pair<string, string> dividestrings(const string &str1, const string &s2) {
	string temp, s1 = str1;
	REP (i, s1.sz) {
		temp += s1[i];
		temp=extract0sstring(temp);
		s1[i] = '0';
		while (gestrings(temp, s2)) {
			temp = subtractstrings(temp.c_str(), s2.c_str());
			++s1[i];
		}
	}
	return make_pair(extract0sstring(s1), temp);
}

struct bigint{
	vector<bool> Num;
	bool negative;
	
	bigint( string s ) {
		if(s.sz>0 && s[0]=='-'){
			negative=true;
			s=s.substr(1);
			s=extract0sstring(s);
			while(s[0]!='0'){
				Num.pb(s[int(s.sz)-1]&1);
				s=dividestrings(s,"2").first;
			}
			reverse(Num.begin(),Num.end());
			if(Num.sz==0){	Num.pb(0);negative=false;}
		}
		else{
			negative = false; 
			s=extract0sstring(s);
			while(s[0]!='0'){
				Num.pb(s[int(s.sz)-1]&1);
				s=dividestrings(s,"2").first;
			}
			reverse(Num.begin(),Num.end());
			if(Num.sz==0){	Num.pb(0);negative=false;}
		}
	}
	
	bigint() {Num.pb(0);negative = false;}
	
	bigint(const char * t){
		string s=t;
		if(s.sz>0 && s[0]=='-'){
			negative=true;
			s=s.substr(1);
			s=extract0sstring(s);
			while(s[0]!='0'){
				Num.pb(s[int(s.sz)-1]&1);
				s=dividestrings(s,"2").first;
			}
			reverse(Num.begin(),Num.end());
			if(Num.sz==0){	Num.pb(0);negative=false;}
		}
		else{
			negative = false;
			s=extract0sstring(s); 
			while(s[0]!='0'){
				Num.pb(s[int(s.sz)-1]&1);
				s=dividestrings(s,"2").first;
			}
			reverse(Num.begin(),Num.end());
			if(Num.sz==0){	Num.pb(0);negative=false;}
		}
	}
	
	bigint ( int n ) {
		if ( n < 0 )
			negative = true , n = -n;
		else
			negative = false;
		while(n>0){
			Num.pb(n&1);
			n>>=1;
		}
		reverse(Num.begin(),Num.end());
		if(Num.sz==0)	Num.pb(0);
	}
	
	bigint ( LL n ){
		if ( n < 0 )
			negative = true , n = -n;
		else
			negative = false;
		while(n>0){
			Num.pb(n&1);
			n>>=1;
		}
		reverse(Num.begin(),Num.end());
		if(Num.sz==0)	Num.pb(0);
	}
};

VB substr(const VB & s,int i){
	VB ret;
	for(int j=i;j<s.sz;j++)	ret.pb(s[j]);
	if(ret.sz==0)	ret.pb(0);
	return ret;
}

VB substr(const VB & s,int i,int len){
	VB ret;
	int till=min(i+len-1,int(s.sz)-1);
	for(int j=i;j<=till;j++)	ret.pb(s[j]);
	if(ret.sz==0)	ret.pb(0);
	return ret;
}

VB extract0s(const VB & s){
	int i=0;
	for(;i<s.sz && s[i]==0;i++);
	return substr(s,i);
}

VB add(const VB & s1, const VB & s2) {
	int i = int(s1.sz) - 1, j = int(s2.sz) - 1, carry = 0;
	VB res;
	while(i >= 0 && j >= 0) {
		int t = int(s1[i]) + int(s2[j]) + carry;
		carry = t >> 1;
		res.pb(t&1);
		i--; j--;
	}
	while(i >= 0) {
		int t = int(s1[i]) + carry;
		carry = t >> 1;
		res.pb(t&1);
		i--;
	}
	while(j >= 0) {
		int t = int(s2[j]) + carry;
		carry = t >> 1;
		res.pb(t&1);
		j--;
	}
	if(carry)
		res.pb(carry);
	reverse(res.begin(),res.end());
	return res;
}


// Assumes s1-s2>=0 
VB subtract(const VB & s1, const VB & s2) {
	VB res;
	int i = int(s1.sz) - 1, j  = int(s2.sz) - 1, borrow = 0;
	while (i >= 0 && j >= 0) {
		int t = int(s1[i]) - int(s2[j]) - borrow;
		if (t < 0) {
			borrow = 1;
			t += 2;
		}
		else borrow = 0;
		res.pb(t&1);
		i--; j--;
	}
	while (i >= 0) {
		int t = s1[i] - borrow;
		if(t < 0) {
			borrow = 1;
			t += 2;
		}
		else borrow = 0;
		res.pb(t&1);
		i--;
	}
	reverse(res.begin(),res.end());
	return extract0s(res);
}


VB multiply(VB s1, const VB & s2) {
	int j = int(s2.sz) - 1;
	VB res(1,0);
	while(j >= 0) {
		if(s2[j] != 0)
			res = add(res,s1);
		s1.pb(0);
		j--;
	}
	return extract0s(res);
}

inline bool ge(const VB &s1, const VB &s2) {
	if (s1.sz != s2.sz) return s1.sz > s2.sz;
	REP (i, s1.sz)
		if (s1[i] != s2[i])
			return s1[i] > s2[i];
	return true;
}

pair<VB, VB> divide(const VB & str1, const VB & s2) {
	if(s2[0]==0)	{cerr<<"Floating point Exception!"<<endl;return pair<VB,VB>(VB(1,0),VB(1,0));}
	VB temp, s1 = str1;
	REP (i, s1.sz) {
		temp.pb(s1[i]);
		s1[i] = 0;
		temp=extract0s(temp);
		if(ge(temp, s2)) {
			temp = subtract(temp, s2);
			s1[i]=1;
		}
	}
	return make_pair(extract0s(s1), extract0s(temp));
}

/////////////////////////////////////////// Arithmetic operators begins here /////////////////////////////////////////////

bigint operator + ( const bigint& A , const bigint& B ){
	bigint result;
	if ( A.negative != B.negative ){
		if ( ge(A.Num,B.Num) ){
			result.Num = subtract ( A.Num , B.Num );
			result.negative=A.negative;
		}
		else{
			result.Num = subtract ( B.Num , A.Num );
			result.negative=B.negative;
		}
	}
	else{
		result.negative = A.negative;
		result.Num = add ( A.Num , B.Num );
	}
	return result;
}


bigint operator - ( const bigint& A , const bigint& B ){
	bigint result;
	if ( B.negative )	{
		bigint tmp = B;
		tmp.negative = false;
		return tmp + A;
	}
// B is positive	
	if ( A.negative ){
		bigint tmp = A;
		tmp.negative = false;
		result = B + tmp;
		result.negative = true;
		return result;
	}
// Both positive
	if ( ge(A.Num,B.Num) ){
		result.Num = subtract ( A.Num , B.Num );
		result.negative=false;
	}
	else {
		result.Num = subtract ( B.Num , A.Num );
		result.negative = true;
	}
	return result;
}

bigint operator * ( const bigint & A , const bigint & B ){
	bigint result;
	result.Num = multiply ( A.Num , B.Num );
	result.negative = A.negative ^ B.negative;
	if(result.Num[0]==0)	result.negative=false;
	return result;
}


bigint operator / ( const bigint & A , const bigint & B ) {
	bigint result;
	result.Num = divide ( A.Num , B.Num ).first;
	result.negative = A.negative ^ B.negative;
	if(result.Num[0]==0)	result.negative=false;
	return result;
}

// Implemented in the same way as C++
bigint operator % ( const bigint &A , const bigint &B ) {
	bigint result;
	result.Num = divide ( A.Num , B.Num ).second;
	result.negative = A.negative;
	if(result.Num[0]==0)	result.negative=false;
	return result;	
}

/////////////////////////////////////////// Relational operators begins here /////////////////////////////////////////////

bool operator < (const bigint & A, const bigint & B){
	if(A.negative && !B.negative)	return true;
	if(!A.negative && B.negative)	return false;
	if(!A.negative && !B.negative){
		if (A.Num.sz != B.Num.sz) return A.Num.sz < B.Num.sz;
		REP (i, A.Num.sz)
			if (A.Num[i] != B.Num[i])
				return A.Num[i] < B.Num[i];
		return false;
	}
	if(A.negative && B.negative){
		if (A.Num.sz != B.Num.sz) return A.Num.sz > B.Num.sz;
		REP (i, A.Num.sz)
			if (A.Num[i] != B.Num[i])
				return A.Num[i] > B.Num[i];
		return false;
	}
}

bool operator == (const bigint & A, const bigint & B){
	return !(A<B || B<A);
}

bool operator > (const bigint & A, const bigint & B){
	return B<A;
}

bool operator <= (const bigint & A, const bigint & B){
	return !(A>B);
}

bool operator >= (const bigint & A, const bigint & B){
	return !(A<B);
}

bool operator != (const bigint & A, const bigint & B){
	return !(A==B);
}

/////////////////////////////////////////// Unary operators begins here /////////////////////////////////////////////

bigint operator - (bigint A){
	A.negative=!A.negative;
	if(A.Num[0]==0)	A.negative=false;
	return A;
}

bool operator ! (const bigint & A){
	return (A==0);
}

bigint operator ~ (bigint A){
	if(!A.negative){
		A=A+1;
		A.negative=true;
	}
	else{
		A.negative=false;
		A=A-1;
	}
	return A;
}

bigint operator ++ (bigint & A){
	if(!A.negative){
		for(int i=int(A.Num.sz)-1;i>=0;i--){
			if(A.Num[i]==0){
				A.Num[i]=1;
				return A;
			}
			else	A.Num[i]=0;
		}
		A.Num.insert(A.Num.begin(),1);
		return A;
	}
	else{
		if(A.Num.sz==1){
			A.Num[0]=0;
			A.negative=false;
			return A;
		}
		for(int i=int(A.Num.sz)-1;i>=0;i--){
			if(A.Num[i]==1){
				A.Num[i]=0;
				break;
			}
			else	A.Num[i]=1;
		}
		A.Num=extract0s(A.Num);
		return A;
	}
}

bigint operator ++ (bigint & A,int x){
	bigint ret=A;
	if(!A.negative){
		for(int i=int(A.Num.sz)-1;i>=0;i--){
			if(A.Num[i]==0){
				A.Num[i]=1;
				return ret;
			}
			else	A.Num[i]=0;
		}
		A.Num.insert(A.Num.begin(),1);
		return ret;
	}
	else{
		if(A.Num.sz==1){
			A.Num[0]=0;
			A.negative=false;
			return ret;
		}
		for(int i=int(A.Num.sz)-1;i>=0;i--){
			if(A.Num[i]==1){
				A.Num[i]=0;
				break;
			}
			else	A.Num[i]=1;
		}
		A.Num=extract0s(A.Num);
		return ret;
	}
}

bigint operator -- (bigint & A){
	if(A==0){
		A.Num[0]=1;
		A.negative=true;
		return A;
	}
	if(A.negative){
		for(int i=int(A.Num.sz)-1;i>=0;i--){
			if(A.Num[i]==0){
				A.Num[i]=1;
				return A;
			}
			else	A.Num[i]=0;
		}
		A.Num.insert(A.Num.begin(),1);
		return A;
	}
	else{
		if(A.Num.sz==1){
			A.Num[0]=0;
			A.negative=false;
			return A;
		}
		for(int i=int(A.Num.sz)-1;i>=0;i--){
			if(A.Num[i]==1){
				A.Num[i]=0;
				break;
			}
			else	A.Num[i]=1;
		}
		A.Num=extract0s(A.Num);
		return A;
	}
}

bigint operator -- (bigint & A,int x){
	bigint ret=A;
	if(A==0){
		A.Num[0]=1;
		A.negative=true;
		return ret;
	}
	if(A.negative){
		for(int i=int(A.Num.sz)-1;i>=0;i--){
			if(A.Num[i]==0){
				A.Num[i]=1;
				return ret;
			}
			else	A.Num[i]=0;
		}
		A.Num.insert(A.Num.begin(),1);
		return ret;
	}
	else{
		if(A.Num.sz==1){
			A.Num[0]=0;
			A.negative=false;
			return ret;
		}
		for(int i=int(A.Num.sz)-1;i>=0;i--){
			if(A.Num[i]==1){
				A.Num[i]=0;
				break;
			}
			else	A.Num[i]=1;
		}
		A.Num=extract0s(A.Num);
		return ret;
	}
}

/////////////////////////////////////////// Logical operators begins here /////////////////////////////////////////////

// All logical operators work only for non-negative numbers
bigint operator & (const bigint & A, const bigint & B){
	bigint result;
	result.negative=A.negative&B.negative;
	result.Num.clear();
	for(int i=int(A.Num.sz)-1,j=int(B.Num.sz)-1;i>=0 && j>=0;i--,j--){
		result.Num.pb(A.Num[i]&B.Num[j]);
	}
	reverse(result.Num.begin(),result.Num.end());
	result.Num=extract0s(result.Num);
	return result;
}

bigint operator | (const bigint & A, const bigint & B){
	bigint result;
	result.negative=A.negative|B.negative;
	result.Num.clear();
	for(int i=int(A.Num.sz)-1,j=int(B.Num.sz)-1;i>=0 || j>=0;i--,j--){
		bool b1,b2;
		if(i>=0)	b1=A.Num[i];
		else	b1=0;
		if(j>=0)	b2=B.Num[j];
		else	b2=0;
		result.Num.pb(b1|b2);
	}
	reverse(result.Num.begin(),result.Num.end());
	result.Num=extract0s(result.Num);
	return result;
}

bigint operator ^ (const bigint & A, const bigint & B){
	bigint result;
	result.negative=A.negative^B.negative;
	result.Num.clear();
	for(int i=int(A.Num.sz)-1,j=int(B.Num.sz)-1;i>=0 || j>=0;i--,j--){
		bool b1,b2;
		if(i>=0)	b1=A.Num[i];
		else	b1=0;
		if(j>=0)	b2=B.Num[j];
		else	b2=0;
		result.Num.pb(b1^b2);
	}
	reverse(result.Num.begin(),result.Num.end());
	result.Num=extract0s(result.Num);
	return result;
}

bigint operator << (bigint A, const bigint & B){
	for(int i=0;i<B;i++)	A.Num.pb(0);
	return A;
}

bigint operator >> (bigint A, const bigint & B){
	for(int i=0;i<B;i++){
		if(int(A.Num.sz)>0)	A.Num.pop_back();
		else	break;
	}
	if(A.Num.sz==0){
		A.Num.pb(0);
		A.negative=false;
	}
	return A;
}

/////////////////////////////////////////// Binary operators with equality begins here /////////////////////////////////////////////


bigint operator += (bigint & A, const bigint & B){
	return A=A+B;
}

bigint operator -= (bigint & A, const bigint & B){
	return A=A-B;
}

bigint operator *= (bigint & A, const bigint & B){
	return A=A*B;
}

bigint operator /= (bigint & A, const bigint & B){
	return A=A/B;
}

bigint operator %= (bigint & A, const bigint & B){
	return A=A%B;
}

bigint operator &= (bigint & A, const bigint & B){
	return A=A&B;
}

bigint operator |= (bigint & A, const bigint & B){
	return A=A|B;
}

bigint operator ^= (bigint & A, const bigint & B){
	return A=A^B;
}

bigint operator <<= (bigint & A, const bigint & B){
	return A=A<<B;
}

bigint operator >>= (bigint & A, const bigint & B){
	return A=A>>B;
}

/////////////////////////////////////////// Input Output operators begins here /////////////////////////////////////////////

ostream &operator << ( ostream &out , const bigint& A ) {
	if ( A.negative && A.Num[0]!=0 ) out <<"-";
	string s="0";
	REP(i,A.Num.sz){
		s=intmultiplystring(s.c_str(),2);
		if(A.Num[i]==1)	addstring1(s);
	}
	out<<s;
	return out;
}

istream &operator >> ( istream &in , bigint& A ) {
	char buf[53];
	scanf("%s",buf);
	A=buf;
	return in;
}

//////////////////////////////////////////////// BigInt ends here :) ///////////////////////////////////////////////////////

const int mn = 1005;
int n;
bigint inp[mn],diff[mn];

bigint gcd(bigint a,bigint b){
	if(!b)	return a;
	return gcd(b,a%b);
}

int main(){
	
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int Kase=GI;
	FOR(kase,1,Kase+1){
		n=GI;
		REP(i,n)	cin>>inp[i];
		sort(inp,inp+n);
		REP(i,n-1)	diff[i]=inp[i+1]-inp[i];
		bigint g=diff[0];
		FOR(i,1,n-1)	g=gcd(g,diff[i]);
		printf("Case #%d: ",kase);
		cout<<(inp[0]+g-1)/g*g-inp[0]<<endl;
		cerr<<"Completed:"<<kase<<endl;
	}
	
	cerr<<"Completed"<<endl;
	while(1);
	return 0;
}
