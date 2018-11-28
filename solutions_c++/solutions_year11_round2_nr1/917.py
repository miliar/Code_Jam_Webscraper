#include <stdio.h>

const int N = 105;

int a[N][N];
double w[N], ow[N], oww[N];
char s[N + 5];
int sum[N], cnt[N];

int main ()
{
	//freopen("A-large (2).in", "r", stdin);
	//freopen("A-large (2).out", "w", stdout);
	int ca;
	scanf("%d", &ca);
	int cas = 0;

	while (ca--)
	{
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%s", s);
			sum[i] = 0;
			cnt[i] = 0;
			for (int j = 0; j < n; j++)
			{
				if (s[j] == '1') 
				{
					a[i][j] = 1;
					cnt[i]++;
					sum[i]++;
				}
				else if (s[j] == '0')
				{
					a[i][j] = 0;
					cnt[i]++;
				}
				else a[i][j] = -1;
			}			
			w[i] = sum[i] * 1.0 / cnt[i];
			//printf("%lf\n", w[i]);
		}
		for (int i = 0; i < n; i++)
		{
			ow[i] = 0;
			int cntt = 0;
			for (int j = 0; j < n; j++)
			{
				if (a[i][j] == -1) continue;
				cntt++;
				int tmp = sum[j] - a[j][i];
				ow[i] += 1.0 * tmp / (cnt[j] - 1);
			}
			if (cntt != 0) ow[i] /= cntt;
			//printf("## %d %lf\n", cnt, ow[i]);
		}
		for (int i = 0; i < n; i++)
		{
			oww[i] = 0;
			int cntt = 0;
			for (int j = 0; j < n; j++)
			{
				if (a[i][j] != -1) 
				{
					oww[i] += ow[j];
					cntt++;
				}
			}
			if (cntt != 0) oww[i] /= cntt;
		}
		printf("Case #%d:\n", ++cas);
		for (int i = 0; i < n; i++)
		{
			double res = 0.25 * w[i] + 0.50 * ow[i] + 0.25 * oww[i];
			printf("%.12lg\n", res);
		}
	}
	return 0;
}
	
