
	#include <cstdlib>
	#include <cstdio>
	#include <algorithm>

	using namespace std;

	int n, s, p, need[40][20], noneed[40][20], f[1000][1000], u[1000];

	int abs(int x)
	{
		if (x > 0)	return x;
		return -x;
	}

	void prework()
	{
		for (int i = 0; i <= 10; i ++)
			for (int j = i; j <= 10; j ++)
				for (int k = j; k <= 10; k ++)
					if (k - i <= 2)
					{
						if (k - i <= 1)	noneed[i + j + k][k] = 1;
						else	need[i + j + k][k] = 1;
					}
		for (int sum = 0; sum <= 30; sum ++)
		{
			for (int j = 10; j > 0; j --)
			{
				if (noneed[sum][j] == 1)	noneed[sum][j - 1] = 1;
				if (need[sum][j] == 1)	need[sum][j - 1] = 1;
			}
		}
	}

	int work()
	{
		scanf("%d%d%d", &n, &s, &p);
		for (int i = 1; i <= n; i ++)
			scanf("%d", &u[i]);
		memset(f, -1, sizeof(f));
		f[0][0] = 0;
		for (int i = 1; i <= n; i ++)
			for (int j = 0; j <= s; j ++)
			{
				if (f[i - 1][j] >= 0 && f[i][j] < f[i - 1][j])	f[i][j] = f[i - 1][j];
				if (j > 0 && f[i - 1][j - 1] >= 0 && u[i] >= 2 && u[i] <= 28 && f[i][j] < f[i - 1][j - 1])	f[i][j] = f[i - 1][j - 1];
				if (noneed[u[i]][p] == 1)
					if (f[i - 1][j] != -1 && f[i][j] < f[i - 1][j] + 1)
						f[i][j] = f[i - 1][j] + 1;
				if (j > 0 && need[u[i]][p] == 1)
					if (f[i - 1][j - 1] != -1 && f[i][j] < f[i - 1][j - 1] + 1)
						f[i][j] = f[i - 1][j - 1] + 1;
			}
		return f[n][s];
	}

	int main()
	{
		freopen("b.in", "r", stdin);
		freopen("b.out", "w", stdout);
		prework();
		int t;
		scanf("%d", &t);
		for (int i = 1; i <= t; i ++)
			printf("Case #%d: %d\n", i, work());
		return 0;
	}
