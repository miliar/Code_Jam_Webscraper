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
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

const bool contest = 1;

inline int next( int x, int n )
{
	return ( x % n );
}

LL findResult( vector< LL >& v, int R, int capacity, int n )
{
	vector< int > nextIndex( size( v ), 0 );
	vector< LL > rounds( size( v ), 0 );
	for( int i = 0; i < n; ++i ) {
		LL total = v[i];
		int counter = 1;
		for( int j = next( i + 1, n ); counter < n; j = next( j + 1, n ) ) {
			if( total + v[j] > capacity ) {
				nextIndex[i] = j;
				break;
			}
			else {
				total += v[j];
				counter++;
			}
			if( counter == n ) {
				nextIndex[i] = i;
			}
		}
		rounds[i] = total;
	}
	LL result = 0;
	int curr = 0;
	for( int i = 0; i < R; ++i ) {
		result = result + rounds[ curr ];
		curr = nextIndex[ curr ];
	}
	return result;
}

int main()
{
	if( contest ) {
		freopen( "input.txt", "r", stdin );
		freopen( "output.txt", "w", stdout );
	}
	int nTest = rInt();
	for( int kase = 1; kase <= nTest; ++kase ) {
		int R = rInt(), k = rInt(), N = rInt();
		vector< LL > v( N, 0 );
		for( int i = 0; i < N; ++i )
			v[i] = rInt();
		LL result = findResult( v, R, k, N );
		printf( "Case #%d: %lld\n", kase, result );
	}
	return 0;
}

// Powered by PhoenixAI
