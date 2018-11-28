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

int R;
int a[101][101];
void Init()
{
	memset(a, 0, sizeof(a));
	scanf("%d", &R);
	for (int i = 1; i <= R; i ++)
	{
		int x1, y1, x2, y2;
		scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
		if (x1 > x2)
			swap(x1, x2);
		if (y1 > y2)
			swap(y1, y2);
		for (int j = x1; j <= x2; j ++)
			for (int k = y1; k <= y2; k ++)
				a[j][k] = 1;
	}
}

int b[101][101];
int c[101][101];
void Solve(int id)
{
	int N = 100;
	int ans = 0;
	while (true)
	{
		int cnt = 0;
		for (int i = 1; i <= N; i ++)
			for (int j = 1; j <= N; j ++)
				cnt += a[i][j];
		if (!cnt) break;
		ans ++;
		memset(b, 0, sizeof(b));
		for (int i = 1; i <= N; i ++)
			for (int j = 1; j <= N; j ++)
				if (!a[i][j] && a[i - 1][j] && a[i][j - 1])
					b[i][j] = 1;
		memset(c, 0, sizeof(c));
		for (int i = 1; i <= N; i ++)
			for (int j = 1; j <= N; j ++)
				if (a[i][j] && !a[i - 1][j] && !a[i][j - 1])
					c[i][j] = 1;
		for (int i = 1; i <= N; i ++)
			for (int j = 1; j <= N; j ++)
				a[i][j] += b[i][j] - c[i][j];
	}
	printf("Case #%d: %d\n", id, ans);
}

int main()
{
	freopen("bacteria.in", "r", stdin);
	freopen("bacteria.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i ++)
	{
		Init();
		Solve(i);
	}
	return 0;
}
