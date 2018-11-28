#include<stdio.h>
#include<string.h>

char a[16][16];
int dp[11][1024];
int n,m;

void dfs(int i,int j,int mask,int nm,int nn) {
	if (j==m) {
		if (dp[i+1][mask]+nn>dp[i][nm]) dp[i][nm]=dp[i+1][mask]+nn;
		return ;
	}
	if (a[i][j]=='.' && (!j && !(mask&2) || j && !(nm&(1<<(j-1))) && !(mask&(1<<(j-1))) && !(mask&(1<<(j+1)))))
		dfs(i,j+1,mask,nm|(1<<j),nn+1);
	dfs(i,j+1,mask,nm,nn);
}

void run(int T) {
	scanf("%d %d",&n,&m);
	for(int i=0;i<n;i++) scanf("%s",a[i]);
	memset(dp,0xff,sizeof(dp));
	dp[n][0]=0;
	for(int i=n-1;i>=0;i--)
		for(int j=0;j<(1<<m);j++)
			if (dp[i+1][j]>=0) dfs(i,0,j,0,0);
	int ret=0;
	for(int i=0;i<(1<<m);i++)
		if (dp[0][i]>ret) ret=dp[0][i];
	printf("Case #%d: %d\n",T,ret);
}

int main() {
	int N,cs=0;
	for(scanf("%d",&N);N--;)
		run(++cs);
	return 0;
}
