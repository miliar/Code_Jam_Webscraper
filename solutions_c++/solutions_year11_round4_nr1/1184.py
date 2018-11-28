#include <cstdio>
using namespace std;

int T;
double x, s, r, t, n;
int b, e, k;
int a[110];
double ans;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i, j;
	double p;

	scanf("%d", &T);
	for (i = 1; i <= T; ++i)
	{
		scanf("%lf%lf%lf%lf%lf", &x, &s, &r, &t, &n);
		for (k = 1; k <= 100; ++k)
			a[k] = 0;
		a[0] = x;
		for (j = 0; j < n; ++j)
		{
			scanf("%d%d%d", &b, &e, &k);
			a[k] += e - b;
			a[0] -= e - b;
		}
		ans = 0;
		for (k = 0; k <= 100; ++k)
		{
			if (t > 0)
			{
				p = a[k] * 1.0 / (k + r);
				if (p > t)
				{
					ans += t + (a[k] - t * (k + r)) * 1.0 / (k + s);
					t = 0;
				}
				else
				{
					ans += p;
					t -= p;
				}
			}
			else
			{
				ans += a[k] * 1.0 / (k + s);
			}
		}
		printf("Case #%d: %lf\n", i, ans);
	}
	return 0;
}