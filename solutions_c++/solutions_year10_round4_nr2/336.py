#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int P, N;
int M[ 2000 ];
int PR[ 12 ][ 2000 ];
long long int TABLE[ 12 ][ 2000 ][ 12 ];

long long int INF = 100000000000LL ;

void DP()
{
	for( int i=0;i<P;i++ ) {
		for( int j=0;j<1<<(P-i);j++ ) {
			for( int k=0;k<=11;k++ ) {
				TABLE[ i ][ j ][ k ] = INF;
			}
		}
	}
	for( int j=0;j<1<<(P);j++ ) {
		for( int k=M[j];k<=11;k++ ) {
			TABLE[ 0 ][ j ][ k ] = 0;
		}
	}
	/*
	for( int i=0;i<P;i++ ) {
		for( int j=0;j<1<<(P-i);j++ ) {
			for( int k=0;k<=11;k++ ) {
				printf("%d ", TABLE[ i ][ j ][ k ]);
			}
		printf("\n");
		}
		printf("\n");
	}
	*/
	for( int i=1;i<=P;i++ ) {
		for( int j=0;j<1<<(P-i);j++ ) {
			for( int k=0;k<=10;k++ ) {
				TABLE[ i ][ j ][ k ] = min( TABLE[i-1][ 2*j ][ k ] + TABLE[i-1][2*j+1][k], 
							TABLE[i-1][ 2*j ][ k+1 ] + TABLE[i-1][2*j+1][k+1] + PR[ i-1 ][ j ] );
				TABLE[ i ][ j ][ k ] = min( TABLE[i][j][k] , INF ); 
				//printf("%d(%d) ", TABLE[ i ][ j ][ k ], PR[ i ][ j ]);
			}
			//printf("\n");
			TABLE[ i ][ j ][ 11 ] = TABLE[i-1][ 2*j ][ 11 ] + TABLE[i-1][2*j+1][ 11 ]; 
			TABLE[ i ][ j ][ 11 ] = min( TABLE[i][j][11] , INF ); 
		}
		//printf("\n");
	}
}

int main()
{
	int ccN;
	scanf("%d", &ccN);
	for( int cc=0;cc<ccN;cc++ ) {
		scanf("%d", &P );
		N = 1 << P;
		for( int i=0;i<N;i++ ) {
			scanf("%d", &M[i] );
			M[ i ] = P - M[ i ];
		}
		for( int i=0;i<P;i++ ) {
			for( int j=0;j< 1<<(P-i-1);j++ )
				scanf("%d", &PR[i][j] );
		}
		DP();
		printf("Case #%d: %lld\n", cc+1, TABLE[P][ 0 ][ 0 ]);
	}
	return 0;
}
