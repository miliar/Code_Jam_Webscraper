
	#include <cstdlib>
	#include <cstdio>
	#include <algorithm>
	#include <math.h>

	using namespace std;

	int x[10], y[10], r[10];

	double dis(int u, int v)
	{
		return sqrt((x[u] - x[v]) * (x[u] - x[v]) + (y[u] - y[v]) * (y[u] - y[v]));
	}

	double check(int u, int v, int w)
	{
		double t = (dis(u, v) + r[u] + r[v]) / 2;
		if (t < r[w])	t = r[w];
		return t;
	}

	double work()
	{
		double ans = 100000;
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i ++)
			scanf("%d%d%d", &x[i], &y[i], &r[i]);
		if (n == 1)
			return r[0];
		if (n == 2)
		{
			if (r[0] < r[1])	return	r[1];
			return r[0];
		}
//		if (n == 2)
//			return (dis(0, 1) + r[0] + r[1]) / 2;
		double u = check(0, 1, 2);
		ans <?= u;
		u = check(0, 2, 1);
		ans <?= u;
		u = check(1, 2, 0);
		ans <?= u;
		return ans;
	}

	int main()
	{
		freopen("d.in", "r", stdin);
		freopen("d.out", "w", stdout);
		int t;
		scanf("%d", &t);
		for (int i = 1; i <= t; i ++)
			printf("Case #%d: %lf\n", i, work());
		return 0;
	}
