#include <cstdio>
#include <cstdlib>
#include <cstring>

const char fst[] = "welcome to code jam";

char st[ 505 ];
int n, dp[ 505 ][ 25 ];

int main( void ) {
	scanf( "%d\n", &n );
	for( int i = 0; i < n; ++i ) {
		memset( dp, 0, sizeof( dp ) ); 
		dp[ 0 ][ 0 ] = 1; gets( st );
		
		int len = strlen( fst );
		for( int j = 0; st[ j ] != 0; ++j )
			for( int k = 0; k <= len; ++k ) {
				if( st[ j ] == fst[ k ]  &&  k < len )
					dp[ j + 1 ][ k + 1 ] = ( dp[ j + 1 ][ k + 1 ] + dp[ j ][ k ] ) % 1000;
				dp[ j + 1 ][ k ] = ( dp[ j + 1 ][ k ] + dp[ j ][ k ] ) % 1000;
			}
		
		printf( "Case #%d: %04d\n", i + 1, dp[ strlen( st ) ][ len ] );
	}
	return( 0 );
}
