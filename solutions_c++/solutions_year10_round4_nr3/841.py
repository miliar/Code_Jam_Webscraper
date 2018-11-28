#include <stdio.h>
#include <string.h>
const int MAXN = 110;
int ans;
int n;
int a[2][MAXN][MAXN];
int main()
{
	int cases;
	scanf("%d", &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		printf("Case #%d: ", ca);
		scanf("%d", &n);
		memset(a, 0, sizeof(a));
		for (int i = 0; i < n; ++i)
		{
			int t1, t2, t3, t4;
			scanf("%d%d%d%d", &t1, &t2, &t3, &t4);
			for (int j = t1; j <= t3; ++j)
				for (int k = t2; k <= t4; ++k)
					a[0][j][k] = 1;
		}
		ans = 0;
		while (true)
		{
			bool flag = false;
			for (int i = 1; i <= 100; ++i)
				for (int j = 1; j <= 100; ++j)
				{
					if ((a[ans & 1][i][j] && (a[ans & 1][i - 1][j] || a[ans & 1][i][j - 1])) || (!a[ans & 1][i][j] && a[ans & 1][i - 1][j] && a[ans & 1][i][j - 1]))
					{
						a[(ans + 1) & 1][i][j] =1;
						flag = true;
					}
					else a[(ans + 1) & 1][i][j] = 0;

				}
			++ans;
			if (!flag) break;
		}
		printf("%d\n", ans);
	}
	return 0;
}
