#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

#define sqr(x) ((x)*(x))

const double eps = 1e-10;
const double pi = acos(0.0) * 2.0;

double f, R, t, r, g;

struct point
{
	double x, y;
};

inline int insideCircle(const point& a, double r)
{
	return (sqr(a.x) + sqr(a.y) < sqr(r));
}

void intersection_x(point& o, double r)
{
	double x;
	x = sqrt(sqr(r) - sqr(o.y));
	o.x = min(o.x, x);
}

double integral(double y, double x1, double x2, double r)
{
	double a1 = acos(x1 / r);
	double a2 = acos(x2 / r);
	return (-sqr(r) / 2) * ( (a2 - 0.5 * sin(2 * a2)) - (a1 - 0.5 * sin(2 * a1)) ) - y * (x2 - x1);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int rr;
	int cs = 0;
	scanf("%d", &rr);
	while(rr--)
	{
		int i, j;
		point o, o1, o2, o3;

		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		printf("Case #%d: ", ++cs);
		if(g <= f * 2)
		{
			printf("1.000000\n");
			continue;
		}

		double p = 0.0;
		t += f;
		for(i = 0; ; ++i)
		{
			o.x = r + (g + r + r) * (double)i + f;
			if(o.x >= R - t) break;
			for(j = 0; ; ++j)
			{
				o.y = r + (g + r + r) * (double)j + f;
				if(!insideCircle(o, R - t)) break;

				double d = g - 2 * f;
				o1.y = o.y; o1.x = o.x + d;
				o2 = o1; o2.y += d;
				o3 = o2; o3.x -= d;

				if(insideCircle(o3, R - t) && insideCircle(o2, R - t))
				{
					p += sqr(d);
				}
				else if(!insideCircle(o3, R - t))
				{
					intersection_x(o1, R - t);
					p += integral(o.y, o.x, o1.x, R - t);
				}
				else
				{
					intersection_x(o1, R - t);
					intersection_x(o2, R - t);
					p += d * (o2.x - o3.x);
					p += integral(o.y, o2.x, o1.x, R - t);
				}
			}
		}
		p = 1 - ((p * 4) / (pi * sqr(R)));
		printf("%.6lf\n", p);
	}
	return 0;
}