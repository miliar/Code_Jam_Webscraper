#include <cstdio>

long n;
int pd, pg;

int solve()
{
	bool result = false;
	if (pd > 0 && n < 100) {
		for (int i = 1; !result && i <= n; ++ i)
			result = i * pd % 100 == 0;
	} else {
		result = true;
	}
	if (!result) return false;
	return (pg != 100 || pd == 100) && (pg != 0 || pd == 0);
}

int main()
{
	int testCases;
	scanf("%d", &testCases);
	for (int t = 1; t <= testCases; ++ t) {
		scanf("%ld%d%d", &n, &pd, &pg);
		printf("Case #%d: %s\n", t, solve() ? "Possible" : "Broken");
	}
	return 0;
}
