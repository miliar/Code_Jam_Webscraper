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

#define BUG( x ) if( DEBUG ) cout << #x << " = " << x << endl
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
#define PB( x ) push_back( ( x ) )
#define SIZE( x ) ( ( int ) ( x ).size() )
#define MP( x, y ) make_pair( ( x ), ( y ))

typedef vector< int > VI; typedef vector< string > VS; typedef vector< double > VD;
typedef vector< VI > VVI; typedef vector< VS > VVS; typedef stringstream SS;
typedef pair< int, int > PII; typedef long long LL; typedef unsigned long long ULL;
typedef vector< PII > VPII; typedef vector< LL > VLL;

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
template< class T > ostream& operator << (ostream &O, vector< T > &V) { O << "{"; REP(i, size( V )-1) O << V[i] << ", "; O << V[ size( V )-1]; O << "}";return O;}
template< class T > inline int size( const T& c ) { return ( int ) c.size(); }

const bool contest = 1;


bool oddMoves( int x, int y )
{
	if( max( x - y, y - x ) < min( x, y ) ) {
		if( x > y ) return !oddMoves( y, x - y );
		else return !oddMoves( y - x, x );
	}
	return true;
}

int main()
{
	if( contest ) {
		freopen( "input.txt", "r", stdin );
		freopen( "output.txt", "w", stdout );
	}
	int nTest = rInt();
	for( int kase = 1; kase <= nTest; ++kase ) {
		int A1 = rInt(), A2 = rInt(), B1 = rInt(), B2 = rInt();
		int ctr = 0;
		for( int i = A1; i <= A2; ++i )
			for( int j = B1; j <= B2; ++j )
				if( oddMoves( i, j ) ) {
					ctr++;
				}
		printf( "Case #%d: %d\n", kase, ctr );
	}
	return 0;
}

// Powered by PhoenixAI
