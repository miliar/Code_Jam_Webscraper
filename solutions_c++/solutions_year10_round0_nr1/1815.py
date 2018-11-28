#include <cstdio>
#include <cstdlib>

int n, k, t;

int main( void ) {
	scanf( "%d", &t );
	for( int i = 1; i <= t; ++i ) {
		scanf( "%d %d", &n, &k ); ++k;
		printf( "Case #%d: %s\n", i, ( ( k & -k ) % ( 1 << n ) == 0 ? "ON" : "OFF" ) );
	}
	return( 0 );
}
