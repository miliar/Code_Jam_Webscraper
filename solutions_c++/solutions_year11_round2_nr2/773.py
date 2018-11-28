#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int T, C, cnt;
double a[1000005], b[1000005], D;

inline bool ok ( double x ) {
	
	b[0] -= x;
	for ( int i=1; i<cnt; ++i ) {
		
		double nx = b[i-1] + (double)D;
		if ( nx <= b[i]-x ) b[i] = max ( b[i]-x, nx );
		else if ( nx-b[i] <= x ) b[i] = nx;
		else return false;
		
		}
	
	return true;
	
}

void solve () {
	
	scanf ( "%d%lf", &C, &D );
	
	cnt = 0;
	int v, p;
	for ( int i=0; i<C; ++i ) {
		
		scanf ( "%d%d", &p, &v );
		while ( v -- ) a[ cnt++ ] = p;
		
		}
	
	double lo = 0., hi=1e17, mid;
	while ( abs ( lo-hi ) > 1e-7 ) {
		
//		printf ( "%.6lf %.6lf\n", lo, hi );
		
		mid = ( lo+hi ) / 2.;
		
		memcpy ( b, a, sizeof a );
		if ( ok ( mid ) ) hi = mid;
		else lo = mid;
		
		}
	
	printf ( "%lf\n", hi );
	
}

int main (void) {
	
	scanf ( "%d", &T );
	for ( int t=1; t<=T; ++t ) {
		printf ( "Case #%d: ", t );
		solve ();
		}
	
}
