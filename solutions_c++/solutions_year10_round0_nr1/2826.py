#include <stdio.h>

int fast2power(int power)
{
	int result = 1;
	if (power > 0)
	{
		result = fast2power(power / 2);
		result = result * result;
		if (power % 2 != 0) result = 2 * result;
	}
	return result;
}

int main()
{
	int t;
	scanf("%d", &t);

	int n;
	int k;
	for (int i = 1; i<=t; i++)
	{
		scanf("%d%d", &n, &k);
		if ((k + 1) % fast2power(n) == 0) printf("Case #%d: ON\n", i);
					 else printf("Case #%d: OFF\n", i);
	}
}