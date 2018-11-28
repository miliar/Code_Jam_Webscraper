#include <cstdio>

int T, N, k, g[2048], R, next[2048], add[2048];

int main (void) {
	
	scanf ( "%d", &T );
	
	for ( int i=1; i<=T; ++i ) {
		
		scanf ( "%d%d%d", &R, &k, &N );
		for ( int j=0; j<N; ++j ) {
			scanf ( "%d", g+j );
			g[N+j] = g[j];
			}
		
		
		long long ans = 0, t;
		
		for ( int p, j=0; j<N; ++j ) {
			
			t = 0;
			
			p = j;
			while ( 1 ) {
				
				if ( p == N+j ) {
					next[j] = j; add[j] = t;
					break;
					}
					
				t += g[p];
				
				if ( t > k ) {	
					next[j] = p%N;
					add[j] = t - g[p];
					break;
					}
				
				++ p;
				
				}
				
//			printf ( "j=%d next=%d add=%d\n", j, next[j], add[j] );			
			
			}
		
		int p = 0;
		while ( R -- ) {
			
			ans += add[p];
//			printf ( "%d %d\n", p, add[p] );
			p = next[p];
			
			}
		
		printf ( "Case #%d: %lld\n", i, ans );
		
		
		}
	
}
