#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int TABLE[ 256 ][ 256 ];
int IN[ 1000 ];
int D, I, M, N;

int minRange( int x[], int to )
{
		if( M == 0 )
				return x[ to ];
		int minx = 10000000;
		for( int i=0;i<=255;i++ ) {
				int a = abs( i - to ) - 1;
				if( a < 0 ) a = 0;
				minx = min( x[i] + ( a / M ) * I, minx );
		}
		return minx;
}
int main()
{
		int ccN;
		scanf("%d", &ccN);
		for( int cc=0;cc<ccN;cc++ ) {
				memset( TABLE, 0, sizeof( TABLE ) );
				scanf("%d%d%d%d", &D, &I, &M, &N );
				for( int i=0;i<N;i++ )
						scanf("%d", &IN[ i ] );
				for( int i=0;i<256;i++ ) {
						TABLE[ 0 ][ i ] = min( abs( i - IN[0] ), D );
				}
				for( int i=1;i<N;i++ ) {
						for( int j=0;j<256;j++ ) {
								TABLE[ i ][ j ] = min( abs( IN[i] - j ) + minRange( TABLE[ i-1 ], j ), 
														TABLE[ i-1 ][ j ] + D );
						}
				}
				int minx = 100000000;
				for( int i=0;i<256;i++ ) {
						minx = min( minx, TABLE[N-1][i] );
				}
				printf("Case #%d: %d\n", cc + 1, minx );
		}
		return 0;
}
