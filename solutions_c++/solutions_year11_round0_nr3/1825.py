#include <stdio.h>

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tt;
	scanf("%d", &tt);
	for (int t = 1; t <= tt; t++)
	{
		int n;
		scanf("%d", &n);
		int sum = 0, xor = 0, mn = 1000000000;
		for (int i = 0; i < n; i++)
		{
			int c;
			scanf("%d", &c);
			sum += c;
			xor ^= c;
			if (c < mn) mn = c;
		}
		printf("Case #%d: ", t);
		if (xor != 0) printf("NO\n");
		else printf("%d\n", sum - mn);
	}
	return 0;
}