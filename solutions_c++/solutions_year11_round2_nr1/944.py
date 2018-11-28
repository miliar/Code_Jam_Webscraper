#include <stdio.h>
#define N 101

double GetDiv(double a, int b)
{
	return b>0 ? a/b : 0;
}

char a[N][N];
int win[N], tot[N];
double WP[N], OWP[N], OOWP[N];

int main()
{
	int i, j, n;
	int T, TT;
	scanf("%d", &TT);
	for (T = 1; T <= TT; ++T)
	{
		scanf("%d", &n);
		for (i = 0; i < n; ++i)
		{
			scanf("%s", &a[i]);
			win[i] = tot[i] = 0;
			for (j = 0; j < n; ++j) if ('.' != a[i][j])
			{
				++tot[i];
				if ('1' == a[i][j]) ++win[i];
			}
			WP[i] = GetDiv(win[i], tot[i]);
		}
		for (i = 0; i < n; ++i)
		{
			OWP[i] = 0;
			for (j = 0; j < n; ++j) if ('.' != a[i][j])
				OWP[i] += GetDiv(win[j] - ('1'==a[j][i]), tot[j]-1);
			OWP[i] = GetDiv(OWP[i], tot[i]);
		}
		for (i = 0; i < n; ++i)
		{
			OOWP[i] = 0;
			for (j = 0; j < n; ++j) if ('.' != a[i][j])
				OOWP[i] += OWP[j];
			OOWP[i] = GetDiv(OOWP[i], tot[i]);
		}
		printf("Case #%d:\n", T);
		for (i = 0; i < n; ++i)
		{
			double RPI = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			printf("%.10lf\n", RPI);
		}
	}
	return 0;
}
