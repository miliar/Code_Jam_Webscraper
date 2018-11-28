#include <cstdio>
#include <cmath>
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
		double ans = 0;
		bool ok[1005] = {false};
		int arr[1005], n;
		scanf( "%d", &n );
		FOR(i,1,n) scanf( "%d", &arr[i] );
		FOR(i,1,n) if ( !ok[i] ) {
			int cnt = 1, x = i;
			ok[i]   = true;
			while ( arr[x] != i ) {
				x     = arr[x];
				ok[x] = true;
				cnt++;
			}
			if ( cnt != 1 ) ans += cnt;
		}
		printf( "Case #%d: %.6lf\n", tcase, ans );
	}
	return 0;
}
