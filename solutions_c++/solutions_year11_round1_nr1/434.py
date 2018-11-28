#include <stdio.h>

int main ( void ) {
	//freopen ( "in.txt", "r", stdin );
	freopen ( "A-large.in", "r", stdin );
	freopen ( "A-large.out", "w", stdout );
	__int64 n;
	int pd, pg, cas, i;
	scanf ( "%d", &cas );
	for ( int t = 1 ; t <= cas ; ++t ) {
		scanf ( "%I64d%d%d", &n, &pd, &pg );
		for ( i = 1 ; i <= 100 && i <= n ; ++i) {
			if ( pd * i % 100 == 0 ) break;
		}
		if ( i == n + 1 || i == 101 ) {
			printf ( "Case #%d: Broken\n", t );
		} else {
			if ( pg == 100 ) {
				if ( pd == 100 ) {
					printf ( "Case #%d: Possible\n", t );
				} else {
					printf ( "Case #%d: Broken\n", t );
				}
			} else if ( pg == 0 ) {
				if ( pd == 0 ) {
					printf ( "Case #%d: Possible\n", t );
				} else {
					printf ( "Case #%d: Broken\n", t );
				}
			} else printf ( "Case #%d: Possible\n", t );
		}
	}
	return 0;
}
