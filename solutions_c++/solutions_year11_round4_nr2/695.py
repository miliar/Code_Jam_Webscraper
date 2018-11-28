/*
	author: AmazingCaddy
	time: 
*/
#include <cstdio>
#include <complex>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <vector>
#include <map>
#include <queue>
using namespace std;

typedef __int64 ll;

const int maxn = 504;
const double pi = acos( -1.0 );
const double inf = 1e20;
const double eps = 1e-8;

int g[ maxn ][ maxn ];
char buf[ maxn ][ maxn ];

int Min( int a, int b ) { return ( a < b ? a : b ); }

int check( int x, int y, int n )
{
	double sumx = 0, sumy = 0;
	double cx = x + ( n - 1.0 ) / 2, cy = y + ( n - 1.0 ) / 2;
	for( int i = x; i < x + n; i++ )
	{
		for( int j = y; j < y + n; j++ )
		{
			if( ( i == x && ( j == y || ( j == y + n - 1 ) ) ) ||
				( i == x + n - 1 && ( j == y || j == y + n -1 ) ) )
				continue;
			sumx += ( i - cx ) * g[ i ][ j ];
			sumy += ( j - cy ) * g[ i ][ j ];
		}
	}
	if( fabs( sumx ) < eps && fabs( sumy ) < eps ) return 1;
	return 0;
}

int main(int argc, char *argv[])
{
	freopen( "B-small-attempt0.in", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int R, C, D;
	int cas;
	scanf( "%d", &cas );
	for( int t = 1; t <= cas; t++ )
	{
		scanf( "%d%d%d", &R, &C, &D );
		for( int i = 0; i < R; i++ )
			scanf( "%s", buf[ i ] );
		for( int i = 0; i < R; i++ )
			for( int j = 0; j < C; j++ )
				g[ i ][ j ] = buf[ i ][ j ] - '0';
		int st = Min( R, C );
		int cx, cy, ans = -1;
		for( int k = st; k >= 3; k-- )
		{
			for( int i = 0; i <= R - k; i++ )
			{
				for( int j = 0; j <= C - k; j++ )
				{
					if( check( i, j, k ) ) 
					{
						ans = k;
						goto out;
					}
				}
			}
		}
		out:;
		if( ans == -1 ) printf( "Case #%d: IMPOSSIBLE\n", t );
		else printf( "Case #%d: %d\n", t, ans );
	}
	return 0;
}
