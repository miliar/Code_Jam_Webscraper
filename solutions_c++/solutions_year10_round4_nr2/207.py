#include <stdio.h>
#include <algorithm>
using namespace std;

#define INF 1010101010

int dp[4000][20];

main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		int p;
		scanf("%d",&p);
		int m[4000];
		int c[4000];
		int s=0;
		for(int i=(1<<p)-1;i>=0;i--){scanf("%d",&m[i]);}
		for(int i=(1<<p)-1;i>0;i--){scanf("%d",&c[i]);s+=c[i];}
		for(int i=(1<<p)-1;i>=1;i--){
			for(int j=0;j<=p;j++){
				if(i>=(1<<(p-1))){
					int ii=i-(1<<(p-1));
					int lim=min(m[2*ii],m[2*ii+1]);
					if(j>lim)dp[i][j]=-INF;
					else if(j==lim)dp[i][j]=0;
					else dp[i][j]=c[i];
				}else{
					int jj=min(j+1,p);
					int il=i*2,ir=i*2+1;
					dp[i][j]=max(-INF,max(c[i]+dp[il][jj]+dp[ir][jj],dp[il][j]+dp[ir][j]));
				}
				//printf("%d %d: %d\n",i,j,dp[i][j]);
			}
		}
		int ans=s-dp[1][0];
		printf("Case #%d: %d\n",t,ans);
	}
}