#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cassert>

using namespace std;

const int MAX = 128;

double WP[MAX], OWP[MAX], OOWP[MAX];

int N;
char p[MAX][MAX];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t_case = 1; t_case <= T; t_case++)
	{
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%s", p[i]);

		for (int i = 0; i < N; i++)
		{
			int win = 0, total = 0;
			for (int j = 0; j < N; j++)
			{
				if (p[i][j] != '.')
				{
					total++;
					if (p[i][j] == '1')
						win++;
				}
				WP[i] = (double)win / total;
			}
		}

		for (int k = 0; k < N; k++)
		{
			double s = 0.0;
			int z = 0;
			for (int i = 0; i < N; i++) if (p[k][i] != '.')
			{
				z++;
				int win = 0, total = 0;
				for (int j = 0; j < N; j++) if (j != k)
				{
					if (p[i][j] != '.')
					{
						total++;
						if (p[i][j] == '1')
							win++;
					}
				}
				s += (double)win / total;

			}
			OWP[k] = s / z;
		}

		for (int i = 0; i < N; i++)
		{
			double s = 0.0;
			int total = 0;
			for (int j = 0; j < N; j++)
			{
				if (p[i][j] != '.')
				{
					s += OWP[j];
					total++;
				}
			}
			OOWP[i] = s / total;
		}

		printf("Case #%d:\n", t_case);
		for (int i = 0; i < N; i++)
			printf("%.10f\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
	}
	return 0;
}
