#include <cstdio>
#include <algorithm>

using namespace std;

struct el {
	int a, b;
	
	inline bool operator< ( const el& t ) const {
		return a == t.a ? b < t.b : a < t.a;
		}
} m[1024];

int T, N;

int main (void) {
	
	scanf ( "%d", &T );
	
	for ( int t=1; t<=T; ++t ) {
		
		scanf ( "%d", &N );
		for ( int i=0; i<N; ++i ) scanf ( "%d%d", &m[i].a, &m[i].b );
		
		sort ( m, m+N );
		
		int ans = 0;
		for ( int i=0; i<N; ++i )
			for ( int j=0; j<i; ++j ) ans += ( m[i].b < m[j].b );
		
		printf ( "Case #%d: %d\n", t, ans );
		
		}
	
}
