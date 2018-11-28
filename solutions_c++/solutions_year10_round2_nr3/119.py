
	#include <cstdlib>
	#include <cstdio>
	#include <string>
	#include <algorithm>
	#include <iostream>

	using namespace std;

	int N, n, k, b, t;
	long long c[505][505];
	long long f[505][505];
	long long g[505];

	int work()
	{
		scanf("%d", &n);
		cout << g[n] << endl;
	}

	int main()
	{
		freopen("C-large.in", "r", stdin);
		freopen("C.out", "w", stdout);
		scanf("%d", &N);
		memset(c, 0, sizeof(c));
		c[0][0] = 1;
		for (int i = 1; i <= 500; i ++)
		{
			c[i][0] = 1;
			for (int j = 1; j <= i; j ++)
				c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % 100003;
		}
		for (int i = 2; i <= 500; i ++)
		{
			g[i] = 0;
			for (int j = 1; j < i; j ++)
			{
				if (j == 1)	f[i][j] = 1;
				else
				{
					f[i][j] = 0;
					for (int k = 1; k < j; k ++)
						f[i][j] = (f[i][j] + f[j][k] * c[i - j - 1][j - k - 1]) % 100003;
				}
				g[i] = (g[i] + f[i][j]) % 100003;
				//if (i <= 5)
				//	cout << f[i][j] << endl;
			}
		}
		for (int i = 1; i <= N; i ++)
		{
			printf("Case #%d: ", i);
			work();
		}
		return 0;
	}
