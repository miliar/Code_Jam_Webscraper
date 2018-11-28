#include<iostream>
#include<list>
using namespace std;

int map[102][102];
char mark[102][102];

struct cell
{
	int x, y, value;
};

bool ccell(cell c1, cell c2)
{
	return c1.value > c2.value;
}

cell icell(int x, int y, int v)
{
	cell c;
	c.x = x;
	c.y = y;
	c.value = v;
	return c;
}

void findmin(int& x, int& y)
{
	if(map[x][y-1] <= map[x-1][y] && map[x][y-1] <= map[x+1][y] && map[x][y-1] <= map[x][y+1]){ y--; return; }
	if(map[x-1][y] <= map[x+1][y] && map[x-1][y] <= map[x][y+1]){ x--; return; }
	if(map[x+1][y] <= map[x][y+1]){ x++; return; }
	y++; return;
}

bool isSink(int x, int y)
{
	if( map[x - 1][y] >= map[x][y] &&
		map[x + 1][y] >= map[x][y] &&
		map[x][y - 1] >= map[x][y] &&
		map[x][y + 1] >= map[x][y]) return true;

	return false;
}

void reput(int a, char c, int w, int h)
{
	int i, j;

	for(j = 1; j <= h; j++)
	{
		for(i = 1; i <= w; i++)
		{
			if(mark[i][j] == a) mark[i][j] = c;
		}
	}
}

int main()
{
	int n, k, h, w, i, j, v;
	char a;
	list<cell> cells;
	list<int> step_x;
	list<int> step_y;
	cell c;

	cin >> n;

	for(k = 1; k <= n; k++)
	{
		scanf("%d %d ", &h, &w);

		cells.clear();

		printf("Case #%d: \n", k);

		for(i = 0; i <= w + 1; i++)
		{
			for(j = 0; j <= h + 1; j++)
			{
				mark[i][j] = 0;
			}
		}

		for(i = 0; i <= w + 1; i++)
		{
			map[i][0]     = 10001;
			map[i][h + 1] = 10001;
		}

		for(j = 0; j <= h + 1; j++)
		{
			map[0]    [j] = 10001;
			map[w + 1][j] = 10001;
		}

		for(j = 1; j <= h; j++)
		{
			for(i = 1; i <= w; i++)
			{
				scanf("%d", &map[i][j]);
				cells.push_back(icell(i, j, map[i][j]));
			}
		}

		cells.sort(ccell);

		v = 0;

		for(j = 1; j <= h; j++)
			for(i = 1; i <= w; i++)
				if(isSink(i, j))
					mark[i][j] = ++v;

		while(!cells.empty())
		{
			i = cells.front().x;
			j = cells.front().y;
			cells.pop_front();

			step_x.clear();
			step_y.clear();

			while(mark[i][j] == 0)
			{
				step_x.push_back(i);
				step_y.push_back(j);

				findmin(i, j);
			}

			while(!step_x.empty())
			{
				v = mark[i][j];

				mark[step_x.back()][step_y.back()] = v;

				step_x.pop_back();
				step_y.pop_back();
			}
		}

		a = 'a';

		for(j = 1; j <= h; j++)
		{
			for(i = 1; i <= w; i++)
			{
				if(mark[i][j] < 'a') reput(mark[i][j], a++, w, h);
			}
		}

		for(j = 1; j <= h; j++)
		{
			for(i = 1; i <= w; i++)
			{
				printf("%c ", mark[i][j]);
			}
			printf("\n");
		}
	}
}
