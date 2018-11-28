#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
const int dx[]={-1,0,0,1,0};
const int dy[]={0,-1,1,0,0};
int N,M,Map[102][102],F[102][102],Tx[102][102],Ty[102][102];
char Ret[102][102];

inline void Work(int x,int y)
{
	if (F[x][y]>=0) return;
	int minh=10000000,k=4;
	for (int i=0;i<4;i++) {
		int u=x+dx[i],v=y+dy[i];
		if (u<1 || u>N || v<1 || v>M) continue;
		if (Map[u][v]<minh) minh=Map[u][v],k=i;
	}
	if (minh<Map[x][y]) {
		F[x][y]=k;
		Work(x+dx[k],y+dy[k]);
		Tx[x][y]=Tx[x+dx[k]][y+dy[k]];
		Ty[x][y]=Ty[x+dx[k]][y+dy[k]];
	} else {
		F[x][y]=4;
		Tx[x][y]=x;
		Ty[x][y]=y;
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int Test;
	scanf("%d",&Test);
	for (int Case=1;Case<=Test;Case++) {
		scanf("%d%d",&N,&M);
		for (int i=1;i<=N;i++)
		for (int j=1;j<=M;j++)
			scanf("%d",&Map[i][j]);
		memset(F,-1,sizeof(F));
		for (int i=1;i<=N;i++)
		for (int j=1;j<=M;j++)
			Work(i,j);
		memset(Ret,0,sizeof(Ret));
		for (int i=1,k=0;i<=N;i++)
		for (int j=1;j<=M;j++)
		if (!Ret[i][j]) {
			for (int u=1;u<=N;u++)
			for (int v=1;v<=M;v++)
			if (Tx[i][j]==Tx[u][v] && Ty[i][j]==Ty[u][v])
				Ret[u][v]=k+'a';
			++k;
		}
		printf("Case #%d:\n",Case);
		for (int i=1;i<=N;i++) {
			for (int j=1;j<M;j++)
				printf("%c ",Ret[i][j]);
			printf("%c\n",Ret[i][M]);
		}
	}
	return 0;
}
