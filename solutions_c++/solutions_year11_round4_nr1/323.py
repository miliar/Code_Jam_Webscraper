#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

typedef long long LL;

#define MAXN 10100
#define EPS  1e-9

struct way
{
	double l;
	double v;
} w[MAXN];

bool way_less(const way &x, const way &y)
{
	return x.v < y.v;
}

int		x, s, r, t, n;
int		b, e, ww;
double	t0, ans;

int main()
{
    int tc;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%i", &tc);
    for(int tt=1; tt<=tc; ++tt)
    {
        //printf("Case %i:\n", tt);
		scanf("%i %i %i %i %i", &x, &s, &r, &t, &n);
		w[0].l = x;
		w[0].v = s;
		r = r - s;
		t0 = t;
		for(int i=1; i<=n; ++i)
		{
			scanf("%i %i %i", &b, &e, &ww);
			w[0].l -= e - b;
			w[i].l = e - b;
			w[i].v = ww + s;
		}

		sort(&w[0], &w[n + 1], way_less);

		ans = 0.0;
		for(int i=0; i<=n; ++i)
		{
			if ((w[i].v + r) * t0 > w[i].l - EPS)
			{			
				t0 -= w[i].l / (w[i].v + r);
				ans += w[i].l / (w[i].v + r);
	            w[i].l = 0.0;
			}
			else
			{
				ans += t0;
				w[i].l -= (w[i].v + r) * t0;
				t0 = 0.0;
				ans += w[i].l / w[i].v;
			}
		}
		printf("Case #%i: %.9f\n", tt, ans);
    }
}