#include<stdio.h>
#include<string.h>
#define maxn 110
int d[maxn][maxn];
int fa[maxn][maxn][2];
char ans[maxn][maxn];

int po[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

char p;

int n,m;

void findfa(int x,int y,int & x1,int & y1)
{
	if(fa[x][y][0]==x&&fa[x][y][1]==y)
	{
		if(ans[x][y]<0) ans[x][y]=p++;
		x1=x;
		y1=y;
	}
	else
	{
		findfa(fa[x][y][0],fa[x][y][1],x1,y1);
		fa[x][y][0]=x1;
		fa[x][y][1]=y1;
	}
}

bool testin(int x,int y)
{
	if(x<0||x>=n) return 0;
	if(y<0||y>=m) return 0;
	return 1;
}

void output(int x,int y)
{
	int x1,y1;
	findfa(x,y,x1,y1);
	printf("%c",ans[x1][y1]);
}

void solve()
{
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;++i)
		for(int j=0;j<m;++j)
		{
			scanf("%d",&d[i][j]);
			fa[i][j][0]=i;
			fa[i][j][1]=j;
		}
	for(int i=0;i<n;++i)
		for(int j=0;j<m;++j)
		{
			int h=d[i][j];
			for(int k=0;k<4;++k)
				if(testin(i+po[k][0],j+po[k][1])&&d[i+po[k][0]][j+po[k][1]]<h)
				{
					h=d[i+po[k][0]][j+po[k][1]];
					fa[i][j][0]=i+po[k][0];
					fa[i][j][1]=j+po[k][1];
				}
		}
	memset(ans,0xff,sizeof(ans));
	p='a';
	for(int i=0;i<n;++i)
	{
		output(i,0);
		for(int j=1;j<m;++j)
		{
			printf(" ");
			output(i,j);
		}
		puts("");
	}
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
	{
		printf("Case #%d:\n",i+1);
		solve();
	}
	return 0;
}

