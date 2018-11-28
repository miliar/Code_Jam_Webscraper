#include <stdio.h>
#include <string.h>

int d[200][200];

int main()
{
	int ccc;
	scanf("%d", &ccc);
	for (int cc = 1; cc <= ccc; ++cc)
	{
		int n, s, p, t[200];
		scanf("%d%d%d", &n, &s, &p);
		for (int i = 0; i < n; ++i)
			scanf("%d", t + i);
		
		memset(d, 0, sizeof(d));
		for (int i = 1; i <= n; ++i)
		{
			for (int j = 0; j <= i && j <= s; ++j)
			{
				int val = t[i - 1];
				d[i][j] = d[i - 1][j];
				if ((val % 3 == 0 && val / 3 >= p) ||
					(val % 3 != 0 && val / 3 + 1 >= p))
					d[i][j]++;
				if (j > 0)
				{
					int tmp = d[i - 1][j - 1];
					if ((val && val % 3 != 2 && val / 3 + 1 >= p) ||
						(val % 3 == 2 && val /3 + 2 >= p))
						tmp++;
					if (tmp > d[i][j])
						d[i][j] = tmp;
				}
			}
		}
		printf("Case #%d: %d\n", cc, d[n][s]);
	}
	return 0;
}