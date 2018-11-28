#include<stdio.h>
#include<string.h>
#include<algorithm>
#define INF 1050000000
using namespace std;
int p;
int in[20][2024];
int m[2024];
int dp[2024][20];
int id[20][2024];
int dpf(int x,int y,int e){
	if(x!=-1&&dp[id[x][y]][e]!=-1)return dp[id[x][y]][e];
	if(x==-1){
	//	printf("y=%d m=%d e=%d\n",y,m[y],e);
		if(e>m[y])return INF;
		return 0;
	}
	dp[id[x][y]][e]=INF;
	dp[id[x][y]][e]<?=dpf(x-1,y*2,e)+dpf(x-1,y*2+1,e)+in[x][y];
	dp[id[x][y]][e]<?=dpf(x-1,y*2,e+1)+dpf(x-1,y*2+1,e+1);
	//if(e==0)	printf("dp %d %d %d=%d\n",x,y,e,dp[id[x][y]][e]);
	return dp[id[x][y]][e];
}
int main(){
	int t,cas=1,i,j;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&p);
		for(i=0;i<(1<<p);i++)scanf("%d",&m[i]);
		int ii=0;
		for(i=0;i<p;i++){
			for(j=0;j<(1<<(p-i-1));j++){
				scanf("%d",&in[i][j]);
				id[i][j]=ii++;
			}
		}
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n",cas++,dpf(p-1,0,0));
	}
}


