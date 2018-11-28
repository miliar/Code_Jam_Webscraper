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

		char s[100];
		scanf( "%s", s );
		
		int n = strlen(s);

		int p[100], t = 0;
		int c[256];
		memset(c,-1,sizeof(c));
		c[s[0]] = 1; p[0] = 1;
		FOR(i,1,n-1) {
			if ( c[s[i]] == -1 ) {
				c[s[i]] = t++;
				if ( t == 1 ) t++;
			}
			p[i] = c[s[i]];
		}
		
		if ( t == 0 ) t = 2;

		long long ans = 0;
		REP(i,n) ans = ans * t + p[i];

		printf( "Case #%d: %I64d\n", tcase, ans );
	}

	return 0;
}
