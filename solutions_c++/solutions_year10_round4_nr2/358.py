#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAX 105
#define i64 __int64
#define MAXP 10

int M[(1<<MAXP)], D[(1<<MAXP)];
i64 C[MAXP][(1<<(MAXP-1))];
int P;

i64 dp[MAXP][(1<<(MAXP-1))][MAXP];
i64 INF = 10234567;

i64 go(int level, int node, int taken) {
	if(dp[level][node][taken] != -1) return dp[level][node][taken];
	if(level == 0) {
		if(D[node*2] <= taken && D[node*2+1] <= taken) return 0; //return dp[level][node][taken] = 0;
		if(D[node*2] <= taken + 1 && D[node*2+1] <= taken + 1) return C[level][node];//return dp[level][node][taken] = C[level][node];
		//return dp[level][node][taken] = INF;
		return INF;
	}

	i64 &ret = dp[level][node][taken];
	i64 r1,r2;

	r1 = go(level-1, node*2, taken);
	r1 += go(level-1, node*2+1, taken);

	r2 = go(level-1, node*2, taken+1);
	r2 += go(level-1, node*2+1, taken+1) + C[level][node];

	ret = min(r1, r2);
	return ret;

}

int main() {
	int i,j,k;
	int T,kase=1;
	i64 ret;
	scanf("%d",&T);
	INF *= INF;
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf("%d",&P);
		rep(i,(1<<P)) {
			scanf(" %d",&M[i]);
			D[i] = P - M[i];
		}
		rep(i,P) rep(j,(1<<(P-i-1))) scanf(" %I64d",&C[i][j]);
		rep(i,P) rep(j,(1<<(P-1))) rep(k,P) dp[i][j][k] = -1;
		ret = go(P-1,0,0);
		printf("%I64d\n",ret);
	}
	return 0;
}