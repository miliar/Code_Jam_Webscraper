// Solution by Maxim Kulikov <maxim.coolikov@gmail.com>
// Compiled with Visual Studio 2005 Express Edition

#include <cstdio>
#include <fstream>
#include <iostream>

using namespace std;

int h, w;
int map[128][128];
char ans[128][128];
char cur;
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

inline bool good(int x, int y)
{
	return 0 <= x && x < h && 0 <= y && y < w;
}

char go (int x, int y)
{
	if (!ans[x][y])
	{
		int min = map[x][y];
		int ind = -1;
		for (int i = 0; i < 4; ++i)
			if (good (x + dx[i], y + dy[i]) && map[x + dx[i]][y + dy[i]] < min)
			{
				min = map[x + dx[i]][y + dy[i]];
				ind = i;
			}
		if (ind == -1)
			ans[x][y] = cur++;
		else
			ans[x][y] = go (x + dx[ind], y + dy[ind]);
	}
	return ans[x][y];
}

int main ()
{
	freopen ("B-large.in", "rt", stdin);
	freopen ("B-large.out", "wt", stdout);

	int test_n;
	cin >> test_n;
	for (int test = 1; test <= test_n; ++test)
	{
		cout << "Case #" << test << ":" << endl;

		cin >> h >> w;
		memset (ans, 0, sizeof (ans));
		cur = 'a';
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j)
				cin >> map[i][j];
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j)
				go (i, j);
		for (int i = 0; i < h; ++i)
		{
			for (int j = 0; j < w; ++j)
				cout << ans[i][j] << ' ';
			cout << endl;
		}
	}

	return 0;
}