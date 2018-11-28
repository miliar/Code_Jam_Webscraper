
	#include <cstdlib>
	#include <cstdio>
	#include <algorithm>

	using namespace std;

	int p[8];
	int friends[2000005][7], cnt[2000005];

	void solve(int s, int e, int pp)
	{
		for (int i = s; i <= e; i ++)
		{
			int u = i;
			for (int j = 0; j < pp - 1; j ++)
			{
				u = u / 10 + u % 10 * p[pp];
				if (u < i && u >= p[pp])
				{
					int flag = 1;
					for (int k = 0; k < cnt[i]; k ++)
						if (friends[i][k] == u)
							flag = 0;
					if (flag == 1)
					{
						friends[i][cnt[i]] = u;
						cnt[i] ++;
					}
				}
			}
		}
	}

	void prework()
	{
		memset(cnt, 0, sizeof(cnt));
		p[2] = 10;
		p[3] = 100;
		p[4] = 1000;
		p[5] = 10000;
		p[6] = 100000;
		p[7] = 1000000;
		solve(10, 99, 2);
		solve(100, 999, 3);
		solve(1000, 9999, 4);
		solve(10000, 99999, 5);
		solve(100000, 999999, 6);
		solve(1000000, 2000000, 7);
	}

	int work()
	{
		int a, b;
		scanf("%d%d", &a, &b);
		int sum = 0;
		for (int i = a + 1; i <= b; i ++)
		{
			for (int j = 0; j < cnt[i]; j ++)
				if (friends[i][j] >= a)
					sum ++;
			//if (i >= 2100 && i <= 2200)//(i % 100 == 0)
			//	printf("%d: %d\n", i, sum);
		}
		return sum;
	}

	int main()
	{
		freopen("c.in", "r", stdin);
		freopen("c.out", "w", stdout);
		prework();
		int t;
		scanf("%d", &t);
		for (int i = 1; i <= t; i ++)
			printf("Case #%d: %d\n", i, work());
		return 0;
	}
