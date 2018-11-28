#include<stdio.h>
#include<string.h>
const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};

char c[110][110];
int n,m,g[110][110];
char d[10010];

int dfs(int x,int y)
{
	if (c[x][y]>0) return c[x][y];
	int mm=g[x][y],xx,yy,tx,ty;
	for (int i=0;i<4;i++)
	{
		tx=x+dx[i];
		ty=y+dy[i];
		if (tx<0||ty<0||tx>n-1||ty>m-1) continue;
		if (g[tx][ty]<mm)
		{
			mm=g[tx][ty];
			xx=tx;
			yy=ty;
		}
	}
	return dfs(xx,yy);
}

int x,y,p,N,z,i,j,k;
char tc;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("Blarge.txt","w",stdout);
	scanf("%d",&N);
	for (z=1;z<=N;z++)
	{
		printf("Case #%d:\n",z);
		scanf("%d%d",&n,&m);
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
				scanf("%d",&g[i][j]);
		p=1;
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
			{
				for (k=0;k<4;k++)
				{
					x=i+dx[k];
					y=j+dy[k];
					if (x<0||y<0||x>n-1||y>m-1) continue;
					if (g[x][y]<g[i][j]) break;
				}
				if (k==4) c[i][j]=p++; else c[i][j]=0;
			//	printf("%d%c",c[i][j],j==m-1?'\n':' ');
			}
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
				if (c[i][j]==0) c[i][j]=dfs(i,j);
		tc='a';
		memset(d,0,sizeof d);
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
				if (d[c[i][j]]==0) d[c[i][j]]=tc++;
		for (i=0;i<n;i++)
		{
			for (j=0;j<m-1;j++) printf("%c ",d[c[i][j]]);
			printf("%c\n",d[c[i][j]]);
		}
	}
}
