#include<iostream>
using namespace std;
int map[101][101];
int ans[101][101];
int num;
int h,w;
int fang[4][2]={-1,0,0,-1,0,1,1,0};
int dfs(int a,int b)
{
//	printf("%d %d\n",a,b);
	int i,j;
	int x,y;
	int aa,bb;
	int mmin=map[a][b];
	//ans[a][b]=num;
	aa=-1;
	bb=-1;
	for(i=0;i<4;i++)
	{
		x=a+fang[i][0];
		y=b+fang[i][1];
		if(x==0 || y==0 || x>h || y>w)
			continue;
		if(map[x][y] < mmin)
		{
			mmin=map[x][y];
			aa=x;
			bb=y;
		}
	}
	if(aa==-1)
	{
		num++;
		ans[a][b]=num;
	}
	else if(ans[aa][bb]!=0)
	{
		ans[a][b]=ans[aa][bb];
	}
	else
	{
		ans[a][b]=dfs(aa,bb);
	}
	return ans[a][b];
	
}

int main()
{
	int t,tt=0;
	int i,j,k;
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);

	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d",&h,&w);
		tt++;
		for(i=1;i<=h;i++)
			for(j=1;j<=w;j++)
				scanf("%d",&map[i][j]);
		memset(ans,0,sizeof(ans));

		//ans[1][1]=1;
		num=0;
		for(i=1;i<=h;i++)
			for(j=1;j<=w;j++)
			{
				if(ans[i][j]==0)
				{
					//num++;
					ans[i][j]=dfs(i,j);
				//	printf("%d \n",ans[i][j]);
				}
			}
			printf("Case #%d:\n",tt);
		for(i=1;i<=h;i++)
		{
			for(j=1;j<w;j++)
				printf("%c ",ans[i][j]+96);
				printf("%c",ans[i][j]+96);
			printf("\n");
		}
	}
	return 0;
}