#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
using namespace std;

bool oppose[ 333 ][ 333 ];
int combine[ 333 ][ 333 ];
int stack[ 333 ] , cstack;

int main(){

	int t;
	scanf( "%d" ,&t );

	for( int tt = 0 ; tt < t ; tt++ ){
		memset( oppose , 0 , sizeof oppose );
		memset( combine , -1 , sizeof combine );
		
		int C;
		scanf( "%d" ,&C );
		for( int q = 0 ; q < C ; q++ ){
			char inp[ 5 ];
			scanf( "%s" ,inp );
			combine[ inp[ 0 ] ][ inp[ 1 ] ] = combine[ inp[ 1 ] ][ inp[ 0 ] ] = inp[ 2 ];
		}
		
		int O;
		scanf( "%d" ,&O );
		for( int q = 0 ; q < O ; q++ ){
			char inp[ 5 ];
			scanf( "%s" ,inp );
			oppose[ inp[ 0 ] ][ inp[ 1 ] ] = oppose[ inp[ 1 ] ][ inp[ 0 ] ] = 1;
		}
		
		int nothing;
		scanf( "%d" ,&nothing );
		
		char inp[ nothing + 2 ];
		
		scanf( "%s" ,inp );
		
		cstack = 0;
		
		for( int q = 0 ; q < nothing ; q++ ){
			char cur = inp[ q ];
			if( cstack > 0 ){
				if( combine[ cur ][ stack[ cstack - 1 ] ] != -1 ){
					stack[ cstack - 1 ] = combine[ cur ][ stack[ cstack - 1 ] ];
					continue;
				}
			}
			bool clear = 0;
			for( int w = 0 ; w < cstack ; w++ ){
				if( oppose[ cur ][ stack[ w ] ] ){
					clear = 1;
				}
			}
			
			if( clear ){
				cstack = 0;
				continue;
			}
			stack[ cstack ++ ] = cur;
		}
		
		printf( "Case #%d: [" ,tt + 1 );
		
		for( int q = 0 ; q < cstack ; q++ ){
			if( q != 0 ){
				printf( " " );
			}
			printf( "%c" ,stack[ q ] );
			if( q < cstack - 1 ){
				printf( "," );
			}		
		}
		
		printf( "]\n" );
	}
	return 0;
}
