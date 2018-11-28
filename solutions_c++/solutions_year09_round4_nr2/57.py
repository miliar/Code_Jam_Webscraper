#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>


using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

#define cin fin
#define cout fout

int n, m, t;
int cases;
char map[64][64];
int best[64][64][2000];
int hash[64][64];
int tot;

int ans;

bool down(int &x, int &y)
{
	int c = 0;
	while (x+1 < n && map[x+1][y] == '.')
	{
		x++;
		c++;
	}
	if (c > t) return false;
	return true;
}

void dfs(int x, int y, int cost, int stat)
{
	int i, j;
	bool ok;
	int rightmost, leftmost;

	if (cost > ans && ans != -1) return;

	if (x >= n-1)
	{
		if (ans == -1) ans = cost;
		if (cost < ans) ans = cost;

		return;
	}

	if (best[x][y][stat] <= cost) return;
	best[x][y][stat] = cost;

	i = x; j = y;
	while (j+1 < m && map[i][j+1] == '.' && map[i+1][j+1] == '#') j++;

	rightmost = j;
	if (j+1 < m && map[i][j+1] == '.' && map[i+1][j+1] == '.')
	{
		j++;
		ok = down(i, j);
		if (ok) dfs(i, j, cost, 0);
	}

	i = x; j = y;
	while (j-1 >= 0 && map[i][j-1] == '.' && map[i+1][j-1] == '#') j--;

	leftmost = j;
	if (j-1 >= 0 && map[i][j-1] == '.' && map[i+1][j-1] == '.')
	{
		j--;
		ok = down(i,j);
		if (ok) dfs(i,j, cost, 0);
	}

	for (int ii = leftmost; ii <= rightmost; ii++)
		for (int jj = ii; jj <= rightmost; jj++)
			if (ii != leftmost || jj != rightmost)
			{
				for (int k = ii; k <= jj; k++)
					map[x+1][k] = '.';

				if (ii > leftmost)
				{
					i = x; j = ii;
					if (down(i,j) == true)
						dfs(i, j, cost + (jj - ii + 1), hash[ii][jj]);
				}

				if (jj < rightmost)
				{
					i = x; j = jj;
					if (down(i,j) == true)
						dfs(i, j, cost + (jj - ii + 1), hash[ii][jj]);
				}

				for (int k = ii; k <= jj; k++)
					map[x+1][k] = '#';
			}
}

int main()
{
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; i++)
	{
		cin >> n >> m >> t;
		for (int x = 0; x < n; x++)
			cin >> map[x];

		ans = -1;
		memset(best, 0x7f, sizeof(best));

		tot = 1;
		for (int j = 0; j < m; j++)
			for (int k = j; k < m; k++)
				hash[j][k] = tot++;

		dfs(0, 0, 0, 0);

		printf("Case #%d\n", i);

		cout << "Case #" << i << ": ";
		
		if (ans == -1)
			cout << "No" << endl;
		else
			cout << "Yes " << ans << endl;
	}

	return 0;
}