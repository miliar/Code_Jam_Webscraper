#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>

int main()
{
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		bool res = !((k + 1) % (1 << n));
		printf("Case #%d: %s\n", i, res ? "ON" : "OFF");
	}
	return 0;
}