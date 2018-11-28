#include<iostream>
#include<algorithm>
#include<cmath>
#include<cassert>
using namespace std;

#define INF 10010
#define N 10010
int M,V,iner;
int p[N],c[N];
int dp[N][2];
#define min(a,b) ((a)<(b)?(a):(b))

int main()
{	
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++){
		printf("Case #%d: ",ii);
		scanf("%d%d",&M,&V);
		iner=(M-1)/2;
		int i;
		for(i=1;i<=iner;i++)
			scanf("%d%d",&p[i],&c[i]);
		for(i=iner+1;i<=M;i++)
			scanf("%d",&p[i]);

		for(i=M;i>iner;i--){
			dp[i][p[i]]=0;
			dp[i][1-p[i]]=INF;
		}
		for(i=iner;i>=1;i--){
			if(p[i]==0){
				dp[i][0]=dp[i*2][0]+dp[i*2+1][0];
				dp[i][1]=min(dp[i*2][1],dp[i*2+1][1]);
			}else{
				dp[i][0]=min(dp[i*2][0],dp[i*2+1][0]);
				dp[i][1]=dp[i*2][1]+dp[i*2+1][1];
			}
			if(c[i]==1){
				int bak[2];
				if(p[i]==1){
					bak[0]=dp[i*2][0]+dp[i*2+1][0];
					bak[1]=min(dp[i*2][1],dp[i*2+1][1]);
				}else{
					bak[0]=min(dp[i*2][0],dp[i*2+1][0]);
					bak[1]=dp[i*2][1]+dp[i*2+1][1];
				}
				dp[i][0]=min(dp[i][0],bak[0]+1);
				dp[i][1]=min(dp[i][1],bak[1]+1);
			}
		}
		int re=dp[1][V];
		if(re>=INF) printf("IMPOSSIBLE\n");
		else printf("%d\n",re);
	}
	return 0;
}