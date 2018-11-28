#include <cstdio>
#include <numeric>
#include <algorithm>

using namespace std;

int T;

void solve ( int t ) {
	
	printf ( "Case #%d: ", t );
	
	int N, ar[1024];
	scanf ( "%d", &N );
	
	int Xor = 0;
	for ( int i=0; i<N; ++i ) {
		scanf ( "%d", ar+i );
		Xor ^= ar[i];
		}
	
	if ( Xor ) printf ( "NO\n" );
	else printf ( "%d\n", accumulate ( ar, ar+N, 0 ) - *min_element ( ar, ar+N ) );
	
}

int main (void) {
	
	scanf ( "%d", &T );
	for ( int i=1; i<=T; ++i ) solve ( i );
	
}
