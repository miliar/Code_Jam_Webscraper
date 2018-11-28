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

int dp[2][(1<<20)+1];
int a[(1<<20)];

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,kase=1;
	int i,j,x,y,n,t,res,sum;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %d",&n);
		t = 0;
		sum = 0;
		rep(i,n) {
			scanf(" %d",&a[i]);
			t ^= a[i];
			sum += a[i];
		}
		memset(dp,-1,sizeof(dp));
		x = 0, y = 1;
		dp[x][0] = 0;
		rep(i,n) {
			//rep(j,(1<<20)) dp[y][j] = -1;
			memset(dp[y],-1,sizeof(dp[y]));
			rep(j,(1<<20)) if(dp[x][j] != -1) {
				dp[y][j] = max(dp[y][j], dp[x][j]);
				dp[y][j^a[i]] = max(dp[y][j^a[i]], dp[x][j] + a[i]);
			}
			swap(x,y);
		}

		res = -1;
		rep(i,(1<<20)) if(dp[x][i] > 0) {
			if(i == (t^i) && dp[x][i] < sum) res = max(res, dp[x][i]);
		}
		if(res == -1) printf("NO\n"); else printf("%d\n",res);

	}
	return 0;
}