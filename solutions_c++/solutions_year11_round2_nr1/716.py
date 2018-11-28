/*
	author: AmazingCaddy
	time: 2011/5/22 0:10
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

const int maxn = 104;
const double pi = acos( -1.0 );
const double inf = 1e20;
const double eps = 1e-8;

char g[ maxn ][ maxn ];
int num[ maxn ], win[ maxn ];
double wp[ maxn ], owp[ maxn ], oowp[ maxn ];
double rpi[ maxn ];

int main(int argc, char *argv[])
{
	int cas, n;
	freopen( "A-large.in", "r", stdin );
	freopen( "outA_Large.txt", "w", stdout );
	scanf( "%d", &cas );
	for( int t = 1; t <= cas; t++ )
	{
		scanf( "%d", &n );
		for( int i = 0; i < n; i++ )
		{
			scanf( "%s", g[ i ] );
			num[ i ] = 0;
			win[ i ] = 0;
			for( int j = 0; j < n; j++ )
			{
				if( g[ i ][ j ] != '.' ) num[ i ]++;
				if( g[ i ][ j ] == '1' ) win[ i ]++;
			}
		}
		for( int i = 0; i < n; i++ )
			wp[ i ] = win[ i ] * 1.0 / num[ i ];

		for( int i = 0; i < n; i++ )
		{
			double sum = 0;
			for( int j = 0; j < n; j++ )
			{
				if( g[ i ][ j ] != '.' )
				{
					sum = sum + ( win[ j ] * 1.0 - ( g[ j ][ i ] == '1' ) ) 
						/ ( num[ j ] - 1 );
				}
			}
			owp[ i ] = sum / num[ i ];
		}

		for( int i = 0; i < n; i++ )
		{
			double sum = 0;
			for( int j = 0; j < n; j++ )
			{
				if( g[ i ][ j ] != '.' )
					sum += owp[ j ];
			}
			oowp[ i ] = sum / num[ i ];
		}

		printf( "Case #%d:\n", t );
		for( int i = 0; i < n; i++ )
		{
			rpi[ i ] = 0.25 * wp[ i ] + 0.5 * owp[ i ] + 0.25 * oowp[ i ];
			printf( "%.10lf\n", rpi[ i ] );
		}
	}
	return 0;
}
