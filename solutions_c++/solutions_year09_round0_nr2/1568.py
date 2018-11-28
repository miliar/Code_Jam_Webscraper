#include<iostream>
using namespace std;
const int N=105;
int grid[N][N],mark[N][N];
int m,n;
int movex[4]={-1,0,0,1};
int movey[4]={0,-1,1,0};
char str[N*N],ans[N][N];
int dfs(int x,int y)
{
	int i,j,k,ret=x*101+y;
	int tmin=INT_MAX;
	for(i=0;i<4;i++)
	{
		j=x+movex[i];
		k=y+movey[i];
		if(tmin>grid[j][k])tmin=grid[j][k];
	}
	for(i=0;i<4;i++)
	{
		j=x+movex[i];
		k=y+movey[i];
		if(grid[j][k]<grid[x][y]&&tmin==grid[j][k])
		{
			if(!mark[j][k])ret=dfs(j,k);
			else ret=mark[j][k];
			break;
		}
	}
	mark[x][y]=ret;
	return ret;
}
int main()
{freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	int i,j,k,t;scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d%d",&m,&n);
		memset(grid,127,sizeof(grid));
		for(i=1;i<=m;i++)
		{
			for(j=1;j<=n;j++)
			{
				scanf("%d",&grid[i][j]);
			}
		}
		memset(mark,0,sizeof(mark));
		for(i=1;i<=m;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(!mark[i][j])
				{
					dfs(i,j);
				}
			}
		}
		memset(str,'*',sizeof(str));
		char tc='a';
		for(i=1;i<=m;i++)
		{
			for(j=1;j<=n;j++)
			{
				if(str[mark[i][j]]=='*')
				{
					ans[i][j]=tc;
					str[mark[i][j]]=tc;
					tc++;
				}
				else ans[i][j]=str[mark[i][j]];
			}
		}
		printf("Case #%d:\n",k);
		for(i=1;i<=m;i++)
		{
			for(j=1;j<=n;j++)
			{
				printf("%c",ans[i][j]);
				if(j!=n)printf(" ");
			}
			printf("\n");
		}
	}
	return 0;
}