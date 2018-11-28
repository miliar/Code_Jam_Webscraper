#include <stdio.h>

int main()
{
	int t, n;
	int min, sum, xorSum, get;
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		min = 2147483647;
		sum = xorSum = 0;
		scanf("%d", &n);
		for (int j=0;j<n;j++)
		{
			scanf("%d", &get);
			sum += get;
			min <?= get;
			xorSum ^= get;
		}
		printf("Case #%d: ", i);
		if (xorSum==0)
			printf("%d", sum-min);
		else
			printf("NO");
		printf("\n");
	}
	return 0;
}
