#include <stdio.h>
int main()
{
	int cases;
	scanf("%d", &cases);
	for (int i = 1; i <= cases; ++i)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		if ((k + 1) % (1 << n) == 0)
			printf("Case #%d: ON\n", i);
		else printf("Case #%d: OFF\n", i);
	}
	return 0;
}
