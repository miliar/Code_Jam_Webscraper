/*
	author: AmazingCaddy
	time: 2011/5/7  15:09
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

const int maxn = 10004;
int sta[ maxn ];
char buf[ maxn ];
int top;
int to2[ 40 ][ 40 ];
int to3[ 40 ][ 40 ];

int main(int argc, char *argv[])
{
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );
	int c, d, n;
	int cas;
	scanf( "%d", &cas );
	for( int t = 1; t <= cas; t++ )
	{
		memset( to2, -1, sizeof( to2 ) );
		memset( to3, -1, sizeof( to3 ) );
		scanf( "%d", &c );
		for( int i = 0; i < c; i++ )
		{
			scanf( "%s", buf );
			int x = buf[ 0 ] - 'A';
			int y = buf[ 1 ] - 'A';
			int z = buf[ 2 ] - 'A';
			to3[ x ][ y ] = z;
			to3[ y ][ x ] = z;
		}
		scanf( "%d", &d );
		for( int i = 0; i < d; i++ )
		{
			scanf( "%s", buf );
			int x = buf[ 0 ] - 'A';
			int y = buf[ 1 ] - 'A';
			to2[ x ][ y ] = 1;
			to2[ y ][ x ] = 1;
		}
		scanf( "%d%s", &n, buf );
		top = 0;
		int tmp;
		for( int i = 0; i < n; i++ )
		{
			sta[ top++ ] = buf[ i ] - 'A';
			while( top >= 2 && ( tmp = to3[ sta[ top - 1 ] ][ sta[ top - 2 ] ] ) != -1 )
			{
				top -= 2;
				sta[ top++ ] = tmp;
			}
			while( top >= 2 )
			{
				int k = top;
				for( int j = top - 2; j >= 0; j-- )
				{
					if( to2[ sta[ top - 1 ] ][ sta[ j ] ] != -1 )
					{
						k = j;
						break;
					}
				}
				if( k == top ) break;
				top = 0;
			}
		}
		printf( "Case #%d: [", t );
		for( int i = 0; i < top; i++ )
		{
			if( i ) printf( ", " );
			printf( "%c", sta[ i ] + 'A' );
		}
		printf( "]\n" );
	}
	return 0;
}
