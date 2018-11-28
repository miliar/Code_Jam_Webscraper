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

#define DBG2 0

#define clr(a) memset(a, 0, sizeof(a))
#define fill(a, b) memset(a, b, sizeof(a))

void dbg(const char * fmt, ...)
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
	int mass;
	Point() {}
	Point(int _x, int _y, int _mass = 1) : x(_x), y(_y), mass(_mass) {}

	Point operator + (const Point & p) const
	{
		return Point(x + p.x, y + p.y, mass + p.mass);
	}

	Point operator - (const Point & p) const
	{
		return Point(x - p.x, y - p.y, mass - p.mass);
	}

	Point operator * (int k) const
	{
		return Point(x * k, y * k, mass * k);
	}

	bool operator == (const Point & p) const
	{
		return x == p.x && y == p.y;
	}

	void print() const
	{
		dbg("%d %d\n", x, y);
	}

};

Point p[600][600], a[600][600];
char s[600][600];
int b[600][600];

int main()
{
#ifndef ONLINE_JUDGE
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
#endif

	int tt;
	scanf("%d", &tt);
	for (int ii = 1; ii <= tt; ++ii)
	{
		int r, c, d;
		scanf("%d%d%d", &r, &c, &d);
		for (int i = 1; i <= r; ++i)
		{
			scanf("%s", s[i] + 1);
			dbg("%s\n", s[i] + 1);
		}
		clr(a);
		clr(b);
		for (int i = 1; i <= r; ++i)
			for (int j = 1; j <= c; ++j)
			{
				p[i][j] = Point(2 * i - 1, 2 * j - 1) * (s[i][j] - '0');
				a[i][j] = a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1] + p[i][j];
			}

		int len = min(r, c);
		while (len >= 3)
		{
			bool ok = false;
			for (int i = 0; i + len <= r; ++i)
				for (int j = 0; j + len <= c; ++j)
				{
					Point sum = a[i + len][j + len] - a[i][j + len] - a[i + len][j] + a[i][j];
					sum = sum - p[i + len][j + len] - p[i + 1][j + len] - p[i + len][j + 1] - p[i + 1][j + 1];

					Point center(2 * i + len, 2 * j + len);
					center = center * sum.mass;

					dbg("%d %d %d\n", len, i, j);
					center.print();
					sum.print();

					if (center == sum)
						ok = true;
				}

		   	if (ok)
		   		break;
		   	--len;
		}

		printf("Case #%d: ", ii);
		if (len >= 3)
			printf("%d\n", len);
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}
