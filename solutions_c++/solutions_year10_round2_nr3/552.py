#include <cstdio>
#include <cstdlib>

int t, n, niz[ 35 ] = { 0, 0 };

inline int jest( int mask, int j ) { return( ( mask >> j ) & 1 ); }

int spust( int x, int mask ) {
	for( int j = 2; j <= x; ++j )
		niz[ j ] = niz[ j-1 ] + jest( mask, j-2 );
	
	while( x > 1 && jest( mask, x-2 ) )
		x = niz[ x ];
	return( x );
}

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		scanf( "%d", &n );
		
		int rez = 0;
		for( int j = 0; j < ( 1 << ( n-1 ) ); ++j )
			rez += ( spust( n, j ) == 1 );
		
		printf( "Case #%d: %d\n", i+1, rez % 100003 );
	}
	return( 0 );
}
