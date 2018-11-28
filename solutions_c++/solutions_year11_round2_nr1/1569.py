#include <cstdio>
using namespace std;


int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t, T, i, j, n;
	double w[200], o[200], oo[200];
	int pl[200];
	char s[200][200];
	int won[200];
	for (t = 1, scanf("%d", &T); t <= T; t++) {
		scanf("%d", &n);
		for (i = 0; i < n; i++) {
			scanf("%s", s[i]);
		}
		printf("Case #%d:\n", t);
		for (i = 0; i < n; i++) {
			won[i] = 0;
			pl[i] = 0;
			for (j = 0; j < n; j++) {
				if (s[i][j] == '1') {
					won[i]++;
					pl[i]++;
				} else {
					if (s[i][j] == '0') pl[i]++;
				}
			}
			w[i] = 1.0 * won[i] / pl[i];
			//printf("%.5f  :%d out of %", w[i], won, p);
		}
		for (i = 0; i < n; i++) {
			double t = 0;
			//printf("%d\n", i);
			for (j = 0; j < n; j++) {
				if (s[i][j] != '.') {
					//printf("against %d: %d %d ", j,won[j]-(s[j][i]-'0'),pl[j]-1);
					//printf("t += %.5f\n", 1.0 * (won[j]-(s[j][i]-'0')) / (pl[j] - 1));
					t += 1.0 * (won[j] - (s[j][i] - '0')) / (pl[j] - 1);
				}
			}
			o[i] = t / (pl[i]);
			//printf("%.5f  :%.5f out of %d opponents\n", o[i], t, pl[i]-1);
		}
		for (i = 0; i < n; i++) {
			double t = 0;
			for (j = 0; j < n; j++) {
				if (s[i][j] != '.') t += o[j];
			}
			oo[i] = t / pl[i];
			//printf("%d - %.5f\n", i, oo[i]);
		}
		for (i = 0; i < n; i++) {
			printf("%.10f\n", 0.25 * w[i] + 0.5 * o[i] + 0.25 * oo[i]);
		}
	}
	fclose(stdout);
	return 0;
}
