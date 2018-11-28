#include <cstdio>
#include <cstring>

#define LEN 10008

using namespace std;

int d[LEN], l[LEN];
int h[LEN];

int main ( ) {
	int i, j;
	int T, c, N, D, diff;
	double max;

	for ( scanf ( "%d", &T ), c = 1; c <= T; ++c ) {
		for ( scanf ( "%d", &N ), i = 0; i < N; ++i ) scanf ( "%d%d", &d[i], &l[i] ), h[i] = 0;
		scanf ( "%d", &D );
		h[0] = d[0];
		d[N] = l[N] = D; h[N] = 0;
		for ( i = 0; i < N; ++i ) {
			for ( j = i + 1; j <= N && d[j] - d[i] <= h[i]; ++j ) {
				diff = d[j] - d[i];
				max = diff;
				if ( max > l[j] ) max = l[j];
				if ( h[j] < max ) h[j] = max;
			}
		}
		printf ( "Case #%d: %s\n", c, h[N] ? "YES" : "NO" );
	}

	return 0;
}
