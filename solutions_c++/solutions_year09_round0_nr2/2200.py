#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int derx[4]={-1,0,0,1};
int dery[4]={0,-1,1,0};
int n,m;
int mat[105][105];
bool visit[106][105];
int cnt=0;
int map[105][105];
int dfs(int x,int y)
{
	if(map[x][y]!=-1)
		return map[x][y];
	int next_x=-1,next_y=-1,min=mat[x][y];
	for(int i=0;i<4;i++)
	{
		int temp_x=x+derx[i];
		int temp_y=y+dery[i];
		if(temp_x<1||temp_x>n||temp_y<1||temp_y>m||visit[temp_x][temp_y])
			continue;
		if(mat[temp_x][temp_y]<min)
		{
			min=mat[temp_x][temp_y];
			next_x=temp_x;
			next_y=temp_y;
		}
	}
	if(next_x==-1)
	{
		map[x][y]=cnt++;
		return map[x][y];
	}
	return map[x][y]=dfs(next_x,next_y);
}
int main()
{
	freopen("fuckk.in","r",stdin);
	freopen("fuckk.out.txt","w",stdout);
	int i,j;
	int T;
	scanf("%d",&T);
	int case_cnt=1;
	while(T--)
	{
		cnt=0;
		memset(map,-1,sizeof(map));
		memset(visit,0,sizeof(visit));
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				scanf("%d",&mat[i][j]);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
			{
				if(map[i][j]==-1)
					dfs(i,j);
			}
			printf("Case #%d:\n",case_cnt++);
			for(i=1;i<=n;i++)
			{
				for(j=1;j<m;j++)
					printf("%c ",map[i][j]+'a');
				printf("%c\n",map[i][m]+'a');
			}
	}
}
