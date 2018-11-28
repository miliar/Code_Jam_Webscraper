#include <stdio.h>
#include <algorithm>
#include <math.h>

const int N = 1000005;
int p[N], v[N];
int n;
int c;

bool work(double mid)
{
	double right = p[0] - mid;
	double left;
	for (int i = 0; i < n; i++)
	{
		left = std::max(right, p[i] - mid);
		right = left + v[i] * c;
		//printf("(%lf  %d %d %lf)\n", left, v[i], c, right);
		if (right - c > p[i] + mid) return false;
	}
	return true;
}


int main ()
{
	//freopen("B-small-attempt0 (2).in", "r", stdin);
	//freopen("B-small-attempt0 (2).out", "w", stdout);
	int ca;
	scanf("%d", &ca);
	int cas = 0;
	while (ca--)
	{
		scanf("%d%d", &n, &c);
		for (int i = 0; i < n; i++)
		{
			scanf("%d%d", &p[i], &v[i]);
		}
		double ll = 0;
		double rr = 10000000;
		//if (work(2.5)) printf("YES\n");
		//printf("$$$$$");
		while (fabs(rr - ll) > 1e-7)
		{
			double mid = (ll + rr) / 2;
			if (work(mid))
			{
				//printf("%lf work\n", mid);
				rr = mid;
			}
			else
			{
				//printf("%lf not work\n", mid);
				ll = mid;
			}
		}
		printf("Case #%d: ", ++cas);
		printf("%lg\n", ll);
	}
	return 0;
}
