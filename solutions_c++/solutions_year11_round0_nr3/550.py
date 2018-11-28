#include <stdio.h>

int main ( void ) {
	//freopen ( "C-large.in", "r", stdin );
	//freopen ( "C-large.out", "w", stdout );
	int cas, n, m, s, t, p;
	scanf ( "%d", &cas );
	for ( int o = 0 ; o < cas ; ++o ) {
		scanf ( "%d", &n );
		p = s = 0; t = 10000000;
		for ( int i = 0 ; i < n ; ++i ) {
			scanf ( "%d", &m );
			if ( t > m ) t = m;
			s += m;
			p ^= m;
		}
		if ( p ) printf ( "Case #%d: NO\n", o + 1 );
		else printf ( "Case #%d: %d\n", o + 1, s - t );
	}
	return 0;
}

