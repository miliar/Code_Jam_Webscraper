#include <cstdio>

int main() {
	int cas , t = 0 ;
	scanf( "%d" , &cas );
	while ( cas-- ) {
		int n , ans = 0;
		scanf( "%d" , &n );
		for ( int i = 1; i <= n; i++ ) {
			int x;
			scanf( "%d" , &x );
			ans += (x!=i);
		}
		printf( "Case #%d: %d.000000\n" , ++t , ans );
	}
	return 0;
}
