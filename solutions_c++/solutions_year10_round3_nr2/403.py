#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <deque>

using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{
		long long l, p, c;

		scanf("%lld %lld %lld", &l, &p, &c);
		l *= c;
		int cnt = 0;
		while (l < p)
		{
			++cnt;
			l *= c;
		}
		int res = 0;
		while (cnt > 0)
		{
			++res;
			cnt /= 2;
		}
		printf("Case #%d: %d\n", t + 1, res);
	}

	return 0;
}