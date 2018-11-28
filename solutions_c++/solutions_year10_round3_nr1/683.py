#include <stdio.h>

bool intersect(int a1, int b1, int a2, int b2)
{
	return (a1 < a2 && b1 > b2) || (a1 > a2 && b1 < b2);
}
int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int n, t, test, i, j, sol, a[1024], b[1024];

	scanf("%d", &t);

	for(test = 1; test <= t; ++test)
	{
		sol = 0;
		scanf("%d", &n);
		for(i = 1; i <= n; ++i)
		{
			scanf("%d %d", &a[i], &b[i]);
		}
		for(i = 1; i <= n; ++i)
		{
			for(j = i + 1; j <= n; ++j)
			{
				if(intersect(a[i], b[i], a[j], b[j]))
				{
					++sol;
				}
			}
		}
		printf("Case #%d: %d\n", test, sol);
	}

	return 0;
}
