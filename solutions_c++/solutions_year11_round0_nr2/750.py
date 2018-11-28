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
	int T;
	scanf( "%d", &T );
	FOR(tcase,1,T) {
		char comb[256][256]; memset(comb,-1,sizeof(comb));
		bool opps[256][256] = {false};
		char invoke[105];
		
		int c, d, n;
		char s[10];
		scanf( "%d", &c );
		REP(_,c) {
			scanf( "%s", s );
			comb[s[0]][s[1]] = s[2];
			comb[s[1]][s[0]] = s[2];
		}
		scanf( "%d", &d );
		REP(_,d) {
			scanf( "%s", s );
			opps[s[0]][s[1]] = true;
			opps[s[1]][s[0]] = true;
		}
		scanf( "%d", &n );
		scanf( "%s", invoke );

		char out[200] = {0};
		int  p = 0;
		REP(i,n) {
			if ( p == 0 ) out[p++] = invoke[i];
			else {
				if ( comb[out[p-1]][invoke[i]] != -1 )
					out[p-1] = comb[out[p-1]][invoke[i]];
				else {
					bool clear = false;
					REP(j,p) if ( opps[out[j]][invoke[i]] ) clear = true;
					if ( clear ) p = 0; else out[p++] = invoke[i];
				}
			}
		}
		
		printf( "Case #%d: [", tcase );
		if ( p != 0 ) {
			printf( "%c", out[0] );
			FOR(i,1,p-1) printf( ", %c", out[i] );
		}
		printf( "]\n" );
	}
	return 0;
}
