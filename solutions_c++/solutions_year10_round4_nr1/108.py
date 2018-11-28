#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
#include <ctime>
#include <queue>

using namespace std;

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int n;
char a[400][400];
int N;
void Init()
{
	memset(a, -1, sizeof(a));
	scanf("%d\n", &n);
	N = 0;
	for (int i = 1; i <= n; i ++)
	{
		int p = 1;
		for (int j = 1; j <= n - i; j ++)
			p++;
		for (int j = 1; j <= i; j ++)
		{
			int t;
			scanf("%d", &t);
			a[i][p++] = t;
			N ++;
			p++;
		}
	}

	for (int i = n + 1; i < n + n; i ++)
	{
		int p = 1;
		for (int j = 1; j <= i - n; j ++)
			p ++;
		for (int j = 1; j <= 2 * n - i; j ++)
		{
			int t;
			scanf("%d", &t);
			a[i][p ++] = t;
			N ++;
			p++;
		}
	}
}

bool hash[400][400];

int INFINITE = 0x3f3f3f3f;
bool InRange(int x, int y)
{
	if (x <= n)
	{
		if (n - x + 1 <= y && y <= n + x - 1)
			return true;
		return false;
	}
	else
	{
		if (x - n + 1 <= y && y <= n + (n + n - x) - 1)
			return true;
		return false;
	}
}

int dist(int x1, int y1, int x2, int y2)
{
	return abs(x1 - x2) + abs(y1 - y2);
}

int Get(int x, int y)
{
	int t = max(dist(x, y, 1, n), max(dist(x, y, n, 1), max(dist(x, y, n, n + n - 1), dist(x, y, n + n - 1, n))));
	t ++;
	return (1 + t) * t / 2 + (1 + t - 1) * (t - 1) / 2;
}

int Cost(int x, int y)
{
	if (x == 2 && y == 2)
	{
		int asdf = 0;
	}
	int ret = 0;
	int maxx = -1, minx = 10000000;
	memset(hash, 0, sizeof(hash));
	for (int i = 1; i < n + n; i ++)
		for (int j = 1; j < n + n; j ++)
			if ((i != x || j != y) && a[i][j] >= 0 && a[i][j] <= 9 && !hash[i][j])
			{
				hash[i][j] = true;
				int nx, ny;
				nx = i, ny = y * 2 - j;
				maxx = max(maxx, nx);
				minx = min(minx, nx);
				if (InRange(nx, ny))
				{
					hash[nx][ny] = true;
					if (a[nx][ny] != a[i][j])
						return INFINITE;
				}
				

				nx = x * 2 - i, ny = j;
				maxx = max(maxx, nx);
				minx = min(minx, nx);
				if (InRange(nx, ny))
				{
					hash[nx][ny] = true;
					if (a[nx][ny] != a[i][j])
						return INFINITE;
				}
				

				nx = x * 2 - i, ny = y * 2 - j;
				maxx = max(maxx, nx);
				minx = min(minx, nx);
				if (InRange(nx, ny))
				{
					hash[nx][ny] = true;
					if (a[nx][ny] != a[i][j])
						return INFINITE;
				}
			}
	int asdf = 0;
	int t = Get(x, y);
	return Get(x, y) - N;
}

void Solve(int id)
{
	int ans = 0x3f3f3f3f;
	// point be the center
	for (int i = 1; i < n + n; i ++)
		for (int j = 1; j < n + n; j ++)
			if (a[i][j] >= '0' && a[i][j] <= '9')
				a[i][j] -= '0';
	for (int i = 1; i < n + n; i ++)
		for (int j = 1; j < n + n; j ++)
			ans = min(ans, Cost(i, j));
	printf("Case #%d: %d\n", id, ans);
}

int main()
{
	freopen("Elegant Diamond.in", "r", stdin);
	freopen("Elegant Diamond.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i ++)
	{
		Init();
		Solve(i);
	}
	return 0;
}
