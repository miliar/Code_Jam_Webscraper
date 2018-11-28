#include<cstdio>
char str[100][100];
int dp[15][2000];
int n,m;
void dfs(int h,int r1,int r2,int s1,int s2,int p)
{
	int i,ct;
	if(p==m)
	{
		ct=0;
		for(i=0;i<m;i++)
		{
			if((1<<i)&s2)
			ct++;
		}
		dp[h][s2]>?=dp[h-1][s1]+ct;
		//printf("** %d %d %d\n",s1,s2,h);
		return;
	}
	dfs(h,0,0,2*s1,2*s2,p+1);
	if(h==1||str[h-2][p]=='.')
	{
		if(r1==0&&r2==0)
		dfs(h,1,0,2*s1+1,2*s2,p+1);
	}
	if(str[h-1][p]=='.'&&r1==0&&r2==0)
	{
		dfs(h,0,1,2*s1,2*s2+1,p+1);
		if(h==1||str[h-2][p]=='.')
		dfs(h,1,1,2*s1+1,2*s2+1,p+1);
	}
}
	
	
	
	
int main()
{
	int t,cc,i,j;
	int best;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++)
	{
		scanf("%d%d",&n,&m);
		best=0;
		for(i=0;i<=n;i++)
			for(j=0;j<(1<<m);j++)
			dp[i][j]=0;
		for(i=0;i<n;i++)
		scanf("%s",str[i]);
		for(i=1;i<=n;i++)
		dfs(i,0,0,0,0,0);
		for(i=0;i<(1<<m);i++)
		best>?=dp[n][i];
		printf("Case #%d: %d\n",cc,best);
	}
	return 0;
}
		
		
		
		
	
