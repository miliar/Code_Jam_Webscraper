#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;

struct pt
{
	double x, y;
} p[100];

double dis(const pt &a, const pt &b){return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y));}
double r[100];
int n;

double solve()
{
	if (n == 1)
	{
		return r[0];
	}
	else if (n == 2)
	{
		return max(r[0], r[1]);
	}
	else
	{
		double r0 = max(r[0], (r[1] + r[2] + dis(p[1], p[2])) / 2.0);
		double r1 = max(r[1], (r[0] + r[2] + dis(p[0], p[2])) / 2.0);
		double r2 = max(r[2], (r[0] + r[1] + dis(p[0], p[1])) / 2.0);
		return min(r0, min(r1, r2));
	}
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%lf %lf %lf", &p[i].x, &p[i].y, &r[i]);
		}
		printf("Case #%d: %lf\n", t, solve());
	}
	return 0;
}
