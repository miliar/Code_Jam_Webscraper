#include <cmath>#include <cstdio>
#include <cstdlib>
#include <cstring>

char s[100][101];
double WP[100], WPT[100][100], OWP[100], OOWP[100];
double RPI[100];
int win[100], lose[100];

int main()
{
	int T, N, t = 0;
	for (scanf("%d", &T); T > 0; --T)
	{
		scanf("%d\n", &N);
		for (int i=0; i < N; ++i) scanf("%s", s[i]);
		
		for (int i=0; i < N; ++i)
		{
			win[i] = 0;
			lose[i] = 0;
			for (int j=0; j < N; ++j)
			{
				if (s[i][j] == '1') ++win[i];
				if (s[i][j] == '0') ++lose[i];
			}
		}
		
		for (int i=0; i < N; ++i) WP[i] = (double) win[i] / (win[i] + lose[i]);
		
		for (int i=0; i < N; ++i)
			for (int j=0; j < N; ++j)
			{
				if (s[i][j] == '.') WPT[i][j] = WP[i];
				if (s[i][j] == '1') WPT[i][j] = (double) (win[i] - 1) / (win[i] + lose[i] - 1);
				if (s[i][j] == '0') WPT[i][j] = (double) win[i] / (win[i] + lose[i] - 1);
			}
		
		for (int i=0; i < N; ++i)
		{
			OWP[i] = 0;
			int c = 0;
			for (int j=0; j < N; ++j)
				if (j != i && s[i][j] != '.')
				{
					++c;
					OWP[i] += WPT[j][i];
				}
			OWP[i] /= c;
		}
		
		for (int i=0; i < N; ++i)
		{
			OOWP[i] = 0;
			int c = 0;
			for (int j=0; j < N; ++j)
				if (s[i][j] != '.')
				{
					++c;
					OOWP[i] += OWP[j];
				}
			OOWP[i] /= c;
		}
		
		for (int i=0; i < N; ++i)
			RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
		
		printf("Case #%d:\n", ++t);
		for (int i=0; i < N; ++i) printf("%lf\n", RPI[i]);
	}
	return 0;
}
