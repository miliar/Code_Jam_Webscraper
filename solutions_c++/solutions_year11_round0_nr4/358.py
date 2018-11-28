#include <iostream>

using namespace::std;

int main()
{
	int test, t, n, i, x, ans;

	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	for (scanf("%d", &test), t = 1; t <= test; ++t)
	{
		printf("Case #%d: ", t);
		for (scanf("%d", &n), i = 1, ans = 0; i <= n; ++i)
		{
			scanf("%d", &x);
			if (x != i) ++ans;
		}
		printf("%d.000000\n", ans);
	}

	return 0;
}