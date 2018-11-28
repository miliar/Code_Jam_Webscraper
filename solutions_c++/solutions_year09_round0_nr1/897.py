#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

char word[5005][20];
bool patt[20][256];
char s[1000];

int main()
{
	int L, D, N;
	scanf( "%d %d %d", &L, &D, &N );

	REP(i,D) scanf( "%s", word[i] );

	FOR(tcase,1,N) {
		memset(patt,0,sizeof(patt));

		scanf( "%s", s );
		int x = 0;
		REP(i,strlen(s)) {
			if ( s[i] == '(' )
				while ( s[++i] != ')' )
					patt[x][s[i]] = true;
			else
				patt[x][s[i]] = true;
			x++;
		}
		
		int ans = 0;
		REP(i,D) {
			bool yes = true;
			REP(j,L) if ( !patt[j][word[i][j]] ) yes = false;
			if ( yes ) ans++;
		}

		printf( "Case #%d: %d\n", tcase, ans );
	}

	return 0;
}
