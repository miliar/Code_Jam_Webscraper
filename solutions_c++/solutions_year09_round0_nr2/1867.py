#include <cstdio>
#include <cstring>
#include <algorithm>

int h,w,nType;
int map[101][101],g[101][101],IsSink[101][101],father[10001];
int ax[4]={-1,0,0,1},ay[4]={0,-1,1,0};
char type[30];

int check(int value)
{
	int i;
	for(i=0;i<nType;i++)
		if(type[i]==value)
			return i;
	return -1;
}

int find(int x)
{
	while(x!=father[x])
		father[x]=find(father[x]);
	return father[x];
}

void make(int a,int b)
{
	int i,j;
	b=find(b);
	for(i=0;i<h;i++)
		for(j=0;j<w;j++)
			if(g[i][j]==a)
				g[i][j]=b;
}

void dfs(int r,int c,int num)
{
	int i,min=map[r][c],dir=-1;
	if(g[r][c]>=0 || IsSink[r][c])
	{
		father[num]=g[r][c];
		make(num,g[r][c]);
		return;
	}
	else if(g[r][c]<0)
		g[r][c]=num;
	for(i=0;i<4;i++)
	{
		if(map[r+ax[i]][c+ay[i]]<min && (r+ax[i]>=0 && r+ax[i]<h) && (c+ay[i]>=0 && c+ay[i]<w))
		{
			min=map[r+ax[i]][c+ay[i]];
			dir=i;
		}
	}
	if(dir>=0)
		dfs(r+ax[dir],c+ay[dir],num);
	else
	{
		IsSink[r][c]=1;
		g[r][c]=num;
	}
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int nCase,i,j,case_Id,now;
	scanf("%d",&nCase);
	for(case_Id=1;case_Id<=nCase;case_Id++)
	{
		memset(map,0,sizeof(map));
		memset(g,-1,sizeof(g));
		memset(IsSink,0,sizeof(IsSink));
		for(i=0;i<10000;i++)
			father[i]=i;
		scanf("%d%d",&h,&w);
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
				scanf("%d",&map[i][j]);
		
		now=nType=0;
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
				if(g[i][j]==-1)
					dfs(i,j,now++);
		printf("Case #%d:\n",case_Id);
		nType=0;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				if(check(g[i][j])==-1 || !nType)
					type[nType++]=g[i][j];
				printf("%c ",check(g[i][j])+97);
			}
			printf("\n");
		}
	}
	return 0;
}