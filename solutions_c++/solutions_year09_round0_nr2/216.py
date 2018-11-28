#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

#ifndef ONLINE_JUDGE
int poj();
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	poj();
	return 0;
}
#define main poj
#endif

#define clr(x) memset(x, 0, sizeof(x))
#define MAXINT 200000000
#define EPS 0.00000001
#define MAXN 300

int t, h, w, now;
const int direx[4] = {-1, 0, 0, 1};
const int direy[4] = {0, -1, 1, 0};
int amap[200][200];
//bool visit[200][200];
int result[200][200];

int dfs(int x, int y)
{
	int i, mini, mintop;
	//printf("x:%d y:%d\n", x, y);
	if (x >= 1 && x <= h && y >= 1 && y <= w)
	{
		if (!result[x][y])
		{
			result[x][y] = now;
			mintop = amap[x][y];
			mini = -1;
			for (i = 0; i < 4; i++)
			{
				if (amap[x + direx[i]][y + direy[i]] != -1 && amap[x + direx[i]][y + direy[i]] < mintop)
				{
					mintop = amap[x + direx[i]][y + direy[i]];
					mini = i;
				}
			}
			if (mini != -1)
			{
				result[x][y] = dfs(x + direx[mini], y + direy[mini]);
				return result[x][y];
			}
			else
			{
				now++;
				//printf("now:%d\n", now);
				result[x][y] = now;
				return now;
			}
		}
		else return result[x][y];
	}
}

int main()
{
	int i, j, k;
	
	scanf("%d", &t);
	for (k = 1; k <= t; k++)
	{
		clr(result);
		scanf("%d%d", &h, &w);
		memset(amap, 0xFF, sizeof(amap));
		for (i = 1; i <= h; i++)
			for (j = 1; j <= w; j++)
				scanf("%d", &amap[i][j]);

		now = 0;
		for (i = 1; i <= h; i++)
			for (j = 1; j <= w; j++)
			{
				if (!result[i][j])
				{
					//clr(visit);
					//result[i][j] = now;
					dfs(i, j);
				}
			}

		printf("Case #%d:\n", k);
		for (i = 1; i <= h; i++)
		{
			for (j = 1; j <= w; j++)
			{
				if (j != 1)
					printf(" ");
				printf("%c", 'a' + (result[i][j] - 1));
			}
			printf("\n");
		}
	}
	
	return 0;
}
