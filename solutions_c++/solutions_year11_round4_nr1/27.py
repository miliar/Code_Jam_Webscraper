#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
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

class walkway
{
public:
	int w, b, e;
	void scan()
	{
		scanf("%d%d%d", &b, &e, &w);
	}
	bool operator < (const walkway & w) const
	{
		return b < w.b;
	}
};
const double eps = 1e-9;

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int s, t, r;
	int x, n;
	scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
	std::vector<pii> segs;
	std::vector<walkway> ways;
	for(int i = 0; i < n; i++)
	{
		walkway temp;
		temp.scan();
		ways.push_back(temp);
	}
	std::sort(ways.begin(), ways.end());
	int last = 0;
	for(int i = 0; i < n; i++)
	{
		segs.push_back(pii(s, ways[i].b - last));
		segs.push_back(pii(s + ways[i].w, ways[i].e - ways[i].b));
		last = ways[i].e;
	}
	segs.push_back(pii(s, x - last));
	std::sort(segs.begin(), segs.end());
	double time = t;
	double ans = 0;
	r -= s;
	for(int i = 0; i < (int) segs.size(); i++)
	{
		if (segs[i].second == 0)
			continue;
		if (time < eps)
		{
			ans += segs[i].second / (double) segs[i].first;
		}
		else
		{
			if (segs[i].second / ((double) segs[i].first + r) < time)
			{
				ans += segs[i].second / ((double) segs[i].first + r);
				time -= segs[i].second / ((double) segs[i].first + r);
			}
			else
			{
				double diff = (segs[i].second - (segs[i].first + r) * time)/segs[i].first;
				ans += time + diff;
				if (diff < -eps)
					throw 42;
				time = 0;
			}
		}
	}
	printf("%.10lf\n", ans);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
		solve(i);

	return 0;
}
