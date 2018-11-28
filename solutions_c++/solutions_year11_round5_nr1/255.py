#include <cstdio>
#include <cstring>

const int MAXN = 1010;

int w, l, u, g;
double a[MAXN], b[MAXN];
double c[MAXN];
bool chk1[MAXN], chk2[MAXN];

void init()
{
	scanf("%d %d %d %d", &w, &l, &u, &g);
	int i, j, k;
	memset(chk1, 0, sizeof(chk1));
	memset(chk2, 0, sizeof(chk2));
	for (i=1; i<=l; ++i)
	{
		scanf("%d %d", &j, &k);
		a[j] = k;
		chk1[j] = true;
	}
	for (i=1; i<=u; ++i)
	{
		scanf("%d %d", &j, &k);
		b[j] = k;
		chk2[j] = true;
	}
}

inline double getArea(double now)
{
	int i = (int)now;
	now -= i;
	double l1 = b[i] - a[i];
	double l2 = b[i+1] - a[i+1];
	return c[i] + (l1 + l1 + (l2 - l1) * now) * now * 0.5;
}

double binsearch(double k)
{
	double l = 0;
	double r = w;
	double mid;
	while (r - l > 1e-8)
	{
		mid = (l + r) / 2;
		if (getArea(mid) > k) r = mid;
		else l = mid;
	}
	return l;
}

void solve()
{
	int l = 0;
	int i, j;
	while (l < w)
	{
		i = l + 1;
		while (!chk1[i]) ++i;
		for (j=l+1; j<i; ++j)
			a[j] = (a[i] - a[l]) * (j - l) / (i - l) + a[l];
		l = i;
	}
	l = 0;
	while (l < w)
	{
		i = l + 1;
		while (!chk2[i]) ++i;
		for (j=l+1; j<i; ++j)
			b[j] = (b[i] - b[l]) * (j - l) / (i - l) + b[l];
		l = i;
	}
	c[0] = 0;
	for (i=1; i<=w; ++i)
		c[i] = c[i-1] + (b[i] - a[i] + b[i-1] - a[i-1]) * 0.5;
	double area = c[w] / g;
	double now = 0;
	double left;
	for (i=1; i<g; ++i)
	{
		left = area * i;
		printf("%.6f\n", binsearch(left));
	}
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int CASE, TT;
	scanf("%d", &TT);
	for (CASE=1; CASE<=TT; ++CASE)
	{
		printf("Case #%d:\n", CASE);
		init();
		solve();
	}
	return 0;
}








