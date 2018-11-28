#include <stdio.h>

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int t, n, k;

	scanf("%d", &t);

	for(int test = 1; test <= t; ++test)
	{
		scanf("%d %d", &n, &k);
		k %= (1 << n);
		if(k + 1 == (1 << n))
		{
			printf("Case #%d: ON\n", test);
		}
		else
		{
			printf("Case #%d: OFF\n", test);
		}
	}

	return 0;
}
