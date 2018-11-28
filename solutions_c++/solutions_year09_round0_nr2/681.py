#include <iostream>
using namespace std;
struct node
{
	int x,y;
};
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int mark[110][110];
int g[110][110];
int cnt;
int H,W;
void dfs(int x,int y)
{
	int i,k=-1;
	int Min=g[x][y];
	for(i=0;i<4;i++)
	{
		if(x+dx[i]<0||x+dx[i]>=H||y+dy[i]<0||y+dy[i]>=W)continue;
		if(g[x+dx[i]][y+dy[i]]<Min)Min=g[x+dx[i]][y+dy[i]],k=i;
	}
	if(k==-1)
	{
		if(mark[x][y]==-1)mark[x][y]=cnt++;
		return ;
	}
	else
	{
		if(mark[x+dx[k]][y+dy[k]]>=0)
		{
			mark[x][y]=mark[x+dx[k]][y+dy[k]];
			return ;
		}
		else dfs(x+dx[k],y+dy[k]);
	}
	mark[x][y]=mark[x+dx[k]][y+dy[k]];
}
void DFS(int x,int y)
{
	int i,k=-1;
	int Min=g[x][y];
	for(i=0;i<4;i++)
	{
		if(x+dx[i]<0||x+dx[i]>=H||y+dy[i]<0||y+dy[i]>=W)continue;
		if(g[x+dx[i]][y+dy[i]]<Min)Min=g[x+dx[i]][y+dy[i]],k=i;
	}
	if(k==-1)return;
	else
	{
		mark[x+dx[k]][y+dy[k]]=mark[x][y];
		DFS(x+dx[k],y+dy[k]);
	}
}
int main()
{
	int t,i,j;
	int cs=0;
	freopen("Download B-small.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		cs++;
		scanf("%d %d",&H,&W);
		memset(mark,-1,sizeof(mark));
		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
				scanf("%d",&g[i][j]);
		mark[0][0]=0;
		cnt=1;
		for(i=0;i<H;i++)
		{
			for(j=0;j<W;j++)
			{
				if(mark[i][j]>=0)DFS(i,j);
				else dfs(i,j);
			}
		}
		printf("Case #%d:\n",cs);
		for(i=0;i<H;i++)
		{
			for(j=0;j<W;j++)
				printf("%c ",mark[i][j]+'a');
			printf("\n");
		}
	}
	return 0;
}