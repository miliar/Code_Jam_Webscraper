#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:65000000")
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <cmath>

using namespace std;
const string FILENAME = "awe";
const int BIG = 99999;

int alt[200][200];
char field[200][200];
int n, m;

int di[] = {-1, 0, 0, 1};
int dj[] = {0, -1, 1, 0};

pair<int, int> getNeib(int i, int j)
{
	int ri = -1, rj = -1;

	for (int k = 0; k < 4; ++k)
	{
		int ni = i + di[k], nj = j + dj[k];
		if (ni <= 0 || nj <= 0 || ni > n || nj > m)
			continue;
		if (ri == -1|| alt[ri][rj] > alt[ni][nj])
		{
			ri = ni;
			rj = nj;
		}
	}
	if (alt[ri][rj] >= alt[i][j])
		return make_pair(-1, -1);
	else
		return make_pair(ri, rj);
}

char lastFree;

char go(int i, int j)
{
	if (field[i][j] != -1)
		return field[i][j];
	pair<int, int> next = getNeib(i, j);
	if (next.first == -1)
	{
		field[i][j] = lastFree;
		lastFree++;
		
	}
	else
	{
		field[i][j] = go(next.first, next.second);
	}
	return field[i][j];
}

void solve()
{
	lastFree = 'a';
	memset(field, -1, sizeof field);
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
		{
			go(i, j);
		}
}

int main()
{
	freopen((FILENAME + ".in").c_str(), "r", stdin);
	freopen((FILENAME + ".out").c_str(), "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		scanf("%d%d", &n, &m);
		for (int j = 1; j <= n; ++j)
		{
			for (int k = 1; k <= m; ++k)
				scanf("%d", &alt[j][k]);
		}

		solve();
		
		printf("Case #%d:\n", i + 1);
		for (int j = 1; j <= n; ++j)
		{
			for (int k = 1; k <= m; ++k)
				printf("%c ", field[j][k]);
			putchar('\n');
		}
	}
	return 0;
}