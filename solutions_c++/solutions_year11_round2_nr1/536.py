#include <cstdio>
#include <cstring>

using namespace std;

char score[100][101];
int N;

int win[100], total[100];
double wp[100];
double owp[100];
double oowp[100];

void solve() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
		scanf("%s", score[i]);

	memset(win, 0, sizeof win);
	memset(total, 0, sizeof total);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (score[i][j] != '.') total[i]++;
			if (score[i][j] == '1') win[i]++;
		}
		wp[i] = double(win[i]) / total[i];
	}

	for (int i = 0; i < N; i++) {
		double sum = 0; int count = 0;
		for (int j = 0; j < N; j++)
			if (score[i][j] != '.') {
				sum += double(win[j] - (score[j][i] - '0')) / (total[j] - 1);
				count++;
			}
		owp[i] = sum / count;
	}

	for (int i = 0; i < N; i++) {
		double sum = 0; int count = 0;
		for (int j = 0; j < N; j++)
			if (score[i][j] != '.') {
				sum += owp[j];
				count++;
			}
		oowp[i] = sum / count;
	}

	for (int i = 0; i < N; i++)
		printf("%.9lf\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
}

int main() {
	int T; scanf("%d\n", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d:\n", i);
		solve();
	}

	return 0;
}
