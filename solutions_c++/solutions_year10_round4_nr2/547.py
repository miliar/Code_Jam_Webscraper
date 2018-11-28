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
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

int n, m;
int price[2000];
int expc[2000];

int d[1105][15];

void rec( int l, int r, int id )
{
	if( r - l == 2 )
	{
		int i;
		fi( 15 )
		{
			if( expc[l] > i && expc[l + 1] > i )
			{
				d[id][i] = 0;
			}
			else if( expc[l] >= i && expc[l + 1] >= i )
				d[id][i] = price[id];
		}
	}
	else
	{
		int e = ( l + r ) / 2;
		rec( l, e, id * 2 + 1 );
		rec( e, r, id * 2 );

		int i, j, k;
		fi( 15 ) // we miss
		{
			fj( 15 ) if( d[id * 2 + 1][j] != -1 ) // left miss
			fk( 15 ) if( d[id * 2][k] != -1 ) // right miss
			{
				// watch
				int nv = d[id * 2 + 1][j] + d[id * 2][k] + price[id];
				if( ( j >= i && k >= i ) && ( d[id][i] == -1 || d[id][i] > nv ) ) d[id][i] = nv;
				// don't watch
				nv = d[id * 2 + 1][j] + d[id * 2][k];
				if( ( j > i && k > i ) && ( d[id][i] == -1 || d[id][i] > nv ) ) d[id][i] = nv;
			}
		}
	}
}

int main( )
{
	int i, j, k, t, tt;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		_( d, -1 );
		printf( "Case #%d:", t );
		n = ni( );
		fi( 1 << n ) expc[i] = ni( );
		fi( ( 1 << n ) - 1 ) price[(1 << n) - i - 1] = ni( );

		rec( 0, 1 << n, 1 );
		int ans = 1000000000;
		fi( 15 ) if( d[1][i] < ans && d[1][i] != -1 ) ans = d[1][i];
		printf( " %d\n", ans );
	}

	return 0;
}
