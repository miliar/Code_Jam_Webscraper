#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <cmath>
#include <cassert>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

#define fo(a,b,c) for( (a) = (b); (a) < (c); ++ (a) )
#define fr(a,b) fo( (a), 0, (b) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define all(v) (v).begin( ), (v).end( )
#define pb push_back
#define mp make_pair

int n, m;
int w, h;
int cnt[1 << 10];
const int mod = 10007;

int num[12][12];
int divs[mod][mod];

int cnk( int k, int n )
{
	int i;
	int ret = 1;

	fi( k )
	{
		ret = ( ret * ( ( n - i ) % mod ) ) % mod;
		ret = divs[ret][( i + 1 ) % mod];
	}

	return ret;
}

int count( int x, int y )
{
	if( x < 0 || y < 0 ) return 0;
	if( ( x + y ) % 3 ) return 0;
	if( x > y ) swap( x, y );
	int a = y - x;
	x -= a;
	if( x < 0 ) return 0;
	int b = ( x ) / 3;
	return cnk( b, a + b + b );
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );

	cnt[0] = 0;
	fi( 1 << 10 ) if( i ) cnt[i] = cnt[i&(i-1)] + 1;

	scanf( "%d", &t );

	fi( mod ) fj( mod ) if( j ) divs[( i * j ) % mod][j] = i;

	for( tt = 1; tt <= t; ++ tt )
	{
		vector< pair< int, int > > c;
		scanf( "%d %d %d", &w, &h, &n );
		fi( n )
		{
			int a, b;
			scanf( "%d %d", &a, &b );
			-- a; -- b;
			c.pb( mp( a, b ) );
		}
		c.pb( mp( 0, 0 ) );
		c.pb( mp( w - 1, h - 1 ) );
		sort( all( c ) );

		fi( c.size( ) ) fj( i ) num[j][i] = count( c[i].first - c[j].first, c[i].second - c[j].second );

		int ans = 0;
		fi( 1 << n )
		{
			int cur = 1;
			int mask = 1 + ( i << 1 ) + ( 1 << ( 1 + n ) );
			vector< int > q;
			fj( 2 + n ) if( mask & ( 1 << j ) ) q.pb( j );
			fj( q.size( ) - 1 ) ( cur *= num[q[j]][q[j + 1]] ) %= mod;
			if( cnt[i] % 2 == 0 ) ans += cur;
			else ans -= cur;
			ans = ( ans + mod ) % mod;
		}
		printf( "Case #%d: %d\n", tt, ans );
	}

	return 0;
}
