#include <stdio.h>
#include <algorithm>
using  namespace std;

const  int MAXN = 110;
int  dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int  H, W;
int  bj[MAXN][MAXN];
int  mp[MAXN][MAXN];
int  CN;

int  dt[30];
int  DFS(int x, int y)
{
	int  i;
	int  tx, ty;
	int  cx = -1, cy = -1;
	if(bj[x][y] != -1) return  bj[x][y];
	for(i = 0; i < 4; i++)
	{
		int  tx = x+dir[i][0];
		int  ty = y+dir[i][1];
		if(tx >= 0 && tx < H && ty >= 0 && ty < W)
		{
			if(cx == -1 || mp[tx][ty] < mp[cx][cy])
			{
				cx = tx;
				cy = ty;
			}
		}
	}
	if(cx == -1 || mp[cx][cy] >= mp[x][y]) bj[x][y] = CN++;
	else  bj[x][y] = DFS(cx, cy);
	return  bj[x][y];
}
int  main()
{
	int  T;
	int  CAS = 1;
	int  i, j;
	//freopen("B.large.in", "r", stdin);
	//freopen("B.large.out", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		CN = 0;
		scanf("%d %d", &H, &W);
		for(i = 0; i < H; i++)
			for(j = 0; j < W; j++)
				scanf("%d", &mp[i][j]);
		memset(bj, -1, sizeof(bj));
		for(i = 0; i < H; i++)
		{
			for(j = 0; j < W; j++)
			{
				if(bj[i][j] == -1)
					bj[i][j] = DFS(i, j);
			}
		}
		printf("Case #%d:\n", CAS++);
		memset(dt, -1, sizeof(dt));
		int cc = 0;
		for(i = 0; i < H; i++)
		{
			for(j = 0; j < W; j++)
			{
				if(dt[bj[i][j]] == -1)
					dt[bj[i][j]] = cc++;
				printf("%c%c", dt[bj[i][j]]+'a', j == W-1 ? '\n' : ' ');
			}
		}
	}
	return 0;
}
