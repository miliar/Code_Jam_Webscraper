#include <cstdio>
using namespace std;

int t, c, d, n, m;
char a[110];
char b[110];
char com[50][5];
char opp[50][5];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("outputlarge.txt", "w", stdout);

	int i, j, k, l;

	scanf("%d", &t);
	for (i = 1; i <= t; ++i)
	{
		scanf("%d", &c);
		for (j = 0; j < c; ++j)
			scanf("%s", &com[j]);
		scanf("%d", &d);
		for (j = 0; j < d; ++j)
			scanf("%s", &opp[j]);
		scanf("%d%s", &n, &a);
		m = 0;
		for (j = 0; j < n; ++j)
		{
			if (m > 0)
			{
				for (k = 0; k < c; ++k)
					if (com[k][0] == b[m - 1] && com[k][1] == a[j] || com[k][0] == a[j] && com[k][1] == b[m - 1])
						break;
				if (k < c)
				{
					b[m - 1] = com[k][2];
					continue;
				}
				for (k = 0; k < d; ++k)
				{
					for (l = 0; l < m; ++l)
						if (opp[k][0] == b[l] && opp[k][1] == a[j] || opp[k][0] == a[j] && opp[k][1] == b[l])
							break;
					if (l < m)
						break;
				}
				if (k < d)
				{
					m = 0;
					continue;
				}
			}
			b[m++] = a[j];
		}
		printf("Case #%d: [", i);
		for (j = 0; j < m; ++j)
		{
			if (j + 1 < m)
				printf("%c, ", b[j]);
			else
				printf("%c", b[j]);
		}
		printf("]\n");
	}
	return 0;
}