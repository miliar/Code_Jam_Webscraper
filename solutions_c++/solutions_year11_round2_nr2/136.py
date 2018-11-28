#include <stdio.h>
#define eps (1e-9)
#define inf 10000000000000.0

double pos[1000010], x[1000010];
int main()
{
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int nt = 1; nt <= t; ++nt)
	{
		int c, d, n = 0;
		scanf("%d%d", &c, &d);
		while (c--)
		{
			int p, v;
			scanf("%d%d", &p, &v);
			while (v--)
				pos[n++] = p;
		}
		double p = 0.0, q = inf;
		for (int step = 0; step < 100; ++step)
		{
			int i;
			double k = (p + q) / 2.0;
			x[0] = pos[0] - k;
			for (i = 1; i < n; ++i)
			{
				if (x[i - 1] + d <= pos[i])
				{
					x[i] = pos[i] - k;
					if (x[i] < x[i - 1] + d)
						x[i] = x[i - 1] + d;
				}
				else
				{
					if (x[i - 1] + d > pos[i] + k)
						break;
					x[i] = x[i - 1] + d;
				}
			}
			if (i < n)
				p = k;
			else
				q = k;
		}
		printf("Case #%d: %.12lf\n", nt, (p + q) / 2.0);
	}
	return 0;
}
