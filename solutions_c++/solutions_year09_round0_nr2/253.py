#include<iostream>
using namespace std;
#define maxn 200
int flag[maxn][maxn];
int a[maxn][maxn];
int dx[]={-1, 0, 0,1};
int dy[]={ 0,-1, 1,0};
int n,m;
int cnt;
int dfs(int x,int y)
{
	if(flag[x][y])  return flag[x][y];
	int i;
	int maxx=1000000;
	int ansx,ansy;
	for(i=0;i<4;i++)
	{
		int xx=dx[i]+x;
		int yy=dy[i]+y;
		if(xx>=0&&xx<n&&yy>=0&&yy<m)
		{
			if(a[xx][yy]<maxx)
			{
				maxx=a[xx][yy];
				ansx=xx;
				ansy=yy;
			}
		}
	}
	if(maxx>=a[x][y]) flag[x][y]=cnt++;
	else	flag[x][y]=dfs(ansx,ansy);
	return flag[x][y];
}
int main()
{
	int t;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&t);
	int i,j;
	
	for(int tt=1;tt<=t;tt++)
	{
		scanf("%d%d",&n,&m);
	
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
				flag[i][j]=0;
			}
		}
		cnt=1;
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				if(flag[i][j]==0) dfs(i,j);
			}
		}
		printf("Case #%d:\n",tt);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++) 
			{
				if(j) printf(" ");
				printf("%c",flag[i][j]-1+'a');
			}
			printf("\n");
		}
	}
	return 0;
}