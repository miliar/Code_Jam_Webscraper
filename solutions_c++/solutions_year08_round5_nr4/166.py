
	#include <cstdlib>
	#include <cstdio>
	#include <algorithm>

	int f[110][100], h, w, r;

	void init()
	{
		scanf("%d%d%d", &h, &w, &r);
		memset(f, 0, sizeof(f));
		f[1][1] = 1;
		for (int i = 1; i <= r; i ++)
		{
			int x, y;
			scanf("%d%d", &x, &y);
			f[x][y] = -1;
		}
		for (int x = 1; x <= h; x ++)
			for (int y = 1; y <= w; y ++)
				if (f[x][y] > 0)
				{
					if (f[x + 1][y + 2] != -1)
						f[x + 1][y + 2] = (f[x + 1][y + 2] + f[x][y]) % 10007;
					if (f[x + 2][y + 1] != -1)
						f[x + 2][y + 1] = (f[x + 2][y + 1] + f[x][y]) % 10007;
				}
	}

	int work()
	{
		if (f[h][w] <= 0)	return 0;
		return f[h][w];
	}

	int main()
	{
		freopen("D-small-attempt0.in", "r", stdin);
		freopen("dsmall.out", "w", stdout);
		int testcase;
		scanf("%d", &testcase);
		for (int i = 1; i <= testcase; i ++)
		{
			init();
			printf("Case #%d: %d\n", i, work());
		}
		return 0;
	}
