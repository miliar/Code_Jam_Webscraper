#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)


int main()
{
	int T;
	scanf( "%d", &T );
	FOR(tcase,1,T) {
		int  n;
		char arr[105][105];
		scanf( "%d", &n );
		REP(i,n) scanf( "%s", arr[i] );

		int np[105] = {0};
		REP(i,n) REP(j,n) if ( arr[i][j] != '.' ) np[i]++;

		double wp[105], owp[105], oowp[105];
		REP(i,n) {
			int win = 0, play = 0;
			REP(j,n) if ( arr[i][j] == '1' ) win++;
			wp[i] = (double)win/np[i];
		}
		REP(i,n) {
			double xwp[105]; REP(j,n) xwp[j] = 0;
			REP(j,n) if ( j != i ) {
				int win = 0, play = 0;
				REP(k,n) if ( k != i ) {
					if ( arr[j][k] == '1' ) win++;
					if ( arr[j][k] != '.' ) play++;
				}
				xwp[j] = (double)win/play;
			}
			owp[i] = 0;
			REP(j,n) if ( arr[i][j] != '.' ) owp[i] += xwp[j];
			owp[i] /= np[i];
		}
		REP(i,n) {
			oowp[i] = 0;
			REP(j,n) if ( arr[i][j] != '.' ) oowp[i] += owp[j];
			oowp[i] /= np[i];
		}
		
		printf( "Case #%d:\n", tcase );
		REP(i,n) printf( "%.8lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] );
		fprintf( stderr, "Case #%d:\n", tcase );
		REP(i,n) fprintf( stderr, "%.8lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] );

	}
	return 0;
}
