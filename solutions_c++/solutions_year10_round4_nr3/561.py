
	#include <cstdlib>
	#include <cstdio>
	#include <string>
	#include <algorithm>
	#include <iostream>

	using namespace std;

	int N, p;
	int aa[105][105], bb[105][105];

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
		memset(aa, 0, sizeof(aa));
		memset(bb, 0, sizeof(bb));
		for (int i = 0; i < p; i ++)
		{
			int x1, x2, y1, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; x ++)
				for (int y = y1; y <= y2; y ++)
					aa[x][y] = 1;
		}
		for (int t = 0; 1; t ++)
		{
			int flag = 0;
			for (int i = 0; i <= 100; i ++)
				for (int j = 0; j <= 100; j ++)
					if (aa[i][j] == 1)
						flag = 1;
			if (flag == 0)	return t;
			for (int i = 1; i <= 100; i ++)
				for (int j = 1; j <= 100; j ++)
				{
					bb[i][j] = aa[i][j];
					if (aa[i - 1][j] == 0 && aa[i][j - 1] == 0)
						bb[i][j] = 0;
					if (aa[i - 1][j] == 1 && aa[i][j - 1] == 1)
						bb[i][j] = 1;
				}
			for (int i = 1; i <= 100; i ++)
				for (int j = 1; j <= 100; j ++)
					aa[i][j] = bb[i][j];
		}
	}

	int main()
	{
		freopen("C-small-attempt0.in", "r", stdin);
		freopen("C.out", "w", stdout);
		scanf("%d", &N);
		for (int i = 1; i <= N; i ++)
			printf("Case #%d: %d\n", i, work());
		return 0;
	}
