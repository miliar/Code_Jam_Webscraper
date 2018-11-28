#include <cstdio>

int schedule[100][100], wp[100][2];
double owp[100], oowp[100];

int main() {
	FILE * fin = fopen ("rpi.in", "r"), * fout = fopen("rpi.out", "w");
	int T, cs, n, i, j, t;
	char in;
	fscanf(fin, "%d", &T);
	for (cs = 1; cs <= T; ++cs) {
		fscanf(fin, "%d", &n);
		for (i = 0; i < n; ++i) {
			fscanf(fin, "%c", &in);
			wp[i][0] = 0;
			wp[i][1] = 0;
			owp[i] = 0;
			oowp[i] = 0;
			if (in != '\n') {
				printf("input error");
				return 1;
			}
			for (j = 0; j < n; ++j) {
				fscanf(fin, "%c", &in);
				switch (in) {
				case '.':
					schedule[i][j] = -1;
					break;
				case '0':
					schedule[i][j] = 0;
					++wp[i][1];
					break;
				case '1':
					schedule[i][j] = 1;
					++wp[i][0];
					++wp[i][1];
					break;
				default:
					break;
				}
			}
		}
		for (i = 0; i < n; ++i) {
			t = 0;
			for (j = 0; j < n; ++j) {
				if (schedule[i][j] != -1) {
					++t;
					owp[i] += ((double)(wp[j][0] - schedule[j][i]))/((double)(wp[j][1] - 1));
				}
			}
			owp[i] /= (double)t;
		}
		for (i = 0; i < n; ++i) {
			t = 0;
			for (j = 0; j < n; ++j) {
				if (schedule[i][j] != -1) {
					++t;
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= (double)t;
		}
		fprintf(fout, "Case #%d:\n", cs);
		for (i = 0; i < n; ++i) {
			fprintf(fout, "%lf\n", 0.25 * (((double)wp[i][0]) / ((double)wp[i][1])) + 0.5 * owp[i] + 0.25 * oowp[i]);
		}
	}
	return 0;
}
