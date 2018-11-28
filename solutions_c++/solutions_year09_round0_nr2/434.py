#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#define MAXN 111
#define MAXM 111
#define INF 99999999

const int Dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

int n,m,c,h[MAXN][MAXM],f[MAXN][MAXM];

inline bool inBoard(int x,int y)
{
	if (x>=1 && x<=n && y>=1 && y<=m)
		return true;
	return false;
}

void view(int i,int j)
{
	int d,min=h[i][j],minx,miny,x,y;
	for (d=0;d<4;d++)
	{
		x=i+Dir[d][0];
		y=j+Dir[d][1];
		if (inBoard(x,y) && h[x][y]<min)
		{
			min=h[x][y];
			minx=x;
			miny=y;
		}
	}
	if (min==h[i][j])
	{
		f[i][j]=c++;
		return;
	}
	if (f[minx][miny]==-1)
		view(minx,miny);
	f[i][j]=f[minx][miny];
}

void run()
{
	int i,j;
	for (i=1;i<=n;i++)
		for (j=1;j<=m;j++)
			if (f[i][j]==-1)
				view(i,j);
}

void ini()
{
	int T,k,i,j;
	scanf("%d",&T);
	for (k=1;k<=T;k++)
	{
		scanf("%d%d",&n,&m);
		for (i=1;i<=n;i++)
			for (j=1;j<=m;j++)
				scanf("%d",&h[i][j]);
		memset(f,-1,sizeof(f));
		c=0;
		run();
		//Case #1:
		printf("Case #%d:\n",k);
		for (i=1;i<=n;i++)
		{
			for (j=1;j<=m;j++)
			{
				printf("%c",f[i][j]+'a');
				if (j==m)
					printf("\n");
				else
					printf(" ");
			}
		}
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	ini();
	return 0;
}
