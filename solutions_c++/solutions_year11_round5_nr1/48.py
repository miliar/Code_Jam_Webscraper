#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#include <cmath>
#define clr(a) memset(a, 0, sizeof(a))

typedef long long ll;
typedef std::pair<int, int> pii;
#define DEBUG 1

void dbg(const char * fmt, ...)
{
#if DEBUG
	va_list args;
	va_start(args, fmt);
	vfprintf(stdout, fmt, args);
	va_end(args);
#endif
}


double x[2][200];
double y[2][200];

double l[300];
double h[300];

double all_x[300];


double find(int t, double pos)
{
	int i = 0;
	while(x[t][i] < pos + 1e-9)
		i++;
	i--;
	double ans = y[t][i] + (y[t][i+1] - y[t][i]) / (x[t][i+1] - x[t][i]) * (pos - x[t][i]);
	//printf("find (%d, %.5lf) = %.5lf\n", t, pos, ans);
	return ans;
}

int n;

double _sqrt(double x)
{
	if (x < -1e-9)
		throw 42;
	if (x < 0)
		return 0;
	return sqrt(x);
}

void solve(int test_case)
{
	printf("Case #%d:\n", test_case);
	int w,u,d,g;
	scanf("%d%d%d%d", &w, &d, &u, &g);
	x[0][d] = x[1][u] = 1e9;
	for(int i = 0; i < d; i++)
	{
		scanf("%lf%lf", &x[0][i], &y[0][i]);
		all_x[i] = x[0][i];
	}
	for(int i = 0; i < u; i++)
	{
		scanf("%lf%lf", &x[1][i], &y[1][i]);
		all_x[d+i] = x[1][i];
	}
	std::sort(all_x, all_x + d + u);
	n = std::unique(all_x, all_x + d + u) - all_x;
	double last = 0;
	for(int i = 0; i < n; i++)
	{
		l[i] = all_x[i] - last;
		last = all_x[i];
		h[i] = find(1, all_x[i]) - find(0, all_x[i]);
	}
	double s = 0, curs = 0;
	for(int i = 1; i < n; i++)
	{
		s += l[i] * (h[i] + h[i-1]);
	}
/*	for(int i = 0; i < n; i++)
		printf("%.5lf ", l[i]);
	printf("\n");
	for(int i = 0; i < n; i++)
		printf("%.5lf ", h[i]);
	printf("\n");*/
	double x = 0;
//	printf("s = %.5lf\n", s);
	curs = s / g;
	for(int i = 1; i < n; i++)
	{
//		printf("i = %d\n", i);
		if (l[i] < 1e-9)
			continue;
		if ((h[i] + h[i-1]) * l[i] < curs)
		{
			curs -= (h[i] + h[i-1]) * l[i];
			x += l[i];
		}
		else
		{
			double a = (h[i] - h[i-1])/2./l[i], b = h[i-1], c = -curs / 2;
			double x0;
			if (fabs(a) < 1e-9)
				x0 =  -c/b;
			else
				x0 = (-b + _sqrt(b*b-4*a*c)) / 2.0 / a;
//			printf("x0 = %.5lf\n", x0);
			if (x0 > l[i] + 1e-9 || x0 < -1e-9)
				throw 42;
			h[i-1] += (h[i] - h[i-1]) * x0 / l[i];
			l[i] -= x0;
			x += x0;
			printf("%.10lf\n", x);
			curs = s / g;
			g--;
			i--;
		}
		if (g == 1)
			break;
	}
	if (g != 1)
		throw 42;
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
