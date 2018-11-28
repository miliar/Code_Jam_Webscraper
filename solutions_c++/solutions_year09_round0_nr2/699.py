#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <string>
#include <map>

using namespace std;

const  int SZ=105;
int M, N;
int d[SZ][SZ];
char a[SZ][SZ];
const int sx[4]={-1, 0, 0, 1};
const int sy[4]={0, -1, 1, 0};
void output();

void init()
{
	memset(a, 0, sizeof(a));
}

void dfs(int x, int y, char c)
{
	for(int i=0; i<4; i++)
	{
		int nx=x+sx[i];
		int ny=y+sy[i];
		if(nx>=0 && nx<M && ny>=0 && ny<N && a[nx][ny]=='\0')
		{
			int px=nx, py=ny;
			for(int i=0; i<4; i++)
			{
				int nnx=nx+sx[i], nny=ny+sy[i];
				if(nnx>=0 && nnx<M && nny>=0 && nny<N)
				{
					if(d[px][py]>d[nnx][nny])
					{
						px=nnx;
						py=nny;
					}
				}
			}
			if(px==x && py==y)
			{
				a[nx][ny]=c;
				dfs(nx, ny, c);
			}
		}
	}
	//output();
}

void single_solve(int x, int y, char c)
{
	int px=x, py=y;
	while(1)
	{
		a[px][py]=c;
		dfs(px, py, c);
		int ppx=px, ppy=py;
		for(int i=0; i<4; i++)
		{
			int nx=px+sx[i], ny=py+sy[i];
			if(nx>=0 && nx<M && ny>=0 && ny<N)
			{
				if(d[ppx][ppy]>d[nx][ny])
				{
					ppx=nx;
					ppy=ny;
				}
			}
		}
		if(ppx==px && ppy==py)
		{
			break;
		}
		else
		{
			px=ppx;
			py=ppy;
		}
	}
}

void solve()
{
	int cnt=0;
	for(int i=0; i<M; i++)
	{
		for(int j=0; j<N; j++)
		{
			if(a[i][j]=='\0')
			{
				single_solve(i, j, char(cnt+'a'));
				cnt++;
			}
		}
	}
}

void output()
{
	for(int i=0; i<M; i++)
	{
		for(int j=0; j<N; j++)
		{
			printf("%c ", a[i][j]);
		}
		printf("\n");
	}
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t=1; t<=T; t++)
	{
		scanf("%d%d", &M, &N);
		for(int i=0; i<M; i++)
		{
			for(int j=0; j<N; j++)
			{
				scanf("%d", &d[i][j]);
			}
		}
		init();
		solve();
		printf("Case #%d:\n", t);
		output();
	}
    return 0;
}

