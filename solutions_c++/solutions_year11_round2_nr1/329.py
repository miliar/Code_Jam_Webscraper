#include <cstdio>

int n;
double wp[105];
double owp[105];
double oowp[105];

int main() {
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
		int r;
		int case_no = 0;
		char games[105][105];
		scanf("%d", &r);
		while (r--) {
				scanf("%d", &n);
				for (int i = 0; i < n; ++i)
						scanf("%s", games[i]);

				// wp
				for (int i = 0; i < n; ++i) {
						wp[i] = 0.0;
						int win = 0, total = 0;
						for (int j = 0; j < n; ++j) {
								if (games[i][j] == '.') continue;
								total++;
								if (games[i][j] == '1') win++;
						}
						if (win == 0) wp[i] = 0.0;
						else wp[i] = win / (double)total;
				}

				// owp
				for (int i = 0; i < n; ++i) {
						owp[i] = 0.0;
						int cnt = 0;
						for (int j = 0; j < n; ++j) {
								if (games[i][j] == '.') continue;
								cnt++;
								int win = 0, total = 0;
								for (int k = 0; k < n; ++k) {
										if (k != i && games[j][k] != '.') {
												total++;
												if (games[j][k] == '1') win++;
										}
								}
								if (total != 0) {
										owp[i] += win / (double)total;
								}
						}
						if (cnt != 0) {
								owp[i] /= cnt;
						}
				}

				for (int i = 0; i < n; ++i) {
						oowp[i] = 0.0;
						int total = 0;
						for (int j = 0; j < n; ++j) {
								if (games[i][j] != '.') {
										oowp[i] += owp[j];
										total++;
								}
						}
						if (total != 0) oowp[i] /= total;
				}

				printf("Case #%d:\n", ++case_no);
				for (int i = 0; i < n; ++i)
						printf("%.7lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
		return 0;
}