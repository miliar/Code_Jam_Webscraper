#include <cstdio>
using namespace std;

int t;
int c, d;
int p[210];
int v[210];
double a, b, r;

const double eps = 1e-7; 

bool ok(double a)
{
	double g, h;
	int i, j;
	
	g = p[0] - a;
	for (i = 0; i < c; ++i)
		for (j = 0; j < v[i]; ++j)
		{
			if (g > p[i] + a)
				return false;
			if (g < p[i] - a)
				g = p[i] - a;
			g += d;
		}
	return true;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int i, j, k;

	scanf("%d", &t);
	for (i = 1; i <= t; ++i)
	{
		scanf("%d%d", &c, &d);
		for (j = 0; j < c; ++j)
			scanf("%d%d", p + j, v + j);
		a = 0;
		b = (1000000 * 1000000LL);
		while (b - a > eps)
		{
			r = (a + b) / 2;
			if (ok(r))
				b = r;
			else
				a = r;
		}
		if (ok(a))
			r = a;
		else
			r = b;
		printf("Case #%d: %.6lf\n", i, r);
	}
	return 0;
}