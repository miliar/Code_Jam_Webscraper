#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for (int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for (int i=(a),_b=(b); i>=_b; i--)
#define REP(i,n) for (int i=0,_n=(n); i<_n; i++)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

int nTC,dp[101][101],r[11],c[11],H,W,R,mod = 10007;

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		printf("Case #%d: ",TC);
		scanf("%d %d %d",&H,&W,&R);
		REP(i,R) scanf("%d %d",&r[i],&c[i]);

		REP(i,H) REP(j,W){
			if (i==0 && j==0){
				dp[i][j] = 1;
				continue;
			}

			dp[i][j] = 0;
			REP(k,R) if (r[k]-1==i && c[k]-1==j) goto next;
			if (i>=1 && j>=2) dp[i][j] += dp[i-1][j-2];
			if (i>=2 && j>=1) dp[i][j] += dp[i-2][j-1];
			dp[i][j] %= mod;
			next:;
		}
		printf("%d\n",dp[H-1][W-1]);
	}
}
