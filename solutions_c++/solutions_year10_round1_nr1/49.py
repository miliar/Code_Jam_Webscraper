#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

char TABLE[100][100];
int N, K;

int check( int x, int y )
{
		int i;
		char c = TABLE[ x ][ y ];
		for( i=0;i<K;i++ ) {
				if( x + i < N && TABLE[ x + i ][ y ] == c )
						continue;
				break;
		}
		if( i == K ) return 1;
		for( i=0;i<K;i++ ) {
				if( y + i < N && TABLE[ x ][ y+i ] == c )
						continue;
				break;
		}
		if( i == K ) return 1;
		for( i=0;i<K;i++ ) {
				if( y + i < N && x + i < N && TABLE[ x+i ][ y+i ] == c )
						continue;
				break;
		}
		if( i == K ) return 1;
		for( i=0;i<K;i++ ) {
				if( y + i < N && x - i >= 0 && TABLE[ x-i ][ y+i ] == c )
						continue;
				break;
		}
		if( i == K ) return 3;
		return 0;
}

int main()
{
		int ccN;
		scanf("%d", &ccN);
		for( int cc=0;cc<ccN;cc++ ) {
				scanf("%d%d", &N, &K);
				for( int y=0;y<N;y++ ) {
						for( int x=0;x<N;x++ ) {
								scanf(" %c ", &TABLE[N-y-1][x] );
						}
				}
				for( int x=0;x<N;x++ ) {
						int moveto = N-1;
						for( int y=N-1;y>=0;y-- ) {
								if( TABLE[ x ][ y ]== '.' ) {
										continue;
								}
								TABLE[ x ][ moveto ] = TABLE[ x ][ y ];
								if( y != moveto )
										TABLE[ x ][ y ] = '.';
								moveto--;
						}
				}
				int R, B;
				R = B = 0;
				for( int y=0;y<N;y++ ) {
						for( int x=0;x<N;x++ ) {
								if( TABLE[x][y] != '.' && check( x, y ) ) {
									if( TABLE[x][y] == 'R' )
											R = 1;
									else
											B = 1;
								}
						}
				}
				printf("Case #%d: ", cc + 1);
				if( R && B ) 
						printf("Both\n");
				else if( R )
						printf("Red\n");
				else if( B )
						printf("Blue\n");
				else
						printf("Neither\n");
			/*
				for( int y=0;y<N;y++ ) {
						for( int x=0;x<N;x++ ) {
								printf("%c", TABLE[x][y] );
						}
						printf("\n");
				}
				*/
		}
		return 0;
}
