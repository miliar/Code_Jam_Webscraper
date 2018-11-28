#include <stdio.h>

int main() {
	int t, n, a;
	scanf("%d", &t);
	for (int j = 1; j <= t; ++j)
	{
		scanf("%d", &n);
		int fix = 0;
		for (int i = 1; i <= n; ++i)
		{
			scanf("%d", &a);
			if (a == i)
				++fix;
		}
		printf("Case #%d: %d\n", j, n - fix);
	}
	return 0;
}
