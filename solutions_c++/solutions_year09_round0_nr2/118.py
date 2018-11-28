#include <iostream>
using namespace std;

int t,h,w;
char dp[101][101];
int map[101][101];
bool flag[101][101];
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
char num;

char calc(int x,int y)
{
	if(flag[x][y]) return dp[x][y];
	int minn=1<<30;
	if(x>0) minn=min(minn,map[x-1][y]);
	if(y>0) minn=min(minn,map[x][y-1]);
	if(x<h-1) minn=min(minn,map[x+1][y]);
	if(y<w-1) minn=min(minn,map[x][y+1]);
	int i;int tx,ty;
	for(i=0;i<4;i++)
	{
		if(x+dir[i][0]>=0 && x+dir[i][0]<h && y+dir[i][1]>=0 && y+dir[i][1]<w && map[x+dir[i][0]][y+dir[i][1]]==minn)
		{
			tx=x+dir[i][0],ty=y+dir[i][1];break;
		}
	}
	if(minn<map[x][y])
	{
		dp[x][y]=calc(tx,ty);
		flag[x][y]=true;
		return dp[x][y];
	}
	else
	{
		dp[x][y]=num,num++,flag[x][y]=true;
		return dp[x][y];
	}
}

int main()
{
	FILE *fp=freopen("out.txt","w",stdout);
	scanf("%d",&t);
	int i,j,k;
	for(i=1;i<=t;i++)
	{
		num='a';
		memset(flag,0,sizeof(flag));
		scanf("%d%d",&h,&w);
		for(j=0;j<h;j++)
			for(k=0;k<w;k++)
			{
				scanf("%d",&map[j][k]);
			}
		for(j=0;j<h;j++)
			for(k=0;k<w;k++)
			{
				dp[j][k]=calc(j,k);
			}
		printf("Case #%d:\n",i);
		for(j=0;j<h;j++)
		{
			for(k=0;k<w-1;k++)
			{
				printf("%c ",dp[j][k]);
			}
			printf("%c\n",dp[j][k]);
		}
	}
	return 0;
}