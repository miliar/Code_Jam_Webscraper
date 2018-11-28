#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int n,inp[10010][2];
int dp[10010];
int cas;
inline int Min(int a, int b){
	return a<b?a:b;
}
int main(){
	scanf("%d",&cas);
	for(int iii=0;iii<cas;iii++){
		scanf("%d",&n);
		inp[0][0]=0;
		for(int i=1;i<=n;i++)scanf("%d%d",&inp[i][0], &inp[i][1]);
		scanf("%d", &inp[n+1][0]);
		
		memset(dp, -1, sizeof(dp));
		dp[0]=inp[1][0]-inp[0][0];
		for(int i=0;i<=n;i++){
			if(dp[i]==-1)continue;
			for(int j=i+1;j<=n+1;j++){
				if(inp[j][0]>inp[i][0]+dp[i])break;
				int len = Min(inp[j][0]-inp[i][0], inp[j][1]);
				if(dp[j]<len)dp[j]=len;
			}		
		}
		
		if(dp[n+1]>-1)printf("Case #%d: YES\n", iii+1);
		else printf("Case #%d: NO\n", iii+1);
		
	}
	return 0;	
}
	
	
	
