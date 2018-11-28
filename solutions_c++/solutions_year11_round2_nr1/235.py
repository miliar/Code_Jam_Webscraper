#include <cstdio>

using namespace std;

const int MAXN = 110;

int n;
int opponents[MAXN];
char schedule[MAXN][MAXN];
double rpi[MAXN], owp[MAXN];

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int tests;
	scanf("%d ", &tests);
	for (int t = 1; t <= tests; ++t) {
		scanf("%d ", &n);
		for (int i = 0; i < n; ++i)
			fgets(schedule[i], MAXN, stdin);

		for (int i = 0; i < n; ++i)
			rpi[i] = owp[i] = 0;

		for (int i = 0; i < n; ++i) {
			int total = 0, wins = 0;
			for (int j = 0; j < n; ++j) {
				if (schedule[i][j] != '.')
					++total;
				if (schedule[i][j] == '1')
					++wins;
			}

			rpi[i] = 0.25 * (double) wins/total;
		}

		for (int i = 0; i < n; ++i) {
			opponents[i] = 0;
			double sum = 0;
			for (int j = 0; j < n; ++j) 
				if (schedule[i][j] != '.') {
					++opponents[i];
					int total = 0, wins = 0;
					for (int k = 0; k < n; ++k)
						if (k != i) {
							if (schedule[j][k] != '.')
								++total;
							if (schedule[j][k] == '1')
								++wins;
						}
					sum += (double) wins / total;
				}
			owp[i] = sum / opponents[i];
			rpi[i] += 0.5*owp[i];
		}

		for (int i = 0; i < n; ++i) {
			double sum = 0;
			for (int j = 0; j < n; ++j)
				if (schedule[i][j] != '.')
					sum += owp[j];

			rpi[i] += 0.25 * (sum / opponents[i]);
		}

		printf("Case #%d:\n", t);
		for (int i = 0; i < n; ++i)
			printf("%.12lf\n", rpi[i]);
	}

	return 0;
}
