#include <cstdio>

int t, n;

int main() {
	FILE * fin = fopen("candy_splitting.in", "r"), * fout = fopen("candy_splitting.out", "w");
	int i, j, c, xor, total, min;
	fscanf(fin, "%d", &t);
	for (i = 0; i < t; ++i) {
		xor = 0;
		total = 0;
		min = 10000000;
		fscanf(fin, "%d", &n);
		for (j = 0; j < n; ++j) {
			fscanf(fin, "%d", &c);
			xor ^= c;
			total += c;
			if (min > c) {
				min = c;
			}
		}
		if (xor) {
			fprintf(fout, "Case #%d: NO\n", i + 1);
		} else {
			fprintf(fout, "Case #%d: %d\n", i + 1, total - min);
		}
	}
	return 0;
}