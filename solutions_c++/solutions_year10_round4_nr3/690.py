#include <cstdio>
#include <cstring>
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
		int n = 100;
		int r, arr[105][105] = {0};
		scanf( "%d", &r );
		REP(_,r) {
			int x1, x2, y1, y2;
			scanf( "%d %d %d %d", &x1, &y1, &x2, &y2 );
			FOR(i,y1,y2) FOR(j,x1,x2) arr[i][j] = 1;
		}

		int ans = 0;
		while ( true ) {
			int sum = 0;
			FOR(i,1,n) FOR(j,1,n) sum += arr[i][j];
			if ( sum == 0 ) break;
			ans++;
			int tmp[105][105];
			FOR(i,1,n) FOR(j,1,n) {
				if ( arr[i][j] == 1 ) tmp[i][j] = arr[i-1][j] | arr[i][j-1];
				if ( arr[i][j] == 0 ) tmp[i][j] = arr[i-1][j] && arr[i][j-1];
			}
			memcpy(arr,tmp,sizeof(arr));
		}
		printf( "Case #%d: %d\n", tcase, ans );
	}
	return 0;
}
