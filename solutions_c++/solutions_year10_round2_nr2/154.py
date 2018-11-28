#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)


int main()
{
	int ncase;
	scanf( "%d", &ncase );
	FOR(tcase,1,ncase) {
		int n, k, b, t;
		int x[100], v[100];
		scanf( "%d %d %d %d", &n, &k, &b, &t );
		REP(i,n) scanf( "%d", &x[i] );
		REP(i,n) scanf( "%d", &v[i] );
		
		int ftf = -1;
		FORD(i,n-1,0) if ( b - x[i] > t * v[i] ) { ftf = i; break; }
		
		int ans = 0, arrive = 0;
		int cnt = 1;
		FORD(i,n-1,0) {
			if ( arrive == k ) break;
			if ( b - x[i] <= t * v[i] ) {
				if ( i < ftf ) ans += cnt;
				arrive++;
			}
			else if ( i < ftf ) cnt++;
		}

		printf( "Case #%d: ", tcase );
		if ( arrive == k ) printf( "%d\n", ans );
		else puts( "IMPOSSIBLE" );
	}
	return 0;
}
