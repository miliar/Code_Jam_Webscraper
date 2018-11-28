#include<cstdio>

int t, i, j, n, k, p;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	scanf("%d", &t);

	for (i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);

		scanf("%d%d", &n, &k);

		for (j = 0; j < n; j++)
		{
			p = (k & (1 << j)) > 0;
			if (!p) break;
		}

		if (p) printf("ON\n"); else printf("OFF\n");
	}
	 		

	return 0;
}
