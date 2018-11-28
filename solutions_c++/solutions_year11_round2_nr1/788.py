#include <cstdio>
#include <cstring>

int T, N;
char G[128][128];
double wp[128], wp1[128][128], owp[128], oowp[128];

void solve () {
	
	double ans[128];
	memset ( ans, 0, sizeof ans );
	memset ( wp, 0, sizeof wp );
	memset ( wp1, 0, sizeof wp1 );
	memset ( owp, 0, sizeof owp );
	memset ( oowp, 0, sizeof oowp );
	
	scanf ( "%d", &N );
	for ( int i=0; i<N; ++i ) scanf ( "%s", G[i] );
	
	for ( int i=0; i<N; ++i ) {
		
		int w = 0, all = 0;
		for ( int j=0; j<N; ++j ) {
			all += ( G[i][j] != '.' );
			w += ( G[i][j] == '1' );
			}
		
		wp[i] = (double)w / all;
		
		for ( int j=0; j<N; ++j ) if ( G[i][j] != '.' ) {
			wp1[i][j] = double(w-( G[i][j] == '1' )) / (all-1);
			}
		
		}
	
	
	for ( int i=0; i<N; ++i ) {
		
		int opp = 0;
		for ( int j=0; j<N; ++j ) {
			
			if ( G[i][j] == '.' ) continue;

			++ opp;
			owp[i] += wp1[j][i];
			
			}
		
		owp[i] /= (double)opp;
		}
	
	for ( int i=0; i<N; ++i ) {
		
		int opp = 0;
		for ( int j=0; j<N; ++j ) {
			
			if ( G[i][j] == '.' ) continue;
			
			++opp;
			oowp[i] += owp[j];
			
			}
		
		oowp[i] /= (double)opp;
		}
	
	for ( int i=0; i<N; ++i ) printf ( "%lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] );
	
}

int main (void) {
	
	scanf ( "%d", &T );
	
	for ( int t=1; t<=T; ++t ) {
		
		printf ( "Case #%d:\n", t );
		solve ();
		
		}
	
}
