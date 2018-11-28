#include <cstdio>
#include <cstring>
#include <algorithm>

using std::sort;

struct Tpoint
{
	int x, y;
};

inline bool cmp(Tpoint a, Tpoint b)
{
	return a.y < b.y;
}

const int MAXN = 1010;

int x, s, r, t, n;
Tpoint a[MAXN];

void init()
{
	scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
	int i, st, ed, w;
	for (i=1; i<=n; ++i)
	{
		scanf("%d %d %d", &st, &ed, &w);
		a[i].x = ed - st;
		a[i].y = w + s;
		x -= (ed - st);
	}
	a[++n].x = x;
	a[n].y = s;
	r -= s;
}

void solve()
{
	sort(a+1, a+n+1, cmp);
	int i;
	double lt = t;
	double ans = 0;
	double tmp;
	for (i=1; i<=n; ++i)
	{
		if ((double)a[i].x / (a[i].y + r) <= lt)
		{
			ans += (double)a[i].x / (a[i].y + r);
			lt -= (double)a[i].x / (a[i].y + r);
		}
		else
		{
			ans += lt;
			tmp = lt * (a[i].y + r);
			lt = 0;
			ans += (double)(a[i].x-tmp) / (a[i].y);
		}
	}
	printf("%.8f\n", ans);
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int CASE, TT;
	scanf("%d", &TT);
	for (CASE=1; CASE<=TT; ++CASE)
	{
		init();
		printf("Case #%d: ", CASE);
		solve();
	}
	return 0;
}


