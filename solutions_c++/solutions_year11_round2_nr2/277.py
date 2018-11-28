#include <stdio.h>
#include <algorithm>
#include <assert.h>

void solve()
{
	static std::pair<int, int> T[200];
	long long lo, hi, mid, x, l, r;
	int c, d;
	bool golo;
	scanf("%d %d", &c, &d);
	for (int i = 0; i < c; i++)
		scanf("%d %d", &T[i].first, &T[i].second);
	std::sort(T, T + c);
	lo = 0;
	hi = 2000000000000LL;
	d *= 2;
	do
	{
		mid = (lo + hi) / 2;
		x = -2000000000000LL;
		golo = true;
		for (int i = 0; i < c; i++)
		{
			if (2 * T[i].first - mid < x)
				l = x;
			else
				l = 2 * T[i].first - mid;
			if (2 * T[i].first + mid < x)
			{
				golo = false;
				break;
			}
			else
				r = 2 * T[i].first + mid;
			if (r - l < (long long)(T[i].second - 1) * d)
			{
				golo = false;
				break;
			}
			x = l + (long long)T[i].second * d;
		}
		if (golo)
			hi = mid;
		else
			lo = mid + 1;
	}
	while (lo != hi);
	printf("%lld.%lld\n", hi / 2, hi % 2 * 5);
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