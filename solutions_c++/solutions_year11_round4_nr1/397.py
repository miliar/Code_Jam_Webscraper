#include <stdio.h>
#include <algorithm>

struct ww_t
{
	int b, e, w;
	bool operator <(const ww_t &r) const
	{
		return w < r.w;
	}
};

void solve()
{
	static ww_t W[1000];
	int x, w, r, n;
	double rt, t, tt;
	scanf("%d %d %d %lf %d", &x, &w, &r, &rt, &n);
	W[0].b = 0;
	W[0].e = x;
	W[0].w = 0;
	for (int i = 1; i <= n; i++)
	{
		scanf("%d %d %d", &W[i].b, &W[i].e, &W[i].w);
		W[0].e -= W[i].e - W[i].b;
	}
	std::sort(W + 1, W + n + 1);
	t = 0;
	for (int i = 0; i <= n; i++)
		if (rt * (r + W[i].w) <= W[i].e - W[i].b)
		{
			t += rt + (W[i].e - W[i].b - rt * (r + W[i].w)) / (w + W[i].w);
			rt = 0;
		}
		else
		{
			tt = double(W[i].e - W[i].b) / (r + W[i].w);
			t += tt;
			rt -= tt;
		}
	printf("%.7f\n", t);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}