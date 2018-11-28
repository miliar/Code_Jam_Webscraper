#include<iostream>
using namespace std;

#define MAXINT 2100000000


int CASE;
int cnt,n,p;
int a[200];
int ans[201][201];

int dfs(int x,int y)
{
	if (ans[x][y]!=MAXINT)
		return ans[x][y];
	if (y-x==1)
	{
		ans[x][y]=0;
		return 0;
	}
	for (int i=x+1;i<=y-1;i++)
	{
		int t=dfs(x,i)+dfs(i,y)+(a[y]-a[x]-2);
		if (ans[x][y]>t)
			ans[x][y]=t;
	}
	return ans[x][y];
}

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (CASE=1;CASE<=T;CASE++)
	{
		cnt=0;
		scanf("%d%d",&n,&p);
		a[++cnt]=0;
		for (int j=1;j<=p;j++)
		{
			int t;
			scanf("%d",&t);
			a[++cnt]=t;
		}
		a[++cnt]=n+1;
		for (int i=1;i<=cnt;i++)
			for (int j=1;j<=cnt;j++)
				ans[i][j]=MAXINT;
		int t=dfs(1,cnt);
		printf("Case #%d: %d\n",CASE,t);
	}
}