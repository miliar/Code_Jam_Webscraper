//////// Header Includes /////////
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <iosfwd>
#include <iomanip>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <iterator>
#include <string>
#include <sstream>
#include <cmath>
#include <cassert>
#include <cctype>
#include <fstream>
#include <functional>
#include <utility>
#include <algorithm>
#include <list>
/////////////////////////////

using namespace std;

////////////////////////// Macro Functions /////////////////////////////
#define BUG( x ) if( DEBUG ) cout << #x << " = " << x << endl
#define FOR( i, a, b ) for( int i = a; i < b; ++i )
#define RFOR( i, a, b ) for( int i = b; i >= a; --i )
#define LET( x, a ) __typeof( a ) x = a
#define REP( i, N ) FOR( i, 0, N )
#define RREP( i, N ) RFOR( i, N, 0 )
#define TWO( x ) ( 1LL << ( x ) )
#define ALL( x ) ( x ).begin(), ( x ).end()
#define RALL( x ) ( x ).rbegin(), ( x ).rend()
#define CLEAR( x ) memset( ( x ), 0, sizeof( ( x ) ) )
#define SORT( x ) sort( ( x ).begin(), ( x ).end() )
#define FOREACH( it, v ) for( LET( it, ( v ).begin() ); it != ( v ).end(); ++it )
#define PB( x ) push_back( ( x ) )
#define SIZE( x ) ( ( int ) ( x ).size() )
#define MP( x, y ) make_pair( ( x ), ( y ))
////////////////////////////////////////////////////////////////////////

////////// Typedefs and Definitions ///////////////
typedef vector< int > VI;
typedef vector< string > VS;
typedef vector< double > VD;
typedef vector< VI > VVI;
typedef vector< VS > VVS;
typedef stringstream SS;
typedef pair< int, int > PII;
typedef long long LL;
typedef unsigned long long ULL;
typedef vector< PII > VPII;
typedef vector< LL > VLL;
///////////////////////////////////////////////////

/////////////// Constants /////////////////
const bool DEBUG = true;
const double EPS = 1e-8;
const int INF  = 100000000;
const LL INFLL = 1000000000000000000LL;
///////////////////////////////////////////

/////////////////////// Pre-Written Functions /////////////////////////////////////////////////////////////////////////////////
vector< int > tokenize( string s ){ stringstream sin( s ); vector< int > v; int x; while( sin >> x ) { v.PB( x ); } return v; }
int rInt(){ int nT = -1; scanf( "%d", &nT ); return nT; }
int strToInt( string &s ) { int nT = 0; REP( i, SIZE( s ) ) nT = nT * 10 + ( s[i] - '0' ); return nT; }
string intToStr(int N){ string s;do{s.PB(N%10+'0');N/=10;}while(N);reverse(ALL(s)); return s; }
string vIntToStr(VI V){ string s;REP(i,SIZE( V )) s.PB(V[i]+'0');return s; }
string rStr(){ char nStr[1 << 15]; scanf( "%s", nStr ); return nStr; }
VI strToVInt( string &s ){ VI V;REP(i,SIZE( s )) V.PB(s[i]-'0');return V; }
LL rLL(){ LL nT = -1; cin >> nT; return nT; }
template< class T > inline int size( const T& c ) { return ( int ) c.size(); }
template<class T> ostream& operator << (ostream &O,vector<T> &V) { O<<"{"; REP(i,V.SZ-1) O<<V[i]<<", ";O<<V[V.SZ-1];O<<"}";return O;}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

typedef vector< int > BigInteger;

/////////////////////////////////////////////////////////////
string toString( const BigInteger& x );
bool compare( const BigInteger& x, const BigInteger& y );
bool isZero( BigInteger& x );
void resolve( BigInteger& x );
void modulo( BigInteger& a, BigInteger &b );
void subtract( BigInteger& x, BigInteger& y );
void insert( BigInteger& x, int a );
BigInteger toBigInteger( string& s );
BigInteger findResult( vector< BigInteger >& v );
BigInteger getGcd( BigInteger x, BigInteger v );
/////////////////////////////////////////////////////////////

const bool contest = 1;

int main()
{
	if( contest ) {
		freopen( "input.txt", "r", stdin );
		freopen( "output.txt", "w", stdout );
	}
	int nTest = rInt();
	for( int kase = 1; kase <= nTest; ++kase ) {
		vector< BigInteger > v;
		int n = rInt();
		for( int i = 0; i < n; ++i ) {
			string s = rStr();
			v.PB( toBigInteger( s ) );
		}
		BigInteger result = findResult( v );
		string answer = toString( result );
		printf( "Case #%d: %s\n", kase, answer.c_str() );
	}
	return 0;
}

string toString( const BigInteger& x )
{
	string s;
	for( int i = size( x ) - 1; i >= 0; --i ) {
		s.PB( x[i] + '0' );
	}
	return s;
}

bool compare( const BigInteger& x, const BigInteger& y )
{
	string a = toString( x ), b = toString( y );
	if( size( a ) < size( b ) || ( size( a ) == size( b ) && a < b ) )
		return true;
	else
		return false;
}

void resolve( BigInteger& x )
{
	x.resize( size( x ) + 5, 0 );
	int iterations = size( x );
	for( int i = 0; i + 1 < iterations; ++i ) {
		x[ i + 1 ] += x[i] / 10;
		x[i] %= 10;
	}
	int last = size( x ) - 1;
	while( last >= 1 && x[ last ] == 0 )
		--last;
	x.resize( last + 1 );
}

void modulo( BigInteger& a, BigInteger &b )
{
	BigInteger x;
	int iterations = size( a );
	for( int i = iterations - 1; i >= 0; --i ) {
		insert( x, a[i] );
		while( compare( b, x ) || x == b ) {
			subtract( x, b );
		}
	}
	a = x;
}

void subtract( BigInteger& x, BigInteger& y )
{
	int iterations = size( y );
	for( int i = 0; i < iterations; ++i ) {
		x[i] -= y[i];
	}
	iterations = size( x );
	for( int i = 0; i + 1 < iterations; ++i ) {
		if( x[i] < 0 ) {
			x[i] += 10;
			x[i + 1]--;
		}
	}
	resolve( x );
}

BigInteger toBigInteger( string& s )
{
	BigInteger x;
	int iterations = size( s );
	for( int i = iterations - 1; i >= 0; --i )
		x.PB( s[i] - '0' );
	return x;
}

BigInteger findResult( vector< BigInteger >& v )
{
	sort( v.begin(), v.end(), compare );
	for( int i = 1; i < size( v ); ++i )
		if( v[i] == v[i - 1] )
			v.erase( v.begin() + i-- );
	BigInteger x = v[1];
	if( compare( v[0], v[1] ) ) {
		subtract( x, v[0] );
		resolve( x );
	}
	for( int i = 2; i < size( v ); ++i ) {
		BigInteger y = v[i];
		subtract( y, v[i - 1] );
		x = getGcd( x, y );
	}
	BigInteger result = v[0];
	modulo( result, x );
	if( isZero( result ) )
		return result;
	subtract( x, result );
	return x;
}

BigInteger getGcd( BigInteger x, BigInteger v )
{
	if( isZero( v ) )
		return x;
	else {
		modulo( x, v );
		return getGcd( v, x );
	}
}

bool isZero( BigInteger& x )
{
	return ( size( x ) == 1 && x[0] == 0 );
}

void insert( BigInteger& x, int a )
{
	BigInteger y;
	y.PB( a );
	for( int i = 0; i < size( x ); ++i )
		y.PB( x[i] );
	x = y;
	resolve( x );
}

// Powered by PhoenixAI
