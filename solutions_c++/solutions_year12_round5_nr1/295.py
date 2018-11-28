#include <cstdio>
#include <cstdlib>
#include <cmath>

int l[1000], p[1000], index[1000], n;

int comp(const void * a, const void * b) {
	int x, y;
	double c, d;
	x = *(int *)a;
	y = *(int *)b;
	c = pow(1 - p[x] / 100.0, 1.0 / l[x]);
	d = pow(1 - p[y] / 100.0, 1.0 / l[y]);
	if (abs(c - d) < .0000001) {
		return x - y;
	}
	if (c > d) {
		return 1;
	}
	return -1;
}

int main() {
	FILE * fin = fopen("input.in", "r"), * fout = fopen("output.out", "w");
	int T, t, i;
	fscanf(fin, "%d\n", &T);
	for (t = 1; t <= T; ++t) {
		fscanf(fin, "%d", &n);
		for (i = 0; i < n; ++i) {
			fscanf(fin, "%d", l + i);
			index[i] = i;
		}
		for (i = 0; i < n; ++i) {
			fscanf(fin, "%d", p + i);
		}
		qsort(index, n, sizeof(int), comp);
		fprintf(fout, "Case #%d:", t);
		for (i = 0; i < n; ++i) {
			fprintf(fout, " %d", index[i]);
		}
		fprintf(fout, "\n");
	}
	return 0;
}
