#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

using namespace std;

int n, m, z;
char f[55][55];
int p[55][55][55];
int memo[55][55][55];
int cur = 1;

int dfs( int y, int x, int lx, int rx )
{
	int i, j;
	if( y == n - 1 ) return 0;

	while( lx && f[y][lx - 1] != '#' ) -- lx;
	while( rx < m - 1 && f[y][rx + 1] != '#' ) ++ rx;

	while( x < rx && f[y + 1][x + 1] == '#' ) ++ x;
	int rg = x;
	if( x < rx ) rx = x + 1;

	while( x > lx && f[y + 1][x - 1] == '#' ) -- x;
	int lg = x;
	if( x > lx ) lx = x - 1;

	int & ret = memo[y][lx][rx];
	if( p[y][lx][rx] == cur ) return ret;
	p[y][lx][rx] = cur;
	ret = 1000000000;

	if( lx < lg )
	{
		for( i = y + 1; i < n; ++ i ) if( f[i][lx] == '#' ) break;
		-- i;
		int l = i - y;
		if( l <= z ) ret = min( ret, dfs( i, lx, lx, lx ) );
	}
	if( rx > rg )
	{
		for( i = y + 1; i < n; ++ i ) if( f[i][rx] == '#' ) break;
		-- i;
		int l = i - y;
		if( l <= z ) ret = min( ret, dfs( i, rx, rx, rx ) );
	}
	for( int ln = lg; ln <= rg; ++ ln )
	{
		if( lg != rg && y < n - 1 && f[y + 2][ln] != '#' )
		{
			for( i = y + 2; i < n; ++ i ) if( f[i][ln] == '#' ) break;
			-- i;
			int l = i - y;
			if( l <= z ) ret = min( ret, 1 + dfs( i, ln, ln, ln ) );
		}
		for( int rn = ln; rn <= rg; ++ rn ) if( ln != lg || rn != rg )
		{
			if( y < n - 1 && f[y + 2][rn] != '#' )
			{
				if( rn == ln ) continue;
				if( f[y + 2][ln] != '#' ) break;
			}
			int newx = rn;
			if( y < n - 1 && f[y + 2][rn] != '#' ) -- newx;

			ret = min( ret, dfs( y + 1, newx, ln, rn ) + rn - ln + 1 );
			if( y == 0 && ret == 2 )
				ret = 2;
			if( y < n - 1 && f[y + 2][rn] != '#' )
				break;
			
		}
	}
	return ret;
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "moo.in", "r", stdin );
	freopen( "moo.out", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		fprintf( stderr, "%d\n", t );
		scanf( "%d %d %d", &n, &m, &z );
		fi( n ) scanf( "%s", f[i] );
		_( p, 0 );
		++ cur;
		fi( m ) if( f[0][i] == '#' ) break;
		int ans = dfs( 0, 0, 0, i - 1 );
		printf( "Case #%d: ", t );
		if( ans > n * m ) printf( "No\n" );
		else printf( "Yes %d\n", ans );
	}

	return 0;
}
