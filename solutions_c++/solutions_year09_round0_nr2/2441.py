#include<stdio.h>
#include<string.h>

int cost[105][105];
int visit[105][105];
int flag[105][105];
char ans[105][105];
int go[105][105][5];
int n,m;

int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
int lab[4]={3,2,1,0};

int dfs1(int x,int y,int k)
{
	int i,tx,ty;
	visit[x][y]=k;
	for(i=0;i<4;i++)
	{
		if(go[x][y][i])
		{
			tx=x+dx[i];
			ty=y+dy[i];
			dfs1(tx,ty,k);
		}
	}
	return 0;
}

int dfs2(int x,int y,char w)
{
	int i;
	int tx,ty;
	ans[x][y]=w;
	for(i=0;i<4;i++)
	{
		tx=x+dx[i];
		ty=y+dy[i];
		if((!ans[tx][ty])&&(visit[tx][ty]==visit[x][y]))
			dfs2(tx,ty,w);
	}
	return 0;
}

int solve()
{
	int i,j,k;
	char w;
	int to;
	int tx,ty;
	memset(flag,0,sizeof(flag));
	memset(go,0,sizeof(go));
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m;j++)
		{
			to=-1;
			for(k=0;k<4;k++)
			{
				tx=i+dx[k];
				ty=j+dy[k];
				if((to==-1)||(cost[tx][ty]<cost[i+dx[to]][j+dy[to]]))
					to=k;
			}
			tx=i+dx[to];
			ty=j+dy[to];
			if(cost[tx][ty]<cost[i][j])
			{
				go[tx][ty][lab[to]]=1;
			}
			else
			{
				flag[i][j]=1;
			}
		}
	}
	k=0;
	memset(visit,-1,sizeof(visit));
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m;j++)
		{
			if(flag[i][j])
				dfs1(i,j,k++);
		}
	}
	w='a';
	memset(ans,0,sizeof(ans));
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=m;j++)
		{
			if(!ans[i][j])
				dfs2(i,j,w++);
		}

	}
	return 0;

}

int main()
{
	int t,T;
	int i,j;
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d",&n,&m);
		memset(cost,127,sizeof(cost));
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
				scanf("%d",&cost[i][j]);
		}
		solve();
		printf("Case #%d:\n",t);
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++)
				printf("%c ",ans[i][j]);
			printf("\n");
		}
	}
	return 0;
}