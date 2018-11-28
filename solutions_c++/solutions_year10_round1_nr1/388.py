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

void rotate( VS& v )
{
	VS s = v;
	for( int i = 0; i < size( s ); ++i )
		for( int j = 0; j < size( s ); ++j )
			s[i][j] = v[j][i];
	v = s;
}

void display( VS& v )
{
	cout << "Displaying v " << endl;
	for( int i = 0; i < size( v ); ++i )
		cout << v[i] << endl;
	cout << endl;
}

void gravity( VS& v )
{
	bool flag = true;
	while( flag ) {
		flag = false;
		for( int i = size( v ) - 1; i >= 0; --i )
			for( int j = size( v ) - 1; j >= 0; --j ) {
				if( v[i][j] == '.' ) {
					for( int k = i - 1; k >= 0; --k ) {
						if( v[k][j] != '.' ) {
							swap( v[k][j], v[i][j] );
							flag = true;
							break;
						}
					}
				}
			}
	}
}

bool isBlue( VS& v, int K )
{
	char ch = 'B';
	for( int i = 0; i < size( v ); ++i )
		for( int j = 0; j < size( v ); ++j ) {
			if( v[i][j] == ch ) {
				bool good = true;
				int moves = 0;
				for( int k = j; k <= j + K - 1 && k < size( v ); ++k ) {
					good = good && v[i][k] == ch;
					moves++;
				}
				if( moves == K && good ) return true;
				good = true;
				moves = 0;
				for( int k = i; k <= i + K - 1 && k < size( v ); ++k ) {
					good = good && v[k][j] == ch;
					moves++;
				}
				if( moves == K && good ) return true;
				good = true;
				moves = 0;
				for( int k = 0; k < K; ++k ) {
					if( i + k < size( v ) && j + k < size( v ) && v[i + k][j + k] == ch )
						moves++;
				}
				if( moves == K ) return true;
				good = true;
				moves = 0;
				for( int k = 0; k < K; ++k ) {
					if( i + k < size( v ) && j - k >= 0 && v[i + k][j - k] == ch )
						moves++;
				}
				if( moves == K ) return true;
			}
		}
	return false;
}

bool isRed( VS& v, int K )
{
	char ch = 'R';
	for( int i = 0; i < size( v ); ++i )
		for( int j = 0; j < size( v ); ++j ) {
			if( v[i][j] == ch ) {
				bool good = true;
				int moves = 0;
				for( int k = j; k <= j + K - 1 && k < size( v ); ++k ) {
					good = good && v[i][k] == ch;
					moves++;
				}
				if( moves == K && good ) return true;
				good = true;
				moves = 0;
				for( int k = i; k <= i + K - 1 && k < size( v ); ++k ) {
					good = good && v[k][j] == ch;
					moves++;
				}
				if( moves == K && good ) return true;
				good = true;
				moves = 0;
				for( int k = 0; k < K; ++k ) {
					if( i + k < size( v ) && j + k < size( v ) && v[i + k][j + k] == ch )
						moves++;
				}
				if( moves == K ) return true;
				good = true;
				moves = 0;
				for( int k = 0; k < K; ++k ) {
					if( i + k < size( v ) && j - k >= 0 && v[i + k][j - k] == ch )
						moves++;
				}
				if( moves == K ) return true;
			}
		}
	return false;
}


int main()
{
	if( contest ) {
		freopen( "input.txt", "r", stdin );
		freopen( "output.txt", "w", stdout );
	}
	int nTest = rInt();
	for( int kase = 1; kase <= nTest; ++kase ) {
		int N = rInt(), K = rInt();
		VS v;
		for( int i = 0; i < N; ++i )
			v.PB( rStr() );
		rotate( v );
		gravity( v );
		printf( "Case #%d: ", kase );
		bool blue = isBlue( v, K ), red = isRed( v, K );
		if( blue && red ) printf( "Both" );
		else if( blue && !red ) printf( "Blue" );
		else if( !blue && red ) printf( "Red" );
		else printf( "Neither" );
		printf( "\n" );
	}
	return 0;
}

// Powered by PhoenixAI
