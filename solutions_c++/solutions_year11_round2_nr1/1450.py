#include <cstdio>

int const N_SIZE = 105;

int g[N_SIZE][N_SIZE];
double wpa[N_SIZE];
double wpb[N_SIZE];
double owp[N_SIZE];
double oowp[N_SIZE];
double rpi[N_SIZE];

int main()
{
	freopen("a1.in", "r", stdin);
	freopen("b1.out", "w", stdout);	
	int testCount, nCount;
	scanf("%d", &testCount);
	for (int tc = 1; tc <= testCount; tc++) {
		scanf("%d", &nCount);
		for (int i = 0; i != nCount; i++)
			for (int j = 0; j != nCount; j++) {
				char ch;
				scanf(" %c", &ch);
				if (ch == '.')
					g[i][j] = -1;
				else
					g[i][j] = ch - '0';
			}
		for (int i = 0; i != nCount; i++) {
			wpa[i] = wpb[i] = 0;
			for (int j = 0; j != nCount; j++)
				if (g[i][j] != -1) {
					wpb[i]++;
					if (g[i][j] == 1)
						wpa[i]++;
				}
		}
		double d;
		for (int i = 0; i != nCount; i++) {
			owp[i] = 0;
			for (int j = 0; j != nCount; j++) {
				if (i == j || g[j][i] == -1)
					continue;
				if (g[j][i] == 0)
					d = 1.0 * wpa[j] / (wpb[j] - 1.0);
				else if (g[j][i] == 1)
					d = (wpa[j] - 1) / (wpb[j] - 1.0);
				owp[i] += d;			
			}
			owp[i] /= wpb[i];
		}
		printf("Case #%d:\n", tc);
		for (int i = 0; i != nCount; i++) {
			oowp[i] = 0;
			for (int j = 0; j != nCount; j++) {
				if (i == j || g[i][j] == -1)
					continue;
				oowp[i] += owp[j];
			}
			oowp[i] /= wpb[i];
			rpi[i] = (0.25 * wpa[i]) / wpb[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf("%.6lf\n", rpi[i]);
		}
	}
	return 0;
}
