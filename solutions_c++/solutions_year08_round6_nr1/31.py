
	#include <cstdio>
	#include <cstdlib>
	#include <algorithm>

	int n, m, h[2000], w[2000], b[2000];

	void work()
	{
		int lowh = 100001;
		int highh = 0;
		int loww = 100001;
		int highw = 0;
		scanf("%d", &n);
		for (int i = 1; i <= n; i ++)
		{
			scanf("%d%d", &h[i], &w[i]);
			char c;
			while (c = getchar(), c != 'B' && c != 'N');
			if (c == 'B')	b[i] = 1;
			else	b[i] = 0;
			while (c = getchar(), c != '\n');
			if (b[i] == 1)
			{
				if (h[i] < lowh)	lowh = h[i];
				if (h[i] > highh)	highh = h[i];
				if (w[i] < loww)	loww = w[i];
				if (w[i] > highw)	highw = w[i];
			}
		}
		int lefth = 0, leftw = 0, righth = 100001, rightw = 100001;
		for (int i = 1; i <= n; i ++)
			if (b[i] == 0)
			{
				if (h[i] >= lowh && h[i] <= highh)
				{
					if (w[i] > highw && rightw > w[i])	rightw = w[i];
					if (w[i] < loww && leftw < w[i])	leftw = w[i];
				}
				if (w[i] >= loww && w[i] <= highw)
				{
					if (h[i] > highh && righth > h[i])	righth = h[i];
					if (h[i] < lowh && lefth < h[i])	lefth = h[i];
				}
			}
		//printf("%d %d %d %d\n", lowh, highh, loww, highw);
		//printf("%d %d %d %d\n", lefth, righth, leftw, rightw);
		scanf("%d", &m);
		int p, q;
		if (lowh > highh)
		{
			for (int i = 1; i <= m; i ++)
			{
				scanf("%d%d", &p, &q);
				int oo = 1;
				for (int j = 1; j <= n; j ++)
					if (p == h[i] && q == w[i])
					{
						oo = 0;
						break;
					}
				if (oo)
					printf("UNKNOWN\n");
				else
					printf("NOT BIRD\n");
			}
			return;
		}
		for (int i = 1; i <= m; i ++)
		{
			scanf("%d%d", &p, &q);
			if (p >= lowh && p <= highh && q >= loww && q <= highw)	printf("BIRD\n");
			else
				if (p <= lefth || p >= righth || q <= leftw || q >= rightw)	printf("NOT BIRD\n");
			else
			{
				int oo = 1;
				for (int j = 1; j <= n; j ++)
					if (b[j] == 0)
					{
						if (h[i] < lowh && w[i] < loww)
						{
							if (p <= h[i] && q <= w[i])
							{
								oo = 0;
								break;
							}
						}
						if (h[i] < lowh && w[i] > highw)
						{
							if (p <= h[i] && q >= w[i])
							{
								oo = 0;
								break;
							}
						}
						if (h[i] > highh && w[i] < loww)
						{
							if (p >= h[i] && q <= w[i])
							{
								oo = 0;
								break;
							}
						}
						if (h[i] > highh && w[i] > highw)
						{
							if (p >= h[i] && q >= w[i])
							{
								oo = 0;
								break;
							}
						}
					}
				if (oo)
					printf("UNKNOWN\n");
				else
					printf("NOT BIRD\n");
			}
		}
	}

	int main(int argc, char *argv[])
	{
		int c;
		freopen("a.in", "r", stdin);
		freopen("a.out", "w", stdout);
		scanf("%d", &c);
		for (int testnum = 1; testnum <= c; testnum ++)
		{
			printf("Case #%d:\n", testnum);
			work();
		}
		return 0;
	}
