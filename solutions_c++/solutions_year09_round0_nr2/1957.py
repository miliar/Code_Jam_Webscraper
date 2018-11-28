#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include "iostream"
#include "string"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"

using namespace std;

#define all(s) s.begin(), s.end()

vector<vector<int> > mp, basin;
int basin_num;

int h, w;
int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

int flow (int x, int y)
{
	int cur_basin_num = basin_num;
	int lowest_x = -1, lowest_y = -1;

	if (basin[y][x] != -1)
		return basin[y][x];

	for (int i = 0; i < 4 ; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (nx >= 0 && ny >= 0 && nx < w && ny < h &&
			mp[ny][nx] < mp[y][x] &&
			(lowest_x == -1 || mp[ny][nx] < mp[lowest_y][lowest_x]))
			lowest_x = nx, lowest_y = ny;
			
	}

	if (lowest_x == -1)
	{
		basin_num++;
	} else
		cur_basin_num = flow(lowest_x, lowest_y);

	basin[y][x] = cur_basin_num;

	return cur_basin_num;
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

int test_count;
cin >> test_count;

for (int test = 0; test < test_count ; test++)
{

	cin >> h >> w;

	mp.clear();
	basin.clear();
	basin_num = 0;

	mp.assign(h, vector<int> (w));
	basin.assign(h, vector<int> (w, -1));

	for (int i = 0; i < h ; i++)
	{
		for (int j = 0; j < w ; j++)
		{
			scanf("%d", &mp[i][j]);
		}
	}

	for (int i = 0; i < h ; i++)
	{
		for (int j = 0; j < w ; j++)
		{
			flow(j, i);
		}
	}

	vector<char> belongs(basin_num);
	char lett = 'a';
	for (int i = 0; i < h ; i++)
	{
		for (int j = 0; j < w ; j++)
		{
			int basin_id = basin[i][j];
			if (!belongs[basin_id])
				belongs[basin_id] = lett++;
		}
	}


	printf("Case #%d:\n", test + 1);

	for (int i = 0; i < h ; i++)
	{
		for (int j = 0; j < w ; j++)
		{
			int basin_id = basin[i][j];
			printf("%c ", belongs[basin_id]);
		}
		puts("");
	}

}

}