#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define INF 1000000
#define min(a,b) (((a)<(b))?(a):(b))

char se[105][105];
char qu[1005][105];
int dp[1005][105];
char ok[1005][105];

int main() {
	int T,i,n,q,kase=1,j,k,res;
	char s[1005];
	gets(s);
	sscanf(s,"%d",&T);
	while(T--) {
		gets(s); sscanf(s,"%d",&n);// strcpy(se[0],"*");
		for(i=1;i<=n;i++) gets(se[i]);
		gets(s); sscanf(s,"%d",&q);
		for(i=1;i<=q;i++) gets(qu[i]);
		if(q == 0) {
			printf("Case #%d: 0\n",kase++);
			continue;
		}
		res = INF;
		memset(ok,0,sizeof(ok));
		for(i=1;i<=q;i++) for(j=1;j<=n;j++) if(strcmp(qu[i],se[j])!=0 ) ok[i][j] = 1;
		
		for(i=0;i<=q;i++) for(j=0;j<=n;j++) dp[i][j] = INF;
		for(i=1;i<=n;i++) dp[0][i] = 0;
		for(i=0;i<q;i++) for(j=1;j<=n;j++) if(dp[i][j] < INF) {
			for(k=1;k<=n;k++) {
				if(ok[i+1][k]) {
					if(j == k) dp[i+1][k] = min(dp[i+1][k],dp[i][j]);
					else dp[i+1][k] = min(dp[i+1][k],dp[i][j]+1);
				}
			}
		}
		for(i=1;i<=n;i++) res = min(res,dp[q][i]);

		printf("Case #%d: %d\n",kase++,res);
	}
	return 0;
}