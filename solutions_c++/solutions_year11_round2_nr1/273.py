#include <stdio.h>
#include <assert.h>

void solve()
{
	static double WP[100], OWP[100], OOWP[100];
	static char T[100][101];
	double x;
	int n;
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++)
		gets(T[i]);
	for (int i = 0, s, c; i < n; i++)
	{
		s = 0;
		c = 0;
		for (int j = 0; j < n; j++)
			if (T[i][j] != '.')
			{
				if (T[i][j] == '1')
					s++;
				else
					assert(T[i][j] == '0');
				c++;
			}
		WP[i] = (double)s / c;
	}
	for (int i = 0, c, cc, ss; i < n; i++)
	{
		x = 0.0;
		c = 0;
		for (int j = 0; j < n; j++)
			if (T[i][j] != '.')
			{
				cc = 0;
				ss = 0;
				for (int k = 0; k < n; k++)
					if (i != k && T[j][k] != '.')
					{
						if (T[j][k] == '1')
							ss++;
						cc++;
					}
				x += (double)ss / cc;
				c++;
			}
		OWP[i] = x / c;
	}
	for (int i = 0, c; i < n; i++)
	{
		x = 0.0;
		c = 0;
		for (int j = 0; j < n; j++)
			if (T[i][j] != '.')
			{
				x += OWP[j];
				c++;
			}
		OOWP[i] = x / c;
	}

	putchar('\n');
	for (int i = 0; i < n; i++)
		printf("%.7f\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}