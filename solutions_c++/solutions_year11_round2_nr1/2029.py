#include <stdio.h>

struct RPI
{
	double wp;
	double owp;
	double oowp;
}player[105];
char score[105][105];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		int n;
		scanf("%d", &n);
		for (int j = 0; j < n; ++j)
			scanf("%s", score[j]);
		for (int j = 0; j < n; ++j)
		{
			int win = 0, total = 0;
			for (int k = 0; k < n; ++k)
			{
				if (score[j][k] == '.')
					continue;
				if (score[j][k] == '1')
					++win;
				++total;
			}
			player[j].wp = win * 1.0 / total;
			int num = 0;
			double wp = 0.0;
			for (int k = 0; k < n; ++k)
			{
				win = total = 0;
				if (k == j || score[k][j] == '.')
					continue;
				++num;
				for (int l = 0; l < n; ++l)
				{
					if (l == j || score[k][l] == '.')
						continue;
					if (score[k][l] == '1')
						++win;
					++total;
				}
				wp += win * 1.0 / total;
			}
			player[j].owp = wp / num;
		}
		for (int j = 0; j < n; ++j)
		{
			int num = 0;
			double owp = 0.0;
			for (int k = 0; k < n; ++k)
			{
				if (k == j || score[j][k] == '.')
					continue;
				++num;
				owp += player[k].owp;
			}
			player[j].oowp = owp / num;
		}
		printf("Case #%d:\n", i);
		for (int j = 0; j < n; ++j)
		{
			printf("%lf\n", 0.25 * player[j].wp + 0.50 * player[j].owp + 0.25 * player[j].oowp);
		}
	}
	return 0;
}