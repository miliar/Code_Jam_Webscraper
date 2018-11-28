#include <stdio.h>
#include <string.h>

char s[110][110];
int win[110], lose[110];
double wp[110], owp[110], oowp[110], rpi[110];
int main()
{
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int nt = 1; nt <= t; ++nt)
	{
		int n, i, j;
		scanf("%d", &n);
		for (i = 0; i < n; ++i)
		{
			scanf("%s", s[i]);
			win[i] = lose[i] = 0;
			for (j = 0; j < n; ++j)
			{
				if (s[i][j] == '1')
					++win[i];
				if (s[i][j] == '0')
					++lose[i];
			}
			wp[i] = owp[i] = oowp[i] = 0.0;
		}
		for (i = 0; i < n; ++i)
			wp[i] = win[i] * 1.0 / (win[i] + lose[i]);
		for (i = 0; i < n; ++i)
		{
			for (j = 0; j < n; ++j)
				if (s[j][i] != '.')
				{
					int w = win[j], l = lose[j];
					if (s[j][i] == '1')
						--w;
					else
						--l;

					owp[i] += w * 1.0 / (w + l);
				}
			owp[i] /= win[i] + lose[i];
		}
		for (i = 0; i < n; ++i)
		{
			for (j = 0; j < n; ++j)
				if (s[j][i] != '.')
					oowp[i] += owp[j];
			oowp[i] /= win[i] + lose[i];
		}
		for (i = 0; i < n; ++i)
			rpi[i] = wp[i] / 4.0 + owp[i] / 2.0 + oowp[i] / 4.0;
		printf("Case #%d:\n", nt);
		for (i = 0; i < n; ++i)
			printf("%.12lf\n", rpi[i]);
	}
	return 0;
}
