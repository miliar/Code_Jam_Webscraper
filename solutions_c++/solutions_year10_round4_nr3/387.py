#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int T;
int r;
int x1,y1,x2,y2;
int a[2][405][405];
int now;

void go()
{
	for(int i=1;i<=400;i++)
		for(int j=1;j<=400;j++)
		{
			a[now][i][j]=a[now^1][i][j];
			if(!a[now^1][i][j])
				if(a[now^1][i-1][j]==1&&a[now^1][i][j-1]==1)
					a[now][i][j]=1;
			if(a[now^1][i][j])
				if(!a[now^1][i-1][j]&&!a[now^1][i][j-1])
					a[now][i][j]=0;
		}
	return;
}

bool check()
{
	for(int i=1;i<=400;i++)
		for(int j=1;j<=400;j++)
			if(a[now][i][j])
				return false;
	return true;
}

int main()
{
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int T;
	scanf("%d",&T);
	int test=0;
	while(T--)
	{
		memset(a,0,sizeof(a));
		int ans=0;
		scanf("%d",&r);
		now=0;
		for(int i=0;i<r;i++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int x=x1;x<=x2;x++)
				for(int y=y1;y<=y2;y++)
					a[now][x][y]=1;
		}
		while(!check())
		{
			ans++;
			now^=1;
			go();
		}
		printf("Case #%d: %d\n",++test,ans);
	}
	return 0;
}

