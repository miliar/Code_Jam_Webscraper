#include <stdio.h>
#include <memory.h>

const int step[4][2]={-1,0,0,-1,0,1,1,0};
const int maxn = 110;

int i,j,n,m,x,y,x1,y1,k,t,cases,s;
int f[maxn][maxn][2],a[maxn][maxn],ans[maxn][maxn];
char daan[maxn][maxn],ch;

bool able(int x,int y)
{
	if(x<1||x>n||y<1||y>m) return false;
	return true;
}

void head(int & x,int & y)
{ 
	if (x==f[x][y][0]&&y==f[x][y][1]) return ;
	head(f[x][y][0],f[x][y][1]);
	int i=x,j=y;
	x=f[i][j][0];
	y=f[i][j][1];
}
void dfs(int x,int y)
{
	daan[x][y]=ch;
	int i,j,k;
	for (k=0;k<4;k++)
	{
		i=x+step[k][0];
		j=y+step[k][1];
		if (able(i,j)&&ans[x][y]==ans[i][j]&&daan[i][j]=='0') dfs(i,j);
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&cases);
	for (t=1;t<=cases;t++)
	{
		memset(ans,0,sizeof(ans));
		memset(f,0,sizeof(f));
		scanf("%d%d",&n,&m);
		for (i=1;i<=n;i++)
			for (j=1;j<=m;j++)
				scanf("%d",&a[i][j]);
		s=1;	
		for (i=1;i<=n;i++)
			for (j=1;j<=m;j++)
			{
				x1=-1;
				y1=0;
				for (k=0;k<4;k++)
				{
					x=i+step[k][0];
					y=j+step[k][1];
					if (able(x,y))
						if (x1<0||a[x][y]<a[x1][y1])
						{
							x1=x;
							y1=y;
						}
				}
				if (a[i][j]<=a[x1][y1])
				{
					ans[i][j]=s++;
					f[i][j][0]=i;
					f[i][j][1]=j;
				} else
				{
					f[i][j][0]=x1;
					f[i][j][1]=y1;
				}
			}
		printf("Case #%d:\n",t);
		for (i=1;i<=n;i++)
			for (j=1;j<=m;j++)
			{
				x=i; y=j;
				head(x,y);
				ans[i][j]=ans[x][y];
				daan[i][j]='0';
			}
		ch='a';
		for (i=1;i<=n;i++)
			for (j=1;j<=m;j++)
				if (daan[i][j]=='0')
				{
					dfs(i,j);
					ch++;
				}
		for (i=1;i<=n;i++)
		{
			for (j=1;j<m;j++) printf("%c ",daan[i][j]);
			printf("%c\n",daan[i][m]);
		}
	}
	return 0;
}