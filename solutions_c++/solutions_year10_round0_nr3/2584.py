#include <stdio.h>

int t;
int g[110];

int main()
{
	//freopen("c", "r", stdin);

	int n, k, r;
	scanf("%d", &t);
	for (int t1 = 0; t1 < t; t1++)
	{
		int sum = 0;
		int res = 0;
		printf("Case #%d: ", t1 + 1);
		scanf("%d%d%d", &r, &k, &n);

		for (int i = 0; i < n; i++)
		{
			scanf("%d", &g[i]);
			sum += g[i];
		}

		if (sum <= k)
		{
			printf("%d\n", sum * r);
			continue;
		}

		int pos = 0;

		for (int i = 0; i < r; i++)
		{
			int cur = 0;
			while (cur + g[pos] <= k)
			{
				cur += g[pos];
				pos = (pos + 1) % n;
			}

			res+=cur;
			cur = 0;

		}

		printf("%d\n", res);

	}

	return 0;

}