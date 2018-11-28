#include<iostream>
using namespace std;

int dp[10010][3];
int gate[10010];
int change[10010];
int nilai[10010];
int tc,x,m,v,k,i,j;

int main() {
	scanf("%d",&tc);
	for(x=1;x<=tc;x++) {
		scanf("%d %d",&m,&v);
		memset(gate,0,sizeof(gate));
		memset(change,0,sizeof(change));
		memset(nilai,0,sizeof(nilai));
		for(i=1;i<=(m-1)/2;i++) scanf("%d %d",&gate[i],&change[i]);
		for(i=1+(m-1)/2;i<=m;i++) scanf("%d",&nilai[i]);
		for(i=1;i<=m;i++) {
			for(j=0;j<=1;j++) dp[i][j]=1000000000;
		}
		for(i=m;i>=1;i--) {
			if(i>(m-1)/2) dp[i][nilai[i]]=0;
			else {
				if(gate[i]==0) {
					for(j=0;j<2;j++) {
						for(k=0;k<2;k++) {
							dp[i][j|k]=min(dp[i][j|k],dp[i*2][j]+dp[i*2+1][k]);
						}
					}
				}
				else {
					for(j=0;j<2;j++) {
						for(k=0;k<2;k++) {
							dp[i][j&k]=min(dp[i][j&k],dp[i*2][j]+dp[i*2+1][k]);
						}
					}
				}
				if(change[i]==1) {
					if(gate[i]==1) {
						for(j=0;j<2;j++) {
							for(k=0;k<2;k++) {
								dp[i][j|k]=min(dp[i][j|k],1+dp[i*2][j]+dp[i*2+1][k]);
							}
						}
					}
					else {
						for(j=0;j<2;j++) {
							for(k=0;k<2;k++) {
								dp[i][j&k]=min(dp[i][j&k],1+dp[i*2][j]+dp[i*2+1][k]);
							}
						}
					}
				}
			}
		}
		printf("Case #%d: ",x);
		if(dp[1][v]>=1000000000) printf("IMPOSSIBLE\n");
		else printf("%d\n",dp[1][v]);
	}
}

					
					
				
