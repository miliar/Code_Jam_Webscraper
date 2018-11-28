#include <stdio.h>

int main() {
	int t, n, a;
	scanf("%d", &t);
	for (int j = 1; j <= t; ++j)
	{
		scanf("%d", &n);
		int min = 1000001;
		int sum = 0, xsum = 0;
		for (int i = 1; i <= n; ++i)
		{
			scanf("%d", &a);
			if (min > a)
				min = a;
			xsum ^= a;
			sum += a;
		}
		if (xsum)
			printf("Case #%d: NO\n", j);
		else
			printf("Case #%d: %d\n", j, sum - min);
	}
	return 0;
}
