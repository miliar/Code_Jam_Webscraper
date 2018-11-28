#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const double Pi = 3.14159265358979323846264338327950288;
const double Eps = 1e-8;
int N, M;

double Calc(double r1, double r2, double d)
{
	if (r1 > r2)
		return Calc(r2, r1, d);
	if (fabs(r1) < Eps)
		return Pi * r2 * r2;
	if (fabs(d) < Eps)
		return Pi * r2 * r2;
	if (d + Eps >= r1 + r2)
		return Pi * (r1 * r1 + r2 * r2);
	if (d <= r2 - r1 + Eps)
		return Pi * r2 * r2;
	double x = (r1 * r1 - r2 * r2 + d * d) / (d * 2.0);
	double y = sqrt(r1 * r1 - x * x);
	double Ans = Pi * (r1 * r1 + r2 * r2);
	Ans -= atan2(y, x) * r1 * r1 - x * y;
	Ans -= atan2(y, d - x) * r2 * r2 - (d - x) * y;
	return Ans;
}

void Work()
{
	scanf("%d%d", &N, &M);
	double x1, y1, x2, y2;
	scanf("%lf%lf%lf%lf", &x1, &y1, &x2, &y2);
	double Dist = sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
	while (M --)
	{
		double x, y;
		scanf("%lf%lf", &x, &y);
		double r1 = sqrt((x1 - x) * (x1 - x) + (y1 - y) * (y1 - y));
		double r2 = sqrt((x - x2) * (x - x2) + (y - y2) * (y - y2));
		printf(" %.8lf", Pi * (r1 * r1 + r2 * r2) - Calc(r1, r2, Dist));
	}
}

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
	{
		printf("Case #%d:", Case);
		Work();
		printf("\n");
	}
	return 0;
}
