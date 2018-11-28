#include <stdio.h>
#include <stdlib.h>

int n, na, nb, t, a[200], b[200];

int comp (const void * a, const void * b) {
	return *(int *)a - *(int *)b;
}

int main() {
	FILE * fin = fopen("Train Timetable.in", "r"), * fout = fopen("Train Timetable.out", "w");
	int i, j, h, c, m, ia, ib, sa, sb;
	fscanf(fin, "%d", &n);
	for (i = 1; i <= n; ++i) {
		fscanf(fin, "%d%d%d", &t, &na, &nb);
		for (j = 0; j < na; ++j) {
			fscanf(fin, "%d%c%d", &h, &c, &m);
			a[j] = ((h * 60 + m) << 1) ^ 1;
			fscanf(fin, "%d%c%d", &h, &c, &m);
			b[j] = (h * 60 + m + t) << 1;
		}
		for (nb += na; j < nb; ++j) {
			fscanf(fin, "%d%c%d", &h, &c, &m);
			b[j] = ((h * 60 + m) << 1) ^ 1;
			fscanf(fin, "%d%c%d", &h, &c, &m);
			a[j] = (h * 60 + m + t) << 1;
		}
		qsort(a, nb, 4, comp);
		qsort(b, nb, 4, comp);
		ia = 0;
		ib = 0;
		sa = 0;
		sb = 0;
		for (j = 0; j < nb; ++j) {
			if (a[j] & 1) {
				if (ia) {
					--ia;
				} else {
					++sa;
				}
			} else {
				++ia;
			}
			if (b[j] & 1) {
				if (ib) {
					--ib;
				} else {
					++sb;
				}
			} else {
				++ib;
			}
		}
		fprintf(fout, "Case #%d: %d %d\n", i, sa, sb);
	}
	return 0;
}
