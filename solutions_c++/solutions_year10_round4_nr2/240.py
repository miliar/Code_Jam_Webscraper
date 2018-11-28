#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;

int p;
int m[1024];
int cost[10][1024];

void Load()
{
	scanf("%d", &p);
	int i;
	for (i = 0; i < (1 << p); i++) scanf("%d", &m[i]);
	for (i = p - 1; i >= 0; i--)
	{
		int j;
		for (j = 0; j < (1 << i); j++) scanf("%d", &cost[i][j]);
	}
}

int mm[11][1024];
int res[11][1024][11];

int Count(int i, int j, int m)
{
	if (res[i][j][m] != -1) return res[i][j][m];
	if (i == p)
	{
		res[i][j][m] = 0;
		return 0;
	}
	res[i][j][m] = 2100000000;
	// can we throw it away
	if (m < mm[i][j])
	{
		res[i][j][m] = min(res[i][j][m], Count(i + 1, 2 * j, m + 1) + Count(i + 1, 2 * j + 1, m + 1));
	}
	res[i][j][m] = min(res[i][j][m], Count(i + 1, 2 * j, m) + Count(i + 1, 2 * j + 1, m) + cost[i][j]);
	return res[i][j][m];
}

void Solve()
{
	int i, j;
	for (i = 0; i < (1 << p); i++) mm[p][i] = m[i];
	for (i = p - 1; i >= 0; i--)
	{
		for (j = 0; j < (1 << i); j++) mm[i][j] = min(mm[i + 1][2 * j], mm[i + 1][2 * j + 1]);
	}
	memset(res, 0xFF, sizeof(res));
	cout << Count(0, 0, 0);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}