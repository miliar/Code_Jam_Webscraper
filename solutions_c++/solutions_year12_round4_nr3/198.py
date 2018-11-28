#include <cstdio>

int N, x[2000], y[2000];

int solve(int a, int d, int c) {
	if (c == d) {
		return 1;
	}
	if (x[c] < d) {
		if (!solve(a, d, x[c])) return 0;
		y[c] = y[x[c]] - ((y[d] - y[x[c]]) / (d - x[c]) + 1) * (x[c] - c);
		return solve(c, x[c], c + 1);
	} else if (x[c] == d) {
		y[c] = y[a] + (((y[d] - y[a]) / (d - a)) * (c - a) - 1);
		return solve(c, d, c + 1);
	}
	return 0;
}

		
int main() {
	FILE * fin = fopen("input.in", "r"), * fout = fopen("output.out", "w");
	int T, t, i;
	fscanf(fin, "%d\n", &T);
	for (t = 1; t <= T; ++t) {
		fscanf(fin, "%d", &N);
		for (i = 0; i < N - 1; ++i) {
			fscanf(fin, "%d", x + i);
			--x[i];
			y[i] = -1;
		}
		y[0] = 1000000000;
		for (i = 0; i < N - 1; i = x[i]) {
			y[x[i]] = y[i];
			if (!solve(i, x[i], i + 1)) {
				break;
			}
		}
		if (i == N - 1) {
			fprintf(fout, "Case #%d:", t);
			for (i = 0; i < N; ++i) {
				fprintf(fout, " %d", y[i]);
			}
			fprintf(fout, "\n");
		} else {
			fprintf(fout, "Case #%d: Impossible\n", t);
		}
	}
	return 0;
}
