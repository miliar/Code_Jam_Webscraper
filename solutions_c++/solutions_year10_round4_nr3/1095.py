#include <iostream>
using namespace std;
int map[105][105];
bool judge(int r)
{
	int i,j;
	for(i=1;i<=r;i++)
		for(j=1;j<=r;j++)
			if(map[i][j]==1)return 0;
	return 1;
}
void work (int r)
{
	int i,j;
	for(i=r;i>0;i--)
	{
		for(j=r;j>0;j--)
		{
			if(map[i-1][j]==0&&map[i][j-1]==0)map[i][j]=0;
			if(map[i-1][j]==1&&map[i][j-1]==1)map[i][j]=1;
		}
	}
}
int main ()
{
	int T,t,i,x1,x2,y1,y2,ii,jj,ans,r,max;
	freopen("a.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		memset(map,0,sizeof(map));
		scanf("%d",&r);
		max=0;
		for(i=0;i<r;i++)
		{
			scanf("%d%d%d%d",&y1,&x1,&y2,&x2);
			if(max<x2)max=x2;
			if(max<y2)max=y2;
			for(ii=x1;ii<=x2;ii++)
				for(jj=y1;jj<=y2;jj++)map[ii][jj]=1;
		}
		ans=0;
		while(judge(max+1)==0)
		{
			work(max+1);
			ans++;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}