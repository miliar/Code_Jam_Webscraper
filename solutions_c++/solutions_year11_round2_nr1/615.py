#include <stdio.h>

int main() {
	int T = 0;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		int N = 0;
		scanf("%d", &N);
		int won[100][100] = {{0}};
		int played[100][100] = {{0}};
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				char c = ' ';
				scanf(" %c", &c);
				if (c != '.') {
					played[i][j] = 1;
					won[i][j] = c == '1';
				}
			}
		}
		int wins[100] = {0};
		int games[100] = {0};
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if (played[i][j]) {
					++games[i];
					if (won[i][j]) ++wins[i];
				}
			}
		}
		//for (int i = 0; i < N; ++i) fprintf(stderr, "> %d/%d\n", wins[i], games[i]);
		double OWP[100] = {0};
		for (int i = 0; i < N; ++i) {
			double owp_sum = 0;
			int owp_count = 0;
			for (int j = 0; j < N; ++j) {
				if (!played[i][j]) continue;
				double owp = (double)(won[j][i] ? wins[j] - 1 : wins[j]) / (games[j] - 1);
				owp_sum += owp;
				++owp_count;
			}
			OWP[i] = owp_count == 0 ? 0 : owp_sum / owp_count;
		}
		//for (int i = 0; i < N; ++i) fprintf(stderr, "> OWP[%d] = %.12lf\n", i, OWP[i]);
		printf("Case #%d:\n", t + 1);
		for (int n = 0; n < N; ++n) {
			double rpi = 0;
			if (wins[n] > 0) rpi += 0.25 * (double)wins[n] / games[n];
			rpi += 0.5 * OWP[n];
			double oowp = 0;
			int oowp_count = 0;
			for (int k = 0; k < N; ++k) {
				if (played[n][k]) oowp += OWP[k], ++oowp_count;
			}
			if (oowp_count > 0) rpi += 0.25 * oowp / oowp_count;
			printf("%.12lf\n", rpi);
		}
	}
}
