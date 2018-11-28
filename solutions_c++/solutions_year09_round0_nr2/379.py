//Watersheds

#include<iostream>
using namespace std;

const int MAX = 110;
const int mov[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

int water[MAX][MAX];
int mark[MAX][MAX];
int cnt;
int h, w;

void Init()
{
	scanf("%d%d", &h, &w);
	memset(water, 0x5e, sizeof(water));
	memset(mark, -1, sizeof(mark));
	int i, j;
	for(i=1; i<=h; ++i)
	{
		for(j=1; j<=w; ++j)
			scanf("%d", &water[i][j]);
	}
	cnt = 0;
}

void dfs(int x, int y)
{
	int i, dir = -1, mn = water[x][y], xx, yy;
	for(i=0; i<4; ++i)
	{
		xx = x + mov[i][0]; yy = y + mov[i][1];
		if(water[xx][yy] < mn)
		{
			dir = i;
			mn = water[xx][yy];
		}
	}
	if(dir == -1)mark[x][y] = cnt++;
	else 
	{
		xx = x + mov[dir][0];
		yy = y + mov[dir][1];
		if(mark[xx][yy] < 0)dfs(xx, yy);
		mark[x][y] = mark[xx][yy];
	}
}

void Solve(int no)
{
	int i, j;
	for(i=1; i<=h; ++i)
	{
		for(j=1; j<=w; ++j)
		{
			if(mark[i][j] < 0)dfs(i, j);
		}
	}
	printf("Case #%d:\n", no);
	for(i=1; i<=h; ++i)
	{
		for(j=1; j<=w; ++j)
		{
			if(j != 1)putchar(' ');
			putchar('a'+mark[i][j]);
		}
		putchar('\n');
	}
}

int main()
{
	int n, i;
	scanf("%d", &n);
	for(i=1; i<=n; ++i)
	{
		Init();
		Solve(i);
	}
	return 0;
}
