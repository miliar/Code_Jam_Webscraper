#include <cstdio>

FILE *in, *out;
const int MAX_N = 105;
int played[MAX_N][MAX_N], T, N;

double calcWP(int team, int dis = -1) {
	double avg = 0;
	int total = 0;
	for (int i = 0; i < N; ++i) {
		if (played[team][i] == -1 || i == dis) continue;
		avg += played[team][i];
		total++;
	}
	return avg/total;
}

double calcOWP(int team) {
	double avg = 0;
	int total = 0;
	for (int i = 0; i < N; ++i) {
		if (i == team || played[team][i] == -1) continue;
		avg += calcWP(i, team);
		total++;
	}
	return avg/total;
}

double calcOOWP(int team) {
	double avg = 0;
	int total = 0;
	for (int i = 0; i < N; ++i) {
		if (i == team || played[team][i] == -1) continue;
		avg += calcOWP(i);
		total++;
	}
	return avg/total;
}


void solve() {
	for (int i = 0; i < N; ++i) {
		double rpi = 0.25*calcWP(i) + 0.5*calcOWP(i) + 0.25*calcOOWP(i);
		fprintf(out, "%lf\n", rpi);
	}
}

int main() {
	in = fopen("datain.txt", "r"); out = fopen("dataout.txt", "w");
	fscanf(in, "%d", &T);
	for (int t = 1; t <= T; ++t) {
		fscanf(in, "%d ", &N);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				char ch = fgetc(in);
				played[i][j] = (ch == '1' ? 1 : ch == '0' ? 0 : -1);
			}
			fscanf(in, " ");
		}
		fprintf(out, "Case #%d:\n", t);
		solve();
	}
}