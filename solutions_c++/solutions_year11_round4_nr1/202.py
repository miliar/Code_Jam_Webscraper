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

struct Walkway {
	int b, e, w;
	bool operator < (const Walkway & w) const
	{
		return e < w.e;
	}
} ww[10000];

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
		int s, r, x, t, n;
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		double walkT = 0;
		int fastLen = 0;
		vector <pii> paths;
		int last = 0;
		for (int i = 0; i < n; ++i)
		{
			scanf("%d%d%d", &ww[i].b, &ww[i].e, &ww[i].w);
		}
		sort(ww, ww + n);
		for (int i = 0; i < n; ++i)
		{
			int b = ww[i].b;
			int e = ww[i].e;
			int w = ww[i].w;
			paths.push_back(pii(s, b - last));
			paths.push_back(pii(s + w, e - b));
			last = e;
		}
		paths.push_back(pii(s, x - last));

		sort(paths.begin(), paths.end());
		double allT = 0;
		double runT = 0;
		for (int i = 0; i < int(paths.size()); ++i)
		{
			int w = paths[i].first;
			int l = paths[i].second;
			double curT = min(t - runT, double(l) / (w - s + r));
			allT += curT;
			runT += curT;
			allT += (l - (w - s + r) * curT) / w;
		}

		printf("Case #%d: %.10lf\n", ii, allT);
	}

	return 0;
}
