#include<stdio.h>
#include<stdlib.h>
#include<string.h>

const int X[5] = {-1,0,0,1};
const int Y[5] = {0,-1,1,0};

const int maxn = 300;

int MAT[maxn][maxn];
int GR[maxn * maxn],N,M;
int MA[maxn * maxn],T;

inline int code(int i,int j)
{
	return i * M + j;
}

int grupa(int x)
{
	if (GR[x] == x) return x;
	GR[x] = grupa(GR[x]);
	return GR[x];
}

void reuniune(int x,int y,int xn,int yn)
{
	GR[grupa(code(x,y))] = grupa(code(xn,yn));
}

void solve()
{
	scanf("%d %d\n",&N,&M);
	for(int i = 1;i <= N; ++i)
			for(int j = 1;j <= M; ++j)
			{
				scanf("%d",&MAT[i][j]);
				GR[code(i,j)] = code(i,j);
			}
	for(int i = 1;i <= N; ++i)
		for(int j = 1;j <= M; ++j)
		{
			int cur = 100000,xn = 0,yn = 0;
			for(int dir = 0;dir < 4; ++dir)
			{
				int x = i + X[dir];
				int y = j + Y[dir];
				if (x < 1 || x > N || y < 1 || y > M) continue;
				if (MAT[i][j] > MAT[x][y] && MAT[x][y] < cur)
				{
					cur = MAT[x][y];
					xn = x;
					yn = y;
				}
			}
//			printf("%d %d %d %d\n",i,j,xn,yn);
			if (xn != 0) reuniune(i,j,xn,yn);
		}
	int cur = 'a';
	memset(MA,0,sizeof(MA));
	for(int i = 1;i <= N; ++i)
			for(int j = 1;j <= M; ++j)
					if (!MA[grupa(code(i,j))]) {MA[grupa(code(i,j))] = cur; ++cur;}
	for(int i = 1;i <= N; ++i,printf("\n"))
			for(int j = 1;j <= M; ++j)
					printf("%c ",MA[grupa(code(i,j))]);

}

int main()
{
		freopen("waterfall.in","r",stdin);
		freopen("waterfall.out","w",stdout);
		scanf("%d",&T);
		for(int i = 1;i <= T; ++i)
		{
			printf("Case #%d:\n",i);
			solve();
		}
}



