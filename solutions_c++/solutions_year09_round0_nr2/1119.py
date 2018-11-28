#include <cstdio>
#include <algorithm>

using namespace std;

int T,H,W;
int X[105][105];
int sink[105][105];
int f[105][105];
int q[10101];

int cmp(int a,int b)
{
	return X[a/W][a%W]<X[b/W][b%W];
}

int main()
{
	scanf("%d",&T);
	for(int t=1;t<=T;++t)
	{
		printf("Case #%d:\n",t);
		scanf("%d%d",&H,&W);
		for(int i=0;i<H;++i)
		{
			for(int j=0;j<W;++j)
			{
				scanf("%d",&X[i][j]);
				q[i*W+j]=i*W+j;
			}
		}
		sort(q,q+H*W,cmp);
		for(int i=0;i<H*W;++i)
		{
			int x=q[i]/W,y=q[i]%W;
			int x2=x,y2=y;
			if (x&&X[x-1][y]<X[x2][y2]) x2=x-1,y2=y;
			if (y&&X[x][y-1]<X[x2][y2]) x2=x,y2=y-1;
			if (y+1<W&&X[x][y+1]<X[x2][y2]) x2=x,y2=y+1;
			if (x+1<H&&X[x+1][y]<X[x2][y2]) x2=x+1,y2=y;
			if (x==x2&&y==y2) sink[x][y]=q[i];
			else sink[x][y]=sink[x2][y2];
			f[x][y]=0;
			//printf("%d %d - %d %d\n",x,y,q[i],sink[x][y]);
		}
		char farba='a';
		for(int i=0;i<H;++i)
		{
			for(int j=0;j<W;++j)
			{
				if (j) putchar(' ');
				int x=sink[i][j]/W,y=sink[i][j]%W;
				if (f[x][y]==0) f[x][y]=farba++;
				putchar(f[x][y]);
				//printf("%d",sink[i][j]);
			}
			puts("");
		}
	}
	return 0;
}
