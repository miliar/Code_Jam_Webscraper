#include <cstdio>

using namespace std;

int gcd(int a, int b)
{
	int t;
	while (b) {
		t = b;
		b = a % b;
		a = t;
	}
	return a;
}

int main()
{
	freopen("a0.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int testCount;
	int n, pd, pg;
	int ans;
	
	scanf("%d", &testCount);
	for (int tc = 1; tc <= testCount; tc++) {
		scanf("%d%d%d", &n, &pd, &pg);
		ans = 0;
		if (pd == pg)
			ans = 1;
		else if (pg == 0 || pg == 100)
			ans = 0;
		else if (n * gcd(pd, 100) >= 100)
			ans = 1;
		else
			ans = 0;
		printf("Case #%d: %s\n", tc, ans ? "Possible" : "Broken");
	}
	return 0;
}
