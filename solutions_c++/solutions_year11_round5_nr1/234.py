#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

#include <cstdarg>

using namespace std;

#define DBG2 1

#define clr(a) memset(a, 0, sizeof(a))
#define fill(a, b) memset(a, b, sizeof(a))

void dbg(char * fmt, ...)
{
#ifdef DBG1
#if	DBG2
	FILE * file = stdout;

	va_list args;
	va_start(args, fmt);
	vfprintf(file, fmt, args);
	va_end(args);

	fflush(file);
#endif
#endif
}

typedef long long ll;
typedef unsigned long long ull;
typedef std::pair<int, int> pii;

struct Point {
	int x, y;
	void read()
	{
		scanf("%d%d", &x, &y);
	}
};

const double eps = 1e-9;

Point p1[1000], p2[1000];
int n1, n2;
int w;
int g;

double getY(Point * p, int n, double x)
{
	int i = 0;
	while (p[i + 1].x < x - eps)
		++i;
	return p[i].y + (p[i + 1].y - p[i].y) * (x - p[i].x) / (p[i + 1].x - p[i].x);
}

double getDy(double x0)
{
	return getY(p2, n2, x0) - getY(p1, n1, x0);
}

int main()
{
#ifdef DBG1
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
#endif

	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		scanf("%d%d%d%d", &w, &n1, &n2, &g);
//		vector <int> xx;
		for (int i = 0; i < n1; ++i)
		{
			p1[i].read();
//			xx.push_back(p1[i].x);
		}
		for (int i = 0; i < n2; ++i)
		{	
			p2[i].read();
//			xx.push_back(p2[i].x);
		}

//		sort(xx.begin(), xx.end());
//		xx.erase(unique(xx.begin(), xx.end()), xx.end());

		int s = 0;
		for (int i = 1; i < n1; ++i)
			s -= (p1[i].x - p1[i - 1].x) * (p1[i].y + p1[i - 1].y);
		for (int i = 1; i < n2; ++i)
			s += (p2[i].x - p2[i - 1].x) * (p2[i].y + p2[i - 1].y);

		double s0 = double(s) / g;

		double curX = 0;
		int i1 = 0;
		int i2 = 0;
		double curS = 0;
		printf("Case #%d:\n", ii);
		while (1)
		{
			while (i1 < n1 && p1[i1].x < curX + eps)
				++i1;
			while (i2 < n2 && p2[i2].x < curX + eps)
				++i2;
			if (i1 >= n1 || i2 >= n2)
				break;
			double nextX = min(p1[i1].x, p2[i2].x);
			double a = getDy(curX);
			double b = getDy(nextX);
			double ds = (a + b) * (nextX - curX);
			if (curS + ds <= s0 + eps)
			{
				curS += ds;
				curX = nextX;
			}
			else
			{
				double left = curX;
				double right = nextX;
				for (int _ = 0; _ < 50; ++_)
				{
					double q = (left + right) / 2;
					if (curS + (a + getDy(q)) * (q - curX) > s0)
						right = q;
					else
						left = q;
				}
				printf("%.10lf\n", left);
				curX = left;
				curS = 0;
			}
		}
	}

	return 0;
}
