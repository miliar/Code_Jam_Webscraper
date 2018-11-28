#include <stdio.h>

int main()
{
	//freopen("A2.in", "r", stdin);
	//freopen("A2.out", "w", stdout);
	int nprob, n, k;
	scanf("%d", &nprob);
	for (int prob = 0; prob < nprob; prob ++)
	{
		scanf("%d%d", &n, &k);
		if (k == 0)
		{
			printf("Case #%d: OFF\n", prob + 1);
			continue;
		}
		int m = (1 << n);
		(k - (m - 1)) % m == 0 ?
			printf("Case #%d: ON\n", prob + 1) : printf("Case #%d: OFF\n", prob + 1);
	}

	return 0;
}