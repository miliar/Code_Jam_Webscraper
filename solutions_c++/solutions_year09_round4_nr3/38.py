#include<cstdio>

int n,K;
int a[105][30];
bool g[105][105];
int match[105];
bool valid[105];
bool can( int x )
{
	for(int i=1;i<=n;i++) if( valid[i] && g[x][i] )
	{
		valid[i] = false;
		if( match[i]==0 || can(match[i]) )
		{
			match[i] = x;
			return true;
		}
	}
	return false;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int num=1;num<=T;num++)
	{
		scanf("%d%d",&n,&K);
		for(int i=1;i<=n;i++)
		for(int j=1;j<=K;j++) scanf("%d",a[i]+j);

		for(int i=1;i<=n;i++)
		for(int j=1;j<=n;j++)
		{
			g[i][j] = false;
			if(a[i][1]<a[j][1])
			{
				g[i][j] = true;
				for(int k=1;k<=K;k++) if( a[i][k] >= a[j][k] )
				{
					g[i][j] = false;break;
				}
			}
		}

		int ans = n;
		for(int i=1;i<=n;i++) match[i] = 0;
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++) valid[j] = true;
			if(can(i)) ans--;
		}
		printf("Case #%d: %d\n",num,ans);
	}
	return 0;
}
