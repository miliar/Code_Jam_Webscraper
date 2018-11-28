#include <cstdio>
#include <algorithm>
using namespace std;


int N,X,Y;
bool G[2][105][105];
inline bool check(int u)
{
	for (int i=1;i<=X;++i)
	for (int j=1;j<=Y;++j)
	if (G[u][i][j])	return 0;
	return 1;
}

int main()
{
	int N,x1,y1,x2,y2,T;
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for (int Te=1;Te<=T;++Te)
	{
		X=0,Y=0;
		scanf("%d",&N);
		memset(G,0,sizeof(G));
		for (int i=0;i<N;++i)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			swap(x1,y1),swap(x2,y2); 
			X=max(X,x1);
			X=max(X,x2);
			Y=max(Y,y1);
			Y=max(Y,y2);
			for (int i=x1;i<=x2;++i)
			for (int j=y1;j<=y2;++j)
				G[0][i][j]=1;
		}
		X+=5,Y+=5;
		int ret=0;
		for (;;++ret)
		{
			int now=(ret&1)^1;
			for (int i=1;i<=X;++i)
			for (int j=1;j<=Y;++j)
			if (G[now^1][i][j])
				if (G[now^1][i-1][j]==0&&G[now^1][i][j-1]==0)	G[now][i][j]=0;
				else	G[now][i][j]=1;
			else
				if (G[now^1][i-1][j]==1&&G[now^1][i][j-1]==1)	G[now][i][j]=1;
				else	G[now][i][j]=0;
			if (check(now))	break;
		}
		printf("Case #%d: %d\n",Te,ret+1);
	}
	return 0;
}
