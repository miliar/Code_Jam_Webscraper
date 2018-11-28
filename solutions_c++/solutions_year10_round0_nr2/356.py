#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

typedef long long ll ; 
int c , n , i , j , t , tt ;

struct BigInt {
	int l , a[60] ;
	BigInt() { l=0 ; memset(a,0,sizeof a) ; }

	ll value()
	{
		ll ret = 0 ;
		for ( int i=l-1 ; i>=0 ; --i ) ret = ret*10 + a[i] ;
		return ret ;
	}
};

BigInt a[2000] , d ;

BigInt operator + ( BigInt a , BigInt b ) 
{
	BigInt ret ; int i ;
	ret.l = max( a.l , b.l ) ;
	for ( i=0 ; i<ret.l ; ++i ) {
		ret.a[i] = a.a[i] + b.a[i] ;
		if ( ret.a[i] >= 10 ) ret.a[i] -= 10 , ++ret.a[i+1] ;
	}
	if ( ret.a[ret.l] ) ++ret.l ; 
	return ret ;
}

bool operator < ( BigInt a , BigInt b ) 
{
	if ( a.l != b.l ) return a.l < b.l ; 
	for ( int i=a.l-1 ; i>=0 ; --i ) if ( a.a[i]!=b.a[i] ) return a.a[i] < b.a[i] ; 
	return false ;
}

BigInt operator - ( BigInt a , BigInt b )  //return abs(a-b) 
{
	if ( a<b ) swap( a , b ) ;
	BigInt ret = a ;
	for ( int i=0 ; i<ret.l ; ++i ) {
		ret.a[i] -= b.a[i] ;
		if ( ret.a[i]<0 ) ret.a[i]+=10 , ret.a[i+1]-- ; 
	}
	while ( ret.l && !ret.a[ret.l-1] ) --ret.l ; 
	return ret ;
}

BigInt operator << ( BigInt a , int b )  // return a * 10^b 
{
	int i ; 
	for ( i=a.l-1 ; i>=0 ; --i ) a.a[i+b] = a.a[i] ; 
	for ( i=b-1 ; i>=0 ; --i ) a.a[i] = 0 ;
	a.l += b ;
	return a ;
}

BigInt operator % ( BigInt a , BigInt b ) 
{
	int base ;
	for ( base = a.l-b.l ; base>=0 ; --base ) {
		BigInt tmp = b << base ;
		while ( !(a<tmp) ) a = a-tmp ;
	}
	return a ;
}

BigInt gcd( BigInt a , BigInt b ) 
{
	if ( a<b ) return gcd( b , a ) ;
	if ( !b.l ) return a ;
	return gcd( b , a%b ) ; 
}

istream &operator >> ( istream &input , BigInt & a )
{
	string tmp ;  a = BigInt() ; 
	input >> tmp ; 
	a.l = tmp.size() ;
	for ( int i=0 ; i<a.l ; ++i ) a.a[i] = tmp[a.l-i-1] - 48 ; 
	return input ;
}

ostream &operator << ( ostream &output , BigInt &a ) 
{
	if ( !a.l ) output << 0 ;
	else {
		for ( int i=a.l-1 ; i>=0 ; --i ) output << a.a[i] ; 
	}
	return output ;
}

int main()
{
	freopen("B-large.in","r",stdin) ; 
	freopen("b-large.out","w",stdout) ; 
	cin >> t ;
	for ( tt=1 ; tt<=t ; ++tt ) {
		cin >> n ; 
		for ( i=1 ; i<=n ; ++i ) cin >> a[i] ; 
		d = a[1] - a[2] ; 
		for ( i=2 ; i<n ; ++i ) d = gcd( d , a[i] - a[i+1] ) ;

		BigInt tmp = a[1] % d ;
		if ( !tmp.l ) tmp = d ; 
		cout << "Case #" << tt << ": " << (d-tmp) << endl ; 
	}		
}