#include <map>
#include <cmath>
#include <cstdio>
#include <utility>

using namespace std;

typedef pair < int, int > Pii;

const int p[] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000 };

int T, A, B, x, m;
map < Pii, bool > cache;

void solve () {
	
	scanf ( "%d%d", &A, &B );
	long long ans = 0;
	cache.clear ();
	
	for ( int n = A; n < B; ++ n ) {

		x = log10 ( n );
		if ( !x ) continue;
		
		for ( int i=0; i<x; ++i ) {
			
			if ( ( n / p[i] ) % 10 == 0 ) continue;
			m = ( n % p[i+1] ) * p[ x-i ] + n / p[i+1];
			
			if ( n < m && m <= B && cache[ Pii ( n, m ) ] == 0 ) {
				++ ans;
				cache[ Pii ( n, m ) ] = 1;
				}
			
			}
		}
	
	printf ( "%lld\n", ans );
}

int main (void) {
	
	scanf ( "%d", &T );
	for ( int t=1; t<=T; ++ t ) {
		printf ( "Case #%d: ", t );
		solve ();
		}
	
}
