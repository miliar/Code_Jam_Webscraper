#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

char t[] = "welcome to code jam";
char s[505];
int  nt, ns;
int  memo[505][25];

int dp(int a, int b) {
	if ( b == nt ) return 1;
	if ( memo[a][b] != -1 ) return memo[a][b];
	int &ret = memo[a][b] = 0;
	
	FOR(i,a,ns) if ( t[b] == s[i] ) {
		ret += dp(i,b+1);
		ret %= 10000;
	}
	
	ret %= 10000;

	return ret;
}

int main()
{
	int T;
	scanf( "%d\n", &T );

	FOR(tcase,1,T) {
		
		gets(s);
		ns = strlen(s);
		nt = strlen(t);
		memset(memo,-1,sizeof(memo));
		int ans = dp(0,0);

		printf( "Case #%d: %04d\n", tcase, ans % 10000 );
	}

	return 0;
}
