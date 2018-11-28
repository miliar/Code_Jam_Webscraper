
	#include <cstdlib>
	#include <cstdio>
	#include <algorithm>

	int n, m, s;
	char map[15][15];
	int f[2000], list[2000], total, value[2000], g[2000];
	int e[2000][2000];

	void init()
	{
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i ++)
			for (int j = 1; j <= m; j ++)
			{
				map[i][j] = getchar();
				while (map[i][j] != '.' && map[i][j] != 'x')	map[i][j] = getchar();
			}
		s = 1;
		for (int i = 1; i <= m; i ++)
			s *= 2;
		s --;
	}

	int ok(int x)
	{
		int last = x % 2;
		x /= 2;
		for (int i = 1; i <= m; i ++)
		{
			if (last == 1 && (x % 2 == 1))
				return 0;
			last = x % 2;
			x /= 2;
		}
		return 1;
	}

	int check(int x, int y)
	{
		int a[15], b[15];
		for (int i = 1; i <= m; i ++)
		{
			a[i] = x % 2;
			b[i] = y % 2;
			x /= 2;
			y /= 2;
		}
		for (int i = 2; i <= m - 1; i ++)
			if (b[i] == 1 && (a[i - 1] == 1 || a[i + 1] == 1))
				return 0;
		if (b[1] == 1 && a[2] == 1)	return 0;
		if (b[m] == 1 && a[m - 1] == 1)	return 0;
		return 1;
	}

	int ccc(int c, int v)
	{
		for (int i = 1; i <= m; i ++)
		{
			if (v % 2 == 1 && map[c][i] == 'x')
				return 0;
			v /= 2;
		}
		return 1;
	}

	int work()
	{
		int ans;
		total = 0;
		for (int i = 0; i <= s; i ++)
			if (ok(i))
			{
				total ++;
				list[total] = i;
				int j = i;
				value[total] = 0;
				for (; j > 0; j /= 2)
					if (j % 2 == 1)
						value[total] ++;
			}
		memset(e, 0, sizeof(e));
		for (int i = 1; i <= total; i ++)
			for (int j = 1; j <= total; j ++)
				if (check(list[i], list[j]))
					e[i][j] = 1;
		memset(f, -1, sizeof(f));
		f[1] = 0;
		for (int i = 1; i <= n; i ++)
		{
			memset(g, -1, sizeof(g));
			for (int j = 1; j <= total; j ++)
				if (ccc(i, list[j]))
					for (int k = 1; k <= total; k ++)
						if (e[k][j] && f[k] >= 0)
							if (g[j] < f[k] + value[j])
								g[j] = f[k] + value[j];
			for (int j = 1; j <= total; j ++)
				f[j] = g[j];
		}
		ans = 0;
		for (int i = 1; i <= total; i ++)
			if (f[i] > ans)
				ans = f[i];
		return ans;
	}

	int main()
	{
		freopen("C-small-attempt0.in", "r", stdin);
		freopen("c.out", "w", stdout);
		int testcase;
		scanf("%d", &testcase);
		for (int i = 1; i <= testcase; i ++)
		{
			init();
			printf("Case #%d: %d\n", i, work());
		}
		return 0;
	}
