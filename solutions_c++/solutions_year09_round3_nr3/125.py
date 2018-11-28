#include <stdio.h>
#include <string.h>
#include <limits.h>
const int MAXN=10002,MAXM=102;
int n,m;
int x[MAXM];
int f[MAXM][MAXM];
int dfs(int l,int r)
{
	if (l>r) return 0;
	if (f[l][r]>=0) return f[l][r];
	int ret=INT_MAX;
	for (int i=l;i<=r;i++)
	{
		int t=x[r+1]-x[l-1]-2+dfs(l,i-1)+dfs(i+1,r);
		if (t<ret) ret=t;
	}
	f[l][r]=ret;
	return ret;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	scanf("%d",&cases);
	for (int k=1;k<=cases;k++)
	{
		scanf("%d%d",&n,&m);
		for (int i=1;i<=m;i++) scanf("%d",&x[i]);
		x[0]=0;x[m+1]=n+1;
		memset(f,0,sizeof(f));
		for (int i=1;i<=m;i++)
			f[1][i]=x[i+1]-x[i-1]-2;
		for (int i=2;i<=m;i++)
			for (int j=1;j<=m-i+1;j++)
			{
				f[i][j]=1000000000;
				for (int k=j;k<=j+i-1;k++)
				{
					int t=x[i+j]-x[j-1]-2;
					t=t+f[k-j][j]+f[j+i-1-k][k+1];
					if (t<f[i][j]) f[i][j]=t;
				}
			}

		printf("Case #%d: %d\n",k,f[m][1]);
	}
	return 0;
}