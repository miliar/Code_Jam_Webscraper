#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)

int t[105];

int main()
{
	int T;
	scanf( "%d", &T );
	FOR(tcase,1,T) {
		int n, s, p;
		scanf( "%d %d %d", &n, &s, &p );
		REP(i,n) scanf( "%d", &t[i] );
		sort(t,t+n); reverse(t,t+n);
		int ans = 0;
		REP(i,n) {
			if ( (t[i] + 2) / 3 >= p ) ans++;
			else if ( s > 0 && t[i] - p >= 0 && (t[i] - p) / 2 + 2 >= p ) ans++, s--;
		}
		printf( "Case #%d: %d\n", tcase, ans );
	}
	return 0;
}
