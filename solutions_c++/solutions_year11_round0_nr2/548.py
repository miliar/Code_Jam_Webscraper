#include <stdio.h>
#include <string.h>

#define N 310

char base[ N ][ 4 ];
char remo[ N ][ 3 ];

char str[ N ];

char ans[ N ];
int main ( void ) {
	//freopen ( "B-large.in", "r", stdin );
	//freopen ( "B-large.out", "w", stdout );
	int cas, c, d, n, top;
	scanf ( "%d", &cas );
	for ( int t = 0 ; t < cas ; ++t ) {
		scanf ( "%d", &c );
		for ( int i = 0 ; i < c ; ++i ) {
			scanf ( "%s", base[ i ] );
		}
		scanf ( "%d", &d );
		for ( int i = 0 ; i < d ; ++i ) {
			scanf ( "%s", remo[ i ] );
		}
		scanf ( "%d", &n );
		scanf ( "%s", str );
		top = -1;
		for ( int i = 0, j ; i < n ; ++i ) {
			ans[ ++top ] = str[ i ];
			if ( top == 0 ) continue;
			for ( j = 0 ; j < c ; ++j ) {
				if ( ( ans[ top ] == base[ j ][ 0 ] && ans[ top - 1 ] == base[ j ][ 1 ] ) ||
					( ans[ top ] == base[ j ][ 1 ] && ans[ top - 1 ] == base[ j ][ 0 ] ) ) {
						ans[ --top ] = base[ j ][ 2 ];
						break;
				}
			}
			if ( j != c ) continue;
			for ( j = 0 ; j < d ; ++j ) {
				for ( int k = 0 ; k < top ; ++k ) {
					if ( ( ans[ k ] == remo[ j ][ 0 ] && ans[ top ] == remo[ j ][ 1 ] ) ||
						( ans[ k ] == remo[ j ][ 1 ] && ans[ top ] == remo[ j ][ 0 ] ) ) {
							top = -1;
							j = d - 1; break;
					}
				}
			}
		}
		printf ( "Case #%d: [", t + 1 );
		for ( int i = 0 ; i <= top ; ++i ) {
			if ( i == 0 ) printf ( "%c", ans[ i ] );
			else printf ( ", %c", ans[ i ] );
		}
		printf ( "]\n" );
	}
	return 0;
}

