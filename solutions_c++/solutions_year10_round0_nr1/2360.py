#include <stdio.h>

FILE *fin = fopen("snapper.in", "r"), *fout = fopen("snapper.out", "w");

int main() {
	int T, N, K;
	fscanf(fin, "%d", &T);
	for (int t = 0; t < T; t++) {
		fscanf(fin, "%d%d", &N, &K);
		fprintf(fout, "Case #%d: %s\n", t+1, ((K + 1) % (1 << N) == 0) ? "ON" : "OFF");
	}

	fclose(fin); fclose(fout);
	return 0;
}