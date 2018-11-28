#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

typedef long long LL;
const LL mod = 100003;

LL nck[1005][1005];
LL  dp[1005][1005];

LL f(int n, int x) {
	if ( dp[n][x] != -1 ) return dp[n][x];
	if ( x == 1 ) return 1;
	LL&ret = dp[n][x] = 0;
	FORD(i,x-1,1) ret = (ret + f(x,i) * nck[n-x-1][x-i-1]) % mod;
	return ret;
}

int main()
{
	nck[0][0] = 1;
	FOR(i,1,1000) {
		nck[i][0] = nck[i][i] = 1;
		FOR(j,1,i-1) nck[i][j] = (nck[i-1][j] + nck[i-1][j-1]) % mod;
	}
	memset(dp,-1,sizeof(dp));

	int ncase;
	scanf( "%d", &ncase );
	FOR(tcase,1,ncase) {
		int n;
		LL ans = 0;
		scanf( "%d", &n );
		FORD(i,n-1,1) ans = (ans + f(n,i)) % mod;
		printf( "Case #%d: %I64d\n", tcase, ans );
	}
	return 0;
}
