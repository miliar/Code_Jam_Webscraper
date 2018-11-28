
	#include <cstdlib>
	#include <cstdio>
	#include <string>
	#include <algorithm>
	#include <iostream>

	using namespace std;

	int N, p;
	int n, m[1024], v;
	int f[2048][11];

	int abs(int x)
	{
		if (x > 0)	return x;
		return -x;
	}

	int sqr(int x)
	{
		return x * x;
	}

	int max(int a, int b)
	{
		if (a > b)	return a;
		return b;
	}

	int work()
	{
		scanf("%d", &p);
		n = 1;
		for (int i = 0; i < p; i ++)	n *= 2;
		for (int i = 0; i < n; i ++)
			scanf("%d", &m[i]);
		memset(f, -1, sizeof(f));
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < 11; j ++)
				if (j <= m[i])
					f[i][j] = 0;
		int last = 0;
		int cur = n;
		int delta = n / 2;
		for (int i = 0; i < p; i ++)
		{
			for (int k = 0; k < delta; k ++)
			{
				scanf("%d", &v);
				for (int u = 0; u < 11 && f[last][u] >= 0; u ++)
					for (int l = 0; l < 11 && f[last + 1][l] >= 0; l ++)
					{
//						if (u > 0 && (f[cur][u - 1] == -1 || f[cur][u - 1] < max(f[last][u], f[last + 1][l])))
//							f[cur][u - 1] = max(f[last][u], f[last + 1][l]);
//						if (f[cur][u] == -1 || f[cur][u] < max(f[last][u] + v, f[last + 1][l]))
//							f[cur][u] = max(f[last][u] + v, f[last + 1][l]);
//						if (v > 0 && (f[cur][l - 1] == -1 || f[cur][l - 1] < max(f[last][u], f[last + 1][l])))
//							f[cur][l - 1] = max(f[last][u], f[last + 1][l]);
//						if (f[cur][l] == -1 || f[cur][l] < max(f[last + 1][l] + v, f[last][u]))
//							f[cur][l] = max(f[last + 1][l] + v, f[last][u]);
						int a = u;
						if (a > l)	a = l;
						if (f[cur][a] == -1 || f[cur][a] > max(f[last][u] + f[last + 1][l], 0) + v)
							f[cur][a] = max(f[last][u] + f[last + 1][l], 0) + v;
						if (a > 0 && (f[cur][a - 1] == -1 || f[cur][a - 1] > max(f[last][u] + f[last + 1][l], 0)))
							f[cur][a - 1] = max(f[last][u] + f[last + 1][l], 0);
					}
			//	for (int i = 0; i <= 10; i ++)
			//		printf("%d%c", f[cur][i], (i == 10 ? '\n' : '\t'));
				last += 2;
				cur ++;
			}
			delta /= 2;
		}
		cur --;
		return f[cur][0];
	}

	int main()
	{
		freopen("B-large.in", "r", stdin);
		freopen("B.out", "w", stdout);
		scanf("%d", &N);
		for (int i = 1; i <= N; i ++)
			printf("Case #%d: %d\n", i, work());
		return 0;
	}
