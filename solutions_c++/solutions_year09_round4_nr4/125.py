#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <cmath>
#define clr(a) memset(a, 0, sizeof(a))

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

double sqr(double x)
{
	return x * x;
}

class point
{
public:
	double x,y,d;
	double dist(const point &p) const
	{
		return (sqrt(sqr(x-p.x)+sqr(y-p.y))+d+p.d)/2;
	}
	void scan()
	{
		scanf("%lf%lf%lf", &x, &y, &d);
	}
};

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	point a,b,c;
	int n;
	scanf("%d", &n);
	if (n == 3)
	{
		a.scan();
		b.scan();
		c.scan();
		double ans = 1e100;
		ans = std::min(ans, std::max(a.dist(b),c.d));
		ans = std::min(ans, std::max(b.dist(c),a.d));
		ans = std::min(ans, std::max(c.dist(a),b.d));
		printf("%.10lf\n", ans);	
	}
	else if (n == 2)
	{
		a.scan();
		b.scan();
		printf("%.10lf\n", std::max(a.d, b.d));
	}
	else if (n == 1)
	{
		a.scan();
		printf("%.10lf\n", a.d);
	}


}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
