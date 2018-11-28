#include <iostream>
#include <iosfwd>
#include <iomanip>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>

#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>

#include <fstream>
#include <functional>
#include <utility>
#include <algorithm>

using namespace std;

#define BUG( x ) if( DEBUG ) cout << __LINE__ << ": " << #x << " = " << x << endl
#define LET( x, a ) __typeof( a ) x = a
#define FOR( i, a, b ) for( LET( i, ( a ) ); i < ( b ); ++i )
#define RFOR( i, a, b ) for( LET( i, ( a ) ); i >= ( b ); --i )
#define REP( i, N ) FOR( i, 0, N )
#define RREP( i, N ) RFOR( i, N, 0 )
#define ALL( x ) ( x ).begin(), ( x ).end()
#define RALL( x ) ( x ).rbegin(), ( x ).rend()
#define CLEAR( x ) memset( ( x ), 0, sizeof( ( x ) ) )
#define FILL( x, v ) memset( ( x ), ( v ), sizeof( ( x ) ) )
#define SORT( x ) sort( ( x ).begin(), ( x ).end() )
#define UNIQUE( x ) SORT( x ), ( x ).resize( unique( ( x ).begin(), ( x ).end() ) - ( x ).begin() )
#define REVERSE( x ) reverse( ( x ).begin(), ( x ).end() )
#define FOREACH( it, v ) for( LET( it, ( v ).begin() ); it != ( v ).end(); ++it )
#define PRESENT( x, v ) ( find( ALL( ( x ) ), ( v ) ) != ( x ).end() )
#define CPRESENT( x, v ) ( ( x ).find( ( v ) ) != ( x ).end() )
#define LAST( x ) x[ size( ( x ) ) - 1 ]
#define PB( x ) push_back( ( x ) )
#define SIZE( x ) ( ( int ) ( x ).size() )
#define MP( x, y ) make_pair( ( x ), ( y ) )

typedef vector< int > VI; typedef vector< string > VS; typedef vector< double > VD;
typedef vector< VI > VVI; typedef vector< VS > VVS; typedef stringstream SS;
typedef pair< int, int > PII; typedef long long LL; typedef unsigned long long ULL;
typedef vector< PII > VPII; typedef vector< LL > VLL; typedef vector< bool > VB;

const bool DEBUG = true;
const double EPS = 1e-8;
const int INF  = 100000000;
const LL INFLL = 1000000000000000000LL;

vector< int > tokenizeInt( string s ){ stringstream sin( s ); vector< int > v; int x; while( sin >> x ) { v.PB( x ); } return v; }
vector< string > tokenizeStr( string s ){ stringstream sin( s ); vector< string > v; string x; while( sin >> x ) { v.PB( x ); } return v; }
int rInt(){ int nT = -1; scanf( "%d", &nT ); return nT; }
int strToInt( string &s ) { int nT = 0; REP( i, SIZE( s ) ) nT = nT * 10 + ( s[i] - '0' ); return nT; }
string intToStr( int N ){ string s; do { s.PB( N % 10 + '0'); N /= 10; } while( N ); reverse( ALL( s ) ); return s; }
string vIntToStr( VI& V ){ string s; REP( i, SIZE( V ) ) s.PB( V[i] + '0'); return s; }
string rStr(){ char nStr[1 << 15]; scanf( "%s", nStr ); return nStr; }
VI strToVInt( string &s ){ VI V; REP( i, SIZE( s ) ) V.PB( s[i] - '0' ); return V; }
LL rLL(){ LL nT = -1; cin >> nT; return nT; }
inline LL two( int x ) { return ( 1LL << ( x ) ); }
template< class T > ostream& operator << (ostream &O, vector< T > &V){ O << "{"; REP(i, size( V )-1) O << V[i] << ", "; O << V[ size( V )-1]; O << "}";return O;}
template< class T > inline int size( const T& c ) { return ( int ) c.size(); }

const bool contest = 1;

bool allFalse( vector< VB >& v )
{
	for( int i = 0; i < size( v ); ++i )
		for( int j = 0; j < size( v[0] ); ++j )
			if( v[i][j] )
				return false;
	return true;
}

void display(vector< VB >& v)
{
	for( int i = 0; i < 10; ++i ) {
		for( int j = 0; j < size( v[0] ); ++j )
			cout << ( int ) v[i][j];
		cout << endl;
	}
	cout << endl;
}

int getCount( vector< VB >& v )
{
	int count = 0;
	int lastCol = size( v[0] ) - 1;
	int lastRow = size( v ) - 1;
	while( !allFalse( v ) ) {
		for( int i = size( v ) - 1; i >= 1; --i ) {
			for( int j = size( v[0] ) - 1; j >= 1; --j ) {
				if( v[i][j] && !v[i - 1][j] && !v[i][j - 1] )
					v[i][j] = false;
				if( !v[i][j] && v[i - 1][j] && v[i][j - 1] )
					v[i][j] = true;
			}
		}
		for( int i = lastRow; i >= 1; --i )
			if( !v[i - 1][0] )
				v[i][0] = false;
		for( int j = lastCol; j >= 1; --j )
			if( !v[0][j - 1] )
				v[0][j] = false;
		v[0][0] = false;
		count++;
	}
	return count;
}

int main()
{
	if( contest ) {
		freopen( "input.txt", "r", stdin );
		freopen( "output.txt", "w", stdout );
	}
	int nTest = rInt();
	for( int kase = 1; kase <= nTest; ++kase ) {
		int r = rInt();
		vector< VB > m( 100, VB ( 100, 0 ) );
		for( int i = 1; i <= r; ++i ) {
			int a = rInt() - 1, b = rInt() - 1, c = rInt() - 1, d = rInt() - 1;
			int x1 = min( a, c ), x2 = max( a, c ), y1 = min( b, d ), y2 = max( b, d );
			for( int j = x1; j <= x2; ++j )
				for( int k = y1; k <= y2; ++k )
					m[k][j] = 1;
		}
		vector< VB > n( 100, VB ( 100, 0 ) );
		for( int i = 0; i < size( n ); ++i )
			for( int j = 0; j < size( n[0] ); ++j )
				n[i][j] = m[ 100 - i - 1 ][ j ];
		int count = getCount( m );
		printf( "Case #%d: %d\n", kase, count );
	}
	return 0;
}

// Powered by PhoenixAI
