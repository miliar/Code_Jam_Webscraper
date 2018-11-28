#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int n, s, q, nu, u[100];
char * e[100], name[100][102], c[102];

int comp(const void * a, const void * b) {
	return strcmp(*(char **)a, *(char **)b);
}

int main() {
	FILE * fin = fopen("Saving the Universe.in", "r"), * fout = fopen("Saving the Universe.out", "w");
	int i, j, k, l, x;
	fscanf(fin, "%d", &n);
	for (i = 1; i <= n; ++i) {
		fscanf(fin, "%d\n", &s);
		for (j = 0; j < s; ++j) {
			e[j] = fgets(name[j], 102, fin);
		}
		qsort(e, s, 4, comp);
		nu = 0;
		memset(u, 0, 400);
		x = 0;
		fscanf(fin, "%d\n", &q);
		for (j = 0; j < q; ++j) {
			fgets(c, 102, fin);
			k = 0;
			l = s;
			while (k + 1 != l) {
				if (strcmp(c, e[(k + l) >> 1]) >= 0) {
					k += l;
					k >>= 1;
				} else {
					l += k;
					l >>= 1;
				}
			}
			if (!u[k]) {
				if (nu + 1 != s) {
					++nu;
				} else {
					memset(u, 0, 400);
					nu = 1;
					++x;
				}
				u[k] = 1;
			}
		}
		fprintf(fout, "Case #%d: %d\n", i, x);
	}
	return 0;
}
