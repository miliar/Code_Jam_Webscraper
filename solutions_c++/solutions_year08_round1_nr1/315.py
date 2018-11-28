#include <stdio.h>
#include <stdlib.h>

int incr(const void * a, const void * b) {
	return *(int *)a - *(int *)b;
}

int decr(const void * a, const void * b) {
	return *(int *)b - *(int *)a;
}

int main() {
	int T, n, x[800], y[800], i, j;
	__int64 a;
	FILE * fin = fopen("Minimum Scalar Product.in", "r"), * fout = fopen("Minimum Scalar Product.out", "w");
	fscanf(fin, "%d", &T);
	for (i = 1; i <= T; ++i) {
		fscanf(fin, "%d", &n);
		for (j = 0; j < n; ++j) {
			fscanf(fin, "%d", x + j);
		}
		for (j = 0; j < n; ++j) {
			fscanf(fin, "%d", y + j);
		}
		qsort(x, n, 4, incr);
		qsort(y, n, 4, decr);
		a = 0;
		for (j = 0; j < n; ++j) {
			a += (__int64)x[j] * (__int64)y[j];
		}
		fprintf(fout, "Case #%d: %lld\n", i, a);
	}
	return 0;
}