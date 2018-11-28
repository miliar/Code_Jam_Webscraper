#include <stdio.h>

char table[105][105];
int counter[105];
int win[105];
double OWPtable[105][105];
double OOWP[105];
double OWP[105];

int main()
{
	int C, N;
	scanf("%d", &C);
	for (int cases = 0; cases < C; cases ++) {
		scanf("%d", &N);
		for (int i=0; i<N; i++)
		{
			scanf("%s", table[i]);
		}

		for (int i = 0; i<N; i++)
		{
			counter[i] = 0;
			win[i] = 0;
			OWP[i] = 0.0;
			OOWP[i] = 0.0;
			for (int j = 0; j<N; j++) {
				OWPtable[i][j] = 0.0;
			}
		}

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j<N; j++) {
				if (table[i][j] != '.')		counter[i] ++;
				if (table[i][j] == '1')		win[i] ++;
			}
		}

		for (int i = 0; i<N; i++) {
			for (int j = 0; j<N; j++) {
				if (table[i][j] == '.')	continue;

				OWPtable[i][j] = (double)(win[j]-(table[i][j]=='0'))/(double)(counter[j]-1);
			}
		}

		for (int i = 0; i<N; i++) {
			double tmp = 0.0;
			int c = 0;
			for (int j = 0; j<N; j++) {
				if (table[i][j]=='.')	continue;
				c++;
				tmp += OWPtable[i][j];
			}
			OWP[i] = tmp / c;
		}

		printf("Case #%d:\n", cases+1);
		for (int i = 0; i<N; i++) {
			double ans = (double)win[i] / (double)counter[i] * 0.25;
			ans += 0.5 * OWP[i];
			double tmp = 0.0;
			int c = 0;
			for (int j = 0; j<N; j++) {
				if (table[i][j] == '.')	continue;
				c++;
				tmp += OWP[j];
			}
			tmp /= c;
			ans += 0.25 * tmp;
			printf("%.16f\n", ans);
		}
	}

	return 0;
}
