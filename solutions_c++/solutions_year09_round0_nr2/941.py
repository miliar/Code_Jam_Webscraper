#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

int  map[200][200];
char ans[200][200];
int basin;

int flow(int i, int j) {
	int ret = 0, low = 10010;
	if ( map[i-1][j] < low ) ret = 1, low = map[i-1][j];
	if ( map[i][j-1] < low ) ret = 2, low = map[i][j-1];
	if ( map[i][j+1] < low ) ret = 3, low = map[i][j+1];
	if ( map[i+1][j] < low ) ret = 4, low = map[i+1][j];
	if ( map[i][j] <= low ) ret = 0;
	return ret;
}

char go(int i, int j) {
	if ( ans[i][j] == 0 )
		switch ( flow(i,j) ) {
			case 0: ans[i][j] = 'a' + basin++; break;
			case 1: ans[i][j] = go(i-1,j); break;
			case 2: ans[i][j] = go(i,j-1); break;
			case 3: ans[i][j] = go(i,j+1); break;
			case 4: ans[i][j] = go(i+1,j); break;
		}
	return ans[i][j];
}

int main()
{
	int T;
	scanf( "%d", &T );

	FOR(tcase,1,T) {
		int h, w;
		scanf( "%d %d", &h, &w );
		FOR(i,1,h) FOR(j,1,w) scanf( "%d", &map[i][j] );
		FOR(i,0,h+1) map[i][0] = map[i][w+1] = 10005;
		FOR(i,0,w+1) map[0][i] = map[h+1][i] = 10005;
		
		basin = 0;
		memset(ans,0,sizeof(ans));
		FOR(i,1,h) FOR(j,1,w) if ( ans[i][j] == 0 ) go(i,j);

		printf( "Case #%d:\n", tcase );
		FOR(i,1,h) FOR(j,1,w) printf( "%c%c", ans[i][j], j == w ? '\n' : ' ' );
	}

	return 0;
}
