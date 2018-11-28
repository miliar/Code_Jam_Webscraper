#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;

typedef string answer_type;

typedef long long llong;

llong gcd(llong a, llong b)
{
	if (a < 0)
		a *= -1;
	if (b < 0)
		b *= -1;
	return (b == 0) ? a : gcd(b, a % b);
}

llong lcm(llong a, llong b)
{
	return a * b / gcd(a, b);
}

answer_type solve()
{
	int n, pd, pg;
	cin >> n >> pd >> pg;
	llong u = 100 / gcd(pd, 100);
	for (int uu = u; uu <= n; uu += u)
	{
		llong wa = uu * pd / 100;
		llong la = uu - wa;
		for (llong lp = 0; lp <= 3000; lp++)
			for (llong wp = 0; wp <= 3000; wp++)
			{
				if ((100 * (wa + wp)) % (la + lp + wa + wp) != 0)
					continue;
				if ((100 * (wa + wp)) / (la + lp + wa + wp) != pg)
					continue;
				return "Possible";
			}
	}
	return "Broken";
}

int main()
{
	int T;
	cin >> T;
	answer_type ans;
	for (int i = 1; i <= T; i++)
		ans = solve(),
		cout << "Case #" << i << ": " << ans << endl,
		cerr << "Case #" << i << ": " << ans << endl;
}
