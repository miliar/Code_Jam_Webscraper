#include <iostream>
#include <cstdio>
#include <set>
#include <algorithm>
#define M 105
using namespace std;
int G[M][M],g[M][M];
int R;
bool check()
{
	int i,j;
	for (i=1;i<M;i++)
		for (j=1;j<M;j++)
			if (g[i][j]) return 1;
	return 0;
}
bool Die(int x,int y)
{
	int i,j;
	if (g[x][y]==1)
	{
		if (g[x-1][y]==0 && g[x][y-1]==0) return 1;
		return 0;
	}
	else
	{
		if (g[x-1][y]==1 && g[x][y-1]==1) return 0;
		return 1;
	}
}
int main()
{
	int C,cases=0;
	freopen("D:\\C-small-attempt0.in","r",stdin);
	freopen("D:\\C-small-attempt0.out","w",stdout);
	scanf("%d",&C);
	while (C--)
	{
		cases++;
		scanf("%d",&R);
		int i,j,k;
		int x1,x2,y1,y2;
		memset(g,0,sizeof(g));
		for (k=0;k<R;k++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (i=x1;i<=x2;i++)
				for (j=y1;j<=y2;j++)
					g[i][j]=1;
		}
		for (i=1;i<M;i++)
			for (j=1;j<M;j++)
				G[i][j]=g[i][j];
		int cnt=0;
		while (check())
		{
			cnt++;
			for (i=1;i<M;i++)
				for (j=1;j<M;j++)
					if (Die(i,j))
						G[i][j]=0;
					else
						G[i][j]=1;
			for (i=1;i<M;i++)
				for (j=1;j<M;j++)
					g[i][j]=G[i][j];
		}
		printf("Case #%d: %d\n",cases,cnt);
	}
	return 0;
}