#include <stdio.h>

int main()
{
	int numCase, cases;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N, i, j, num0[100], num1[100], total[100], cnt;
	double WP[100], OWP[100], OOWP[100], temp, RPI[100];
	char data[100][101];	

	for(scanf("%i", &cases), numCase = 1; numCase <= cases; numCase++)
	{
		scanf("%i\n", &N);
		for(i = 0; i < N; i++)
			scanf("%s", data[i]);

		// WP
		for(i = 0; i < N; i++)
		{				
			num0[i] = num1[i] = total[i] = 0;
			for(j = 0; j < N; j++)
			{
				if(data[i][j] == '1') { num1[i]++; total[i]++; }
				else if(data[i][j] == '0') { num0[i]++; total[i]++; }
			}
			WP[i] = 1.0 * num1[i] / total[i];
		}

		// OWP
		for(i = 0; i < N; i++)
		{				
			OWP[i] = 0;
			cnt = 0;
			for(j = 0; j < N; j++)
			{
				if(i == j) continue;

				if(data[j][i] != '.')
				{
					if(data[j][i] == '1')
						OWP[i] += 1.0 * (num1[j] - 1) / (total[j] - 1);
					else
						OWP[i] += 1.0 * (num1[j]) / (total[j] - 1);
					cnt++;
				}
			}
			OWP[i] = OWP[i] / cnt;
		}

		// OOWP
		printf("Case #%i:\n", numCase);
		for(i = 0; i < N; i++)
		{
			cnt = 0;
			OOWP[i] = 0;
			for(j = 0; j < N; j++)
			{
				if(i == j) continue;

				if(data[j][i] != '.')
				{
					OOWP[i] += OWP[j];
					cnt++;
				}
			}
			OOWP[i] /= cnt;

			RPI[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
			printf("%lf\n", RPI[i]);
		}
	}

	return 0;
}