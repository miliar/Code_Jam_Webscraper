
	#include <cstdlib>
	#include <cstdio>
	#include <algorithm>

	using namespace std;

	int ansnum, nextx, nexty, n, m;
	int ans[105][105], h[105][105];

	int ok(int x, int y)
	{
		return (x >= 0 && x < n && y >= 0 && y < m);
	}

	int lowest(int x, int y)
	{
		int res = 1;
		int ch = h[x][y];
		if (ok(x - 1, y) && h[x - 1][y] < ch)
		{
			res = 0;
			ch = h[x - 1][y];
			nextx = x - 1;
			nexty = y;
		}
		if (ok(x, y - 1) && h[x][y - 1] < ch)
		{
			res = 0;
			ch = h[x][y - 1];
			nextx = x;
			nexty = y - 1;
		}
		if (ok(x, y + 1) && h[x][y + 1] < ch)
		{
			res = 0;
			ch = h[x][y + 1];
			nextx = x;
			nexty = y + 1;
		}
		if (ok(x + 1, y) && h[x + 1][y] < ch)
		{
			res = 0;
			ch = h[x + 1][y];
			nextx = x + 1;
			nexty = y;
		}
		return res;
	}

	int flow(int x, int y)
	{
		if (ans[x][y] != -1)	return ans[x][y];
		if (lowest(x, y))
		{
			ansnum ++;
			ans[x][y] = ansnum;
			return ansnum;
		}
		return ans[x][y] = flow(nextx, nexty);
	}

	void work()
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < m; j ++)
				scanf("%d", &h[i][j]);
		memset(ans, -1, sizeof(ans));
		ansnum = -1;
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < m; j ++)
				if (ans[i][j] == -1)
					ans[i][j] = flow(i, j);
		for (int i = 0; i < n; i ++)
		{
			for (int j = 0; j < m - 1; j ++)
				printf("%c ", ans[i][j] + 'a');
			printf("%c\n", ans[i][m - 1] + 'a');
		}
	}

	int main()
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
		int T;
		scanf("%d", &T);
		for (int i = 0; i < T; i ++)
		{
			printf("Case #%d:\n", i + 1);
			work();
		}
		return 0;
	}
