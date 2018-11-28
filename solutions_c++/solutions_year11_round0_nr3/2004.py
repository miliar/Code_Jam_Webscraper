#include <stdio.h>

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		int n, value, sum = 0, total = 0, min = 0;
		scanf("%d", &n);
		while (n--)
		{
			scanf("%d", &value);
			if (min == 0)
				min = value;
			else if (value < min)
				min = value;
			sum ^= value;
			total += value;
		}
		if (sum != 0)
			printf("Case #%d: NO\n", i);
		else
			printf("Case #%d: %d\n", i, total - min);
	}
	return 0;
}