#include <cstdio>



int main() {
	FILE * fin = fopen("gorosort.in", "r"), * fout = fopen("gorosort.out", "w");
	int t, n, i, j, x;
	double a;
	fscanf(fin, "%d", &t);
	for (i = 1; i <= t; ++i) {
		a = 0;
		fscanf(fin, "%d", &n);
		for (j = 1; j <= n; ++j) {
			fscanf(fin, "%d", &x);
			if (x != j) {
				a += 1;
			}
		}
		fprintf(fout, "Case #%d: %f\n", i, a);
	}
	return 0;
}
