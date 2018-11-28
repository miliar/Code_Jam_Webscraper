#include <stdio.h>

int main()
{
//	freopen("input.txt", "r", stdin);

	int t;
	scanf("%d", &t);

	for (int test = 1; test <= t; test++)
	{
		printf("Case #%d: ", test);

		int n;
		scanf("%d", &n);

		int x = 0;
		int sum = 0;
		int a[1010];
		int min = 10000001;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
			x ^= a[i];
			sum += a[i];
			if (min > a[i])
			{
				min = a[i];
			}

		}

		if (x != 0)
		{
			printf("NO\n");
		}
		else
		{
			printf("%d\n", sum - min);
		}


	}


	return 0;
}