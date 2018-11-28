#include<stdio.h>
#include<math.h>
#include<algorithm>
#define eps 1e-8
using namespace std;

int c, n;
double p[1111111];
double d;

bool ok(double x)
{
	double last = -1e100, newp;
	for (int i = 0; i < n; i++)
	{
		newp = max(last + d, p[i] - x);
		if (fabs(newp - p[i]) > x + eps)return false;
		last = newp;
	}
	return true;
}

double solve()
{
	double low = 0.0, high = d * 2e6, mid;
    while (low + 1e-8 < high)
	{
		mid = (low+high)/2;
        if (low+1e-8>=mid) break;
        if (mid+1e-8>=high) break;
        if (ok(mid))
        	high = mid;
        else
			low = mid;
	}
	return (low + high) / 2.0;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++)
	{
		double tmpp;
		int cnt;
		
		n = 0;
		scanf("%d %lf", &c, &d);
		for (int i = 0; i < c; i++)
		{
			scanf("%lf %d", &tmpp, &cnt);
			while (cnt--)
			{
				p[n++] = tmpp;
			}
		}
		printf("Case #%d: %.10f\n", t, solve());
	}
	return 0;
}
