#include <stdio.h>
#include <string.h>

const int inf = 100000000;

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int c[128][128], t, test, i, j, k, p, q, v[128], d;

	scanf("%d", &t);

	for(test = 1; test <= t; ++test)
	{
		scanf("%d %d", &p, &q);
		for(i = 1; i <= q; ++i)
		{
			scanf("%d", &v[i]);
		}
		v[0] = 0;
		v[q + 1] = p + 1;
		memset(c, 0, sizeof(c));
		for(i = 1; i <= q; ++i)
		{
			c[i][i] = v[i + 1] - v[i - 1] - 2;
		}
		for(d = 1; d < q; ++d)
		{
			for(i = 1; i + d <= q; ++i)
			{
				c[i][i + d] = inf;
				int temp;
				for(k = i; k <= i + d; ++k)
				{
					temp = v[i + d + 1] - v[i - 1] - 2;
					if(k > i)
					{
						temp += c[i][k - 1];
					}
					if(k < i + d)
					{
						temp += c[k + 1][i + d];
					}
					if(c[i][i + d] >= temp)
					{
						c[i][i + d] = temp;
					}
				}
				//printf("%d %d -> %d\n", i, i + d, c[i][i + d]);
			}
		}
		printf("Case #%d: %d\n", test, c[1][q]);
	}


	return 0;
}
