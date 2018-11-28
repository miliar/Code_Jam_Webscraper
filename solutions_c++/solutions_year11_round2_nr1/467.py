#include <stdio.h>

const int N = 200;
int main()
{
	double wp[N], owp[N], oowp[N];
	int win[N], all[N];
	int tc, tc0;
	char a[N][N];
	scanf("%d", &tc0);
	for (tc = 1; tc <= tc0; tc++)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%s", a[i]);
		}

		for (int i = 0; i < n; i++)
		{
			win[i] = 0;
			all[i] = 0;
			for (int j = 0; j < n; j++)
			{
				if (a[i][j] == '1')
				{
					win[i]++;
				}
				if (a[i][j] != '.')
				{
					all[i]++;
				}
			}
			wp[i] = 1.0 * win[i] / all[i];
		}

		for (int i = 0; i < n; i++)
		{
			double sum = 0;
			int count = 0;
			for (int j = 0; j < n; j++)
			{
				if (a[i][j] != '.')
				{
					if (a[i][j] == '0')
					{
						sum += 1.0 * (win[j] - 1) / (all[j] - 1);
					}
					else
					{
						sum += 1.0 * (win[j]) / (all[j] - 1);
					}
					count ++;
				}
			}
			owp[i] = sum / count;
		}

		for (int i = 0; i < n; i++)
		{
			double sum = 0;
			int count = 0;
			for (int j = 0; j < n; j++)
			{
				if (a[i][j] != '.')
				{
					sum += owp[j];
					count ++;
				}
			}
			oowp[i] = sum / count;
		}

		printf("Case #%d:\n", tc);
		for (int i = 0; i < n; i++)
		{
			//printf("%lf,%lf,%lf:", wp[i], owp[i], oowp[i]);
			printf("%.10lf\n", wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
		}
	}
	return 0;
}
