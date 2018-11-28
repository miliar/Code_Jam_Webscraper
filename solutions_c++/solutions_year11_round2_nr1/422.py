#include <cstdio>

int contest[200][200];
double score[3][200];
double total[200];
int N, T;
double IRP[200];

void Open() {
	freopen ("P1.in", "r", stdin);
	freopen ("P1.out", "w", stdout);
}

void Close() {
	fclose(stdin);
	fclose(stdout);
}

void init() {
	scanf ("%d\n", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			char tmp;
			scanf ("%c", &tmp);
			if (tmp == '.') contest[i][j] = 0; else 
			if (tmp == '0') contest[i][j] = -1; else
			if (tmp == '1') contest[i][j] = 1; 
		}
		scanf ("\n");
	}
}

void calc() {
	for (int i = 0; i < N; i++) {
		total[i] = 0;
		for (int j = 0; j < N; j++)
			if (contest[i][j] != 0)
				total[i] += 1.0;
	}

	for (int i = 0; i < N; i++) {
		score[0][i] = 0;
		for (int j = 0; j < N; j++) {
			if (contest[i][j] == 1)
				score[0][i] += 1.0;
		}
		score[0][i] /= total[i];
	}

	for (int i = 0; i < N; i++) {
		score[1][i] = 0;
		for (int j = 0; j < N; j++) {
			if (contest[i][j] == 0) continue;
			if (contest[j][i] == 1) 
				score[1][i] += (score[0][j] * total[j] - 1) / (total[j] - 1);
			else
				score[1][i] += score[0][j] * total[j] / (total[j] - 1);
		}
		score[1][i] /= total[i];
	}

	for (int i = 0; i < N; i++) {
		score[2][i] = 0;
		for (int j = 0; j < N; j++) {
			if (contest[i][j] == 0) continue;
			score[2][i] += score[1][j];
		}
		score[2][i] /= total[i];
	}

	for (int i = 0; i < N; i++)
		IRP[i] = 0.25 * score[0][i] + 0.5 * score[1][i] + 0.25 * score[2][i];
}

void output(int caseNo) {
	printf ("Case #%d:\n", caseNo);
	for (int i = 0; i < N; i++) {
		printf ("%0.8lf\n", IRP[i]);
	}
}

void work() {
	scanf ("%d", &T);
	for (int caseNo = 1; caseNo <= T; caseNo++) {
		init();
		calc();
		output(caseNo);
	}
}

int main() {
	Open();
	work();
	Close();
	return 0;
}