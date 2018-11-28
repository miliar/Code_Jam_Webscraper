#include <cstdio>

double WP[110], OWP[110], OOWP[110], comp[110];
char G[110][110];

int main() {
	int T, n;
	scanf("%d", &T);
	for (int t=0; t<T; ++t) {
		scanf("%d", &n);

		for (int i=0; i<n; ++i) {
			scanf("%s", G[i]);

			int win = 0, tot = 0;
			for (int j=0; j<n; ++j) {
				if (G[i][j] != '.') ++tot;
				if (G[i][j] == '1') ++win;
			}
			WP[i] = double(win) / tot;
			comp[i] = tot;
		}

		for (int i=0; i<n; ++i) {
			int tot = 0;
			double ret = .0;
			for (int j=0; j<n; ++j) if (G[i][j] != '.') {
				++tot;
				double delta = WP[j];
				if (G[j][i] == '1') {
					delta = (delta * comp[j] - 1) / (comp[j] - 1);
				}
				else {
					delta = (delta * comp[j]) / (comp[j] - 1);
				}
				ret += delta;
			}
			OWP[i] = ret / tot;
		}

		for (int i=0; i<n; ++i) {
			int tot = 0;
			double ret = .0;
			for (int j=0; j<n; ++j) if (G[i][j] != '.') {
				++tot;
				ret += OWP[j];
			}
			OOWP[i] = ret / tot;
		}

		printf("Case #%d:\n", t+1);
		for (int i=0; i<n; ++i) {
			double ret = 0;
			ret = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i];
			printf("%.8lf\n", ret);
		}
	}
	return 0;
}
