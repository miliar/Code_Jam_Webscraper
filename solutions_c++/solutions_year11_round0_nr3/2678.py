#include <stdio.h>

int main()
{
	int t, T, n, i, j, s, min, m, a;

	freopen("c.txt", "rb", stdin);
	freopen("outc.txt", "wb", stdout);
	scanf("%d", &T);

	for (t=1; t<=T; t++)
	{
		scanf("%d", &n);

		s = 0;
		a = 0;
		min = 1000000;
		for (i=1; i<=n; i++)
		{
			scanf("%d", &m);
			s += m;
			a = a^m;

			if (min > m)
				min = m;
		}

		if (a != 0)
			printf("Case #%d: NO\n", t);
		else
			printf("Case #%d: %d\n", t, s-min);
	}
	return 0;
}