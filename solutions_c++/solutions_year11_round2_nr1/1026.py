#include <stdio.h>

int total[100];
int win[100][100];
bool played[100][100];
int wincount[100];
double owp[100][100];
double score[100];
double owpresult[100];

int N;

double calcowp(int team) {
	double ret = 0;
	for (int i = 0; i < N; i++) {
		if (i == team) {
			continue;
		}
		if (played[i][team]) {
			owp[i][team] = (double)(wincount[i] - win[i][team]) / (total[i] - 1);
			ret += owp[i][team];
		}
	}
	ret /= total[team];
	owpresult[team] = ret;
	return ret;
}

int main() {
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				win[i][j] = 0;
				owp[i][j] = 0;
				played[i][j] = 0;
			}
			total[i] = 0;
			wincount[i] = 0;
			owpresult[i] = 0;
		}
		char winline[101];
		scanf("%d", &N);

		for (int i = 0; i < N; i++) {
			scanf("%s", winline);
			for (int j = 0; j < N; j++) {
				if (winline[j] == '1') {
					win[i][j] = 1;
					wincount[i]++;
					played[i][j] = played[j][i] = true;
				}
				if (winline[j] != '.') {
					total[i]++;
				}
			}

			score[i] = 0.25 * wincount[i] / total[i];
		}

		for (int i = 0; i < N; i++) {
			score[i] += 0.5 * calcowp(i);
		}

		printf("Case #%d:\n", t);
		for (int i = 0; i < N; i++) {
			double avg = 0;
			for (int j = 0; j < N; j++) {
				if (played[i][j]) {
					avg += owpresult[j];
				}
			}
			avg /= total[i];
			score[i] += 0.25 * avg;
			printf("%lf\n", score[i]);
		}
	}
}
