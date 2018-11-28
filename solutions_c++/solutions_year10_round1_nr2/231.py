#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
#include<cassert>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAXN 105
#define MAXV 270

int D,I,M,N;

int dp[MAXN][MAXV];
int INF = 1023456789;
int a[MAXN];

int main() {
	int i,j,T,kase=1,d,k,res,ni,dt;
	scanf("%d",&T);
	while(T--) {
		scanf("%d%d%d%d",&D,&I,&M,&N);
		rep(i,N) scanf(" %d",&a[i]);
		printf("Case #%d: ",kase++);
		rep(i,N) rep(j, 260) dp[i][j] = INF;
		dp[0][a[0]] = 0;
		dp[0][256] = D;
		rep(i,256) dp[0][i] = min(dp[0][i], abs(i - a[0]));

		for(i = 0; i < N - 1; i++) rep(j, 257) if(dp[i][j] < INF) {
			if(j == 256) { // no prev number
				dp[i+1][a[i+1]] = min(dp[i+1][a[i+1]], dp[i][j]);
				dp[i+1][256] = min(dp[i+1][256], dp[i][j] + D);
				rep(k,256) dp[i+1][k] = min(dp[i+1][k], dp[i][j] + abs(k - a[i+1]));
			}
			else {
				d = abs(a[i+1] - j);
				//do nothing
				if(d <= M) dp[i+1][a[i+1]] = min(dp[i+1][a[i+1]], dp[i][j]);

				//delete
				dp[i+1][j] = min(dp[i+1][j], dp[i][j] + D);

				//change
				rep(k,256) {
					if(abs(k-j) <= M) {
						dp[i+1][k] = min(dp[i+1][k], dp[i][j] + abs(k-a[i+1]));
					}
					else {
						dt = abs(k-j);
						if(M != 0) {
							ni = ( (dt + M - 1) / M) - 1;
							assert(ni >= 1);
							dp[i+1][k] = min(dp[i+1][k], dp[i][j] + abs(k-a[i+1]) + ni * I);
						}
					}
				}

				//insert
				if(d > M && M != 0) {
					ni = ((d + M - 1) / M) - 1;
					assert(ni >= 1);
					dp[i+1][a[i+1]] = min(dp[i+1][a[i+1]], dp[i][j] + ni * I);
				}
			}
		}

		res = INF;
		rep(j,257) res = min(res, dp[N-1][j]);
		printf("%d\n",res);
	}
	return 0;
}