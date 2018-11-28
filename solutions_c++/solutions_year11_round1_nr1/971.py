#include <iostream>
#include <stdio.h>
typedef _int64 LL;
using namespace std;

int gcd(int a, int b)
{
	if (0 == b)
		return a;
	return gcd(b, a % b);
}

bool CheckToday(int pd, LL n)
{
	int mind = 100 / gcd(pd, 100);
	if (n < mind)
		return false;
	return true;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int total;
	scanf("%d", &total);
	for (int test = 1; test <= total; ++test)
	{
		bool possible = true;
		LL n;
		int pd, pg;
		scanf("%I64d%d%d", &n, &pd, &pg);

		if (!CheckToday(pd, n))
			possible = false;

		if (100 == pg && 100 != pd)
			possible = false;

		if (0 == pg && 0 != pd)
			possible = false;

		if (possible)
			printf("Case #%d: Possible\n", test);
		else printf("Case #%d: Broken\n", test);
	}
	return 0;
}