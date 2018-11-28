#include <cstdio>
#include <cstdlib>

int t, n, niz[ 45 ], zamjena;
char buff[ 45 ];

void zamjeni( int x, int y ) {
	int t = niz[ x ]; niz[ x ] = niz[ y ]; niz[ y ] = t;
	++zamjena;
}

int main( void ) {
	scanf( "%d", &t );
	for( int i = 0; i < t; ++i ) {
		scanf( "%d", &n );
		for( int j = 0; j < n; ++j ) {
			scanf( "%s", buff );
			
			niz[ j ] = 0;
			for( int k = 0; k < n; ++k )
				if( buff[ k ] == '1' )
					niz[ j ] = k;
		}
		
		zamjena = 0;
		for( int j = 0; j < n; ++j ) {
			int ind = -1;
			for( int k = j; k < n; ++k )
				if( niz[ k ] <= j )
					{ ind = k; break; }
			
			for( ; ind > j; --ind ) zamjeni( ind, ind - 1 );
		}
		
		printf( "Case #%d: %d\n", i + 1, zamjena );
	}
	
	return( 0 );
}
