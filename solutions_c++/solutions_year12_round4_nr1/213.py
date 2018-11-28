#include <cstdio>

int N, d[10000], l[10000], m[10000], D;

int solve() {
	int i, j;
	for (i = 0; i < N && m[i]; ++i) {
		for (j = i + 1; j < N && d[j] - d[i] <= m[i]; ++j) {
			if (!m[j]) {
				if (d[j] - d[i] > l[j]) {
					m[j] = l[j];
				} else {
					m[j] = d[j] - d[i];
				}
				if (m[j] + d[j] >= D) {
					return 1;
				}
			}
		}
	}
	return 0;
}

int main() {
	FILE * fin = fopen("input.in", "r"), * fout = fopen("output.out", "w");
	int T, t, i;
	fscanf(fin, "%d\n", &T);
	for (t = 1; t <= T; ++t) {
		fscanf(fin, "%d", &N);
		for (i = 0; i < N; ++i) {
			fscanf(fin, "%d%d", d + i, l +i);
			m[i] = 0;
		}
		fscanf(fin, "%d", &D);
		m[0] = d[0];
		if (m[0] + d[0] >= D || solve()) {
			fprintf(fout, "Case #%d: YES\n", t);
		} else {
			fprintf(fout, "Case #%d: NO\n", t);
		}
	}
	return 0;
}

