#include <stdio.h>

const int MAXN = 1005;

FILE *fin = fopen("coaster.in", "r"), *fout = fopen("coaster.out", "w");
int T, R, k, N, g[MAXN];

int main() {
	fscanf(fin, "%d", &T);
	for (int t = 1; t <= T; t++) {
		fscanf(fin, "%d%d%d", &R, &k, &N);
		for (int i = 0; i < N; i++)
			fscanf(fin, "%d", g+i);
		int start, spot = 0, tot, bigtot = 0;
		for (int r = 0; r < R; r++) {
			start = spot, tot = g[spot];
			while (tot + g[(++spot) %= N] <= k && spot != start)
				tot += g[(spot) % N];
			bigtot += tot;
		}

		fprintf(fout, "Case #%d: %d\n", t, bigtot);
	}

	fclose(fin); fclose(fout);
	return 0;
}