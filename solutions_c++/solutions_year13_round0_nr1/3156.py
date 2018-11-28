#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <sstream>
#include <utility>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>
#include <assert.h>
#include <string.h>
#include <limits>
using namespace std;

#define INF 100000000
#define PI 3.1415926535897932384626433832795
#define PI_HALF 1.570796327
#define EPS 1e-9

typedef unsigned int UI;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair< int, int > PII;
typedef pair< LL, LL > PLL;
typedef vector< int > VI;
typedef vector< LL > VLL;
typedef vector< string > VS;
typedef vector< PII > VPII;
typedef vector< PLL > VPLL;

#define X first
#define Y second
#define PB push_back
#define MP make_pair
#define SZ(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort( ALL( c ) )
#define SORT_(c,f) sort( ALL( c ), f )
#define FILL(x,v) memset( x, v, sizeof( x ) );

#define REP(i,n) for ( int i = 0, max_ = (n); i < max_; ++i )
#define REPD(i,n) for ( int i = (n) - 1; i >= 0; --i )
#define FOR(i,a,b) for ( int i = (a), max_ = (b); i < max_; ++i )
#define FORD(i,a,b) for ( int i = (a) - 1, min_ = (b); i >= min_; --i )

int ToInt ( string & s, int len ) { int r = 0; REP(i,len) { r *= 10; r += s[i] - '0'; } return r; }
int GCD ( int a, int b ) { return b != 0 ? GCD(b, a % b) : a; }
int LCM ( int a, int b ) { return a*(b / GCD(a,b)); }
LL Pow ( LL n, LL e ) { if ( e == 0 ) return 1; if ( e == 1 ) return n; else if ( e & 1 ) { LL t = Pow(n,e/2); return n*t*t; } else { LL t = Pow(n,e/2); return t*t; } }

int dx[ 4 ] = { 1, 0, 1, -1 };
int dy[ 4 ] = { 0, 1, 1,  1 };

char m[ 4 ][ 4 ];

bool IsX ( char c ) { return c == 'X' || c == 'T'; }
bool IsO ( char c ) { return c == 'O' || c == 'T'; }

int main ()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "f.out", "w", stdout );

	int T, C = 0;
	cin >> T;
	while ( T-- )
	{
		bool completed = true;
		REP(i,4) REP(j,4)
		{
			cin >> m[ i ][ j ];
			if ( m[ i ][ j ] == '.' )
				completed = false;
		}

		bool winX = false;
		REP(i,4) if ( IsX( m[ i ][ 0 ] ) && IsX( m[ i ][ 1 ] ) && IsX( m[ i ][ 2 ] ) && IsX( m[ i ][ 3 ] ) ) winX = true;
		REP(i,4) if ( IsX( m[ 0 ][ i ] ) && IsX( m[ 1 ][ i ] ) && IsX( m[ 2 ][ i ] ) && IsX( m[ 3 ][ i ] ) ) winX = true;
		if ( IsX( m[ 0 ][ 0 ] ) && IsX( m[ 1 ][ 1 ] ) && IsX( m[ 2 ][ 2 ] ) && IsX( m[ 3 ][ 3 ] ) ) winX = true;
		if ( IsX( m[ 3 ][ 0 ] ) && IsX( m[ 2 ][ 1 ] ) && IsX( m[ 1 ][ 2 ] ) && IsX( m[ 0 ][ 3 ] ) ) winX = true;

		bool winO = false;
		REP(i,4) if ( IsO( m[ i ][ 0 ] ) && IsO( m[ i ][ 1 ] ) && IsO( m[ i ][ 2 ] ) && IsO( m[ i ][ 3 ] ) ) winO = true;
		REP(i,4) if ( IsO( m[ 0 ][ i ] ) && IsO( m[ 1 ][ i ] ) && IsO( m[ 2 ][ i ] ) && IsO( m[ 3 ][ i ] ) ) winO = true;
		if ( IsO( m[ 0 ][ 0 ] ) && IsO( m[ 1 ][ 1 ] ) && IsO( m[ 2 ][ 2 ] ) && IsO( m[ 3 ][ 3 ] ) ) winO = true;
		if ( IsO( m[ 3 ][ 0 ] ) && IsO( m[ 2 ][ 1 ] ) && IsO( m[ 1 ][ 2 ] ) && IsO( m[ 0 ][ 3 ] ) ) winO = true;

		if ( winX ) printf( "Case #%d: X won\n", ++C );
		else if ( winO ) printf( "Case #%d: O won\n", ++C );
		else if ( completed ) printf( "Case #%d: Draw\n", ++C );
		else printf( "Case #%d: Game has not completed\n", ++C );
	}

	return 0;
}