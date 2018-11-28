#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

const double eps = 1e-6;
const int MAXN = 10000000;
double p[MAXN];
int v[MAXN];

bool check(double mid, int c, double d)
{
	double pos = p[0] - mid;
	for (int i = 0; i < c; i++)
	{
		int temp = v[i];
		if (i == 0)
			temp--;
		for (int j = 0; j < temp; j++)
		{
			if (fabs((pos + d) - p[i]) <= mid)
			{
				pos += d;
			}
			else
			{
				if ((pos + d) < p[i])
					pos = p[i] - mid;
				else
					return false;
			}
		}
	}
	return true;
}
int main()
{
	int t, c;
	double d;
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d%lf", &c, &d);
		for (int j = 0; j < c; j++)
			scanf("%lf%d", &p[j], &v[j]);
		double l = 0, r = 10000000, mid, ans = 10000000;
		while (l + eps <= r)
		{
			mid = (l + r) / 2;
			if (check(mid, c, d))
			{
				if (ans > mid)
					ans = mid;
				r = mid;
			}
			else
			{
				l = mid;
			}
		}
		printf("Case #%d: %lf\n", i, ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}