#include <iostream>
#define MAXSIZE 105
#define MIN -1
using namespace std;

int t, h, w, temp;
int map[MAXSIZE][MAXSIZE];
int water[MAXSIZE][MAXSIZE];
bool maped[MAXSIZE][MAXSIZE];

void fall(int i, int j)
{
	if (water[i][j] >= 0)
	{
		return;
	}

	int min, x, y;
	min = 10005;
	x = y = -1;
	
	//South
	if (min >= map[i + 1][j] && map[i + 1][j] != -1)
	{
		min = map[i + 1][j];
		x = i + 1;
		y = j;
	}
	//East
	if (min >= map[i][j + 1] && map[i][j + 1] != -1)
	{
		min = map[i][j + 1];
		x = i;
		y = j + 1;
	}
	//West
	if (min >= map[i][j - 1] && map[i][j - 1] != -1)
	{
		min = map[i][j - 1];
		x = i;
		y = j - 1;
	}
	//North
	if (min >= map[i - 1][j] && map[i - 1][j] != -1)
	{
		min = map[i - 1][j];
		x = i - 1;
		y = j;
	}
	
	if (min < map[i][j])
	{
		fall(x, y);
		water[i][j] = water[x][y];
	}
	else
	{
		water[i][j] = temp++;
	}
}

void solve()
{
	int i, j;

	for (i = 1; i <= h; ++i)
	{
		for (j = 1; j <= w; ++j)
		{
			fall(i, j);
		}
	}

	for (i = 1; i <= h; ++i)
	{
		for (j = 1; j <= w; ++j)
		{
			printf("%c", 'a' + water[i][j]);
			if (j != w)
			{
				printf(" ");
			}
			else
			{
				printf("\n");
			}
		}
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("Watersheds.out", "w", stdout);

	int i, j, k;
	cin >> t;
	
	for (i = 1; i <= t; ++i)
	{
		cin >> h >> w;
		
		//初始化
		for (j = 1; j <= h; ++j)
		{
			for (k = 1; k <= w; ++k)
			{
				water[j][k] = -1;
			}
		}

		temp = 0;
		for (j = 0; j <= w + 1; ++j)
		{
			map[0][j] = MIN;
			map[h + 1][j] = MIN;
		}
		for (j = 0; j <= h + 1; ++j)
		{
			map[j][0] = MIN;
			map[j][w + 1] = MIN;
		}
		
		//输入地图
		for (j = 1; j <= h; ++j)
		{
			for (k = 1; k <= w; ++k)
			{
				scanf("%d", &map[j][k]);
			}
		}
		
		cout << "Case #" << i << ":" << endl;
		solve();

	}
	return 0;
}