#include <cstdio>
#include <cstring>

int T,W,H;
int al[128][128];
int color[128][128];
int dy[4]={-1,0,0,1};
int dx[4]={0,-1,1,0};
int change[64];
int flag;

void init()
{
	int i,j;
	
	scanf("%d%d",&H,&W);
	for (i=1;i<=H;i++)
	{
		for (j=1;j<=W;j++)
			scanf("%d",&al[i][j]);
	}
}

int check(int y,int x)
{
	if (y==0 || x==0 || y>H || x>W)
		return 0;
	return 1;
}

int DFS(int y,int x)
{
	int i,r,mymin;
	
	if (y==0 || x==0 || y>H || x>W)
		return 0;
	if (color[y][x])
		return color[y][x];
	
	mymin=20000;
	r=-1;
	for (i=0;i<4;i++)
	{
		if (check(y+dy[i],x+dx[i]))
			if (al[y][x]>al[y+dy[i]][x+dx[i]] && mymin>al[y+dy[i]][x+dx[i]])
			{
				r=i;
				mymin=al[y+dy[i]][x+dx[i]];
			}
	}
	if (r==-1)
	{
		flag++;
		color[y][x]=flag;
		return flag;
	}
	color[y][x]=DFS(y+dy[r],x+dx[r]);
	return color[y][x];
}

void work()
{
	int i,j,k;
	
	memset(color,0,sizeof(color));
	
	for (i=1;i<=H;i++)
	{
		for (j=1;j<=W;j++)
		{
			if (!color[i][j])
			{
				DFS(i,j);
			}
		}
	}
	
	k=0;
	memset(change,0,sizeof(change));
	for (i=1;i<=H;i++)
	{
		for (j=1;j<=W;j++)
		{
			if (change[color[i][j]]==0)
			{
				k++;
				change[color[i][j]]=k;
			}
		}
	}
	
	for (i=1;i<=H;i++)
	{
		for (j=1;j<=W;j++)
		{
			printf("%c%c",change[color[i][j]]+'a'-1,j<W?' ':'\n');
		}
	}
}

int main()
{
	int i;
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for (i=1;i<=T;i++)
	{
		init();
		flag=0;
		printf("Case #%d:\n",i);
		work();
	}
	return 0;
}
