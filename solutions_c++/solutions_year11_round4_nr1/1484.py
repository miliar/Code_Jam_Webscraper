#include <stdio.h>
#include <algorithm>

struct C
{
	double dis, w;
}way[1001];

double x, s, r, t;

int cmp(struct C a, struct C b)
{
	return a.w + s < b.w + s;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int i = 1; i <= test; ++i)
	{
		memset(way, 0, sizeof (way));
		int n;
		scanf("%lf %lf %lf %lf %d", &x, &s, &r, &t, &n);
		double left = x;
		for (int j = 0; j < n; ++j)
		{
			double b, e;
			scanf("%lf %lf %lf", &b, &e, &way[j].w);
			way[j].dis = e - b;
			left -= way[j].dis;
		}
		way[n].dis = left;
		way[n].w = 0;
		double time = 0.0;
		std::sort(way, way + n + 1, cmp);
		for (int j = 0; j <= n; ++j)
		{
			double tt = way[j].dis / (way[j].w + r);
			if (t == 0)
			{
				time += (way[j].dis) / (way[j].w + s);
				continue;
			}
			if (tt <= t)
			{
				t -= tt;
				time += tt;
			}
			else
			{
				time += t;
				time += (way[j].dis - (way[j].w + r) * t) / (way[j].w + s);
				t = 0;
			}
		}
		printf("Case #%d: %.9lf\n", i, time);
	}
	return 0;
}