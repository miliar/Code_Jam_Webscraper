#include <stdio.h>
#include <memory.h>

int C, N, M, ans[2000], malted[2000], n[2000], m[2000], unmalted[2000][2000];

int malt(int x) {
	int i;
	ans[x] = 1;
	for (i = 0; i < n[x]; ++i) {
		if (!(--m[unmalted[x][i]])) {
			if (malted[unmalted[x][i]] != -1) {
				if (!malt(malted[unmalted[x][i]])) {
					return 0;
				}
			} else {
				return 0;
			}
		}
	}
	return 1;
}

int main() {
	FILE * fin = fopen("Milkshakes.in", "r"), * fout = fopen("Milkshakes.out", "w");
	int i, j, k, t, x;
	fscanf(fin, "%d", &C);
	for (i = 1; i <= C; ++i) {
		memset(ans, 0, 8000);
		memset(n, 0, 8000);
		memset(unmalted, 0, 16000000);
		fscanf(fin, "%d%d", &N, &M);
		for (j = 0; j < M; ++j) {
			fscanf(fin, "%d", &m[j]);
			malted[j] = -1;
			for (k = 0; k < m[j]; ++k) {
				fscanf(fin, "%d%d", &x, &t);
				--x;
				if (t) {
					malted[j] = x;
					--k;
					--m[j];
				} else {
					unmalted[x][n[x]] = j;
					++n[x];
				}
			}
		}
		for (k = 0; k < M; ++k) {
			if (!m[k]) {
				if (malted[k] == -1) {
					break;
				}
				if (!malt(malted[k])) {
					break;
				}
			}
		}
		if (k != M) {
			fprintf(fout, "Case #%d: IMPOSSIBLE\n", i);
		} else {
			fprintf(fout, "Case #%d:", i);
			for (j = 0; j < N; ++j) {
				fprintf(fout, " %d", ans[j]);
			}
			fprintf(fout, "\n");
		}
	}
	return 0;
}