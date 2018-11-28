#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
using namespace std;
#define max(x,y) (((x)>(y))?(x):(y))
#define min(x,y) (((x)<(y))?(x):(y))
#define INF (1<<29)
#define eps (1e-8)
#define feq(x,y) (fabs(x-y)<eps)
#define flt(x,y) (((y)-(x))>eps)
#define fgt(x,y) (((x)-(y))>eps)
#define ll long long

int n,tar;
int dp[10005],d[10005],l[10005];

int main(){
	int T; scanf("%d",&T);
	for (int t=1;t<=T;++t){
		memset(dp,-1,sizeof(dp));

		scanf("%d",&n);
		for (int i=0;i<n;++i) scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&tar);
		
		dp[0]=d[0];
		for (int i=1;i<n;++i){
			for (int j=i-1;j>=0;--j){
				if (dp[j]==-1) continue;

				if (d[j]+dp[j]>=d[i]){
					dp[i]=min(l[i],d[i]-d[j]);
				}
			}
		}



		bool ans=0;
		for (int i=0;i<n;++i){
			if (dp[i]==-1) continue;
			if (d[i]+dp[i]>=tar) ans=1;
		}
		if (ans) printf("Case #%d: YES\n",t); else printf("Case #%d: NO\n",t);
	}
	return 0;
}
