#include <stdio.h>
#include <math.h>

#define N 200
#define abs( c ) ( ( c ) < 0 ? -(c) : (c) )

int op[ N ][ 2 ];

int main ( void ) {
	//freopen ( "A-large.in", "r", stdin );
	//freopen ( "A-large.out", "w", stdout );
	int cas, n;
	scanf ( "%d", &cas );
	for ( int t = 0 ; t < cas ; ++t ) {
		scanf ( "%d", &n );
		for ( int i = 0 ; i < n ; ++i ) {
			char c = getchar ();
			scanf ( "%c%d", &c, &op[ i ][ 1 ] );
			op[ i ][ 0 ] = c;
		}
		int O = 1, B = 1, mo = 0, mb = 0, ans = 0;
		for ( int i = 0 ; i < n ; ++i ) {
			if ( op[ i ][ 0 ] == 'O' ) {
				int tmp = abs ( O - op[ i ][ 1 ] );
				if ( tmp < mo ) tmp = 0;
				else tmp -= mo;
				mo = 0; mb += tmp + 1; ans += tmp + 1;
				O = op[ i ][ 1 ];
			} else {
				int tmp = abs ( B - op[ i ][ 1 ] );
				if ( tmp < mb ) tmp = 0;
				else tmp -= mb;
				mb = 0; mo += tmp + 1; ans += tmp + 1;
				B = op[ i ][ 1 ];
			}
		}
		printf ( "Case #%d: %d\n", t + 1, ans );
	}
	return 0;
}

