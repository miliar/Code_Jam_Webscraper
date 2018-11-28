# include <stdio.h>
# include <iostream>
# include <algorithm>

using namespace std;

struct TRunway
{
	double l, w;
	bool operator<(TRunway other)
	{
		return w < other.w;
	}
};

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		double x, s, r, t, l;
		int n;
		cin >> x >> s >> r >> t >> n;
		l = x;

		TRunway rw[1010];
		for (int i = 0; i < n; ++i)
		{
			int b, e;
			cin >> b >> e >> rw[i].w;
			rw[i].l = e - b;
			l -= rw[i].l;
		}

		sort(rw, rw + n);

		double cur = 0;
		double sec = 0;
		if (l / r < t)
		{
			sec += l / r;
			cur = l;
		}
		else
		{
			sec = t;
			cur = r * t;
			sec += (l - cur) / s;
			cur = l;
		}

		for (int i = 0; i < n; ++i)
		{
			if (rw[i].l / (r + rw[i].w) + sec < t)
			{
				sec += rw[i].l / (r + rw[i].w);
			}
			else
			{
				cur = 0;
				if (sec < t)
				{
					cur = (r + rw[i].w) * (t - sec);
					sec = t;
				}
				sec += (rw[i].l - cur) / (s + rw[i].w);
			}			
		}

		printf("Case #%d: %0.9lf\n", test, sec);
	}

	return 0;
}