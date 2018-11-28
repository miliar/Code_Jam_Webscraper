#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct DA {
	short D;
	short A;
	int na;
	int u;
};

int cmp_da(DA *a, DA *b)
{
	return a->D - b->D;
}

int main(int argc, char**argv)
{
	int Cn;

	fscanf(stdin, "%d\n", &Cn);
	for (int Ci=0; Ci < Cn; Ci++) {
		int T;
		int NA, NB;
		fscanf(stdin, "%d\n", &T);
		fscanf(stdin, "%d %d\n", &NA,  &NB);

		struct DA da[300] = {};
		int dai = 0;

		for (int i = 0; i < NA; i++) {
			int dh, ds, ah, as;
			fscanf(stdin, "%d:%d %d:%d\n", &dh, &ds, &ah, &as);
			da[dai].D = dh*60+ds;
			da[dai].A = ah*60+as;
			da[dai].na = 1;
			dai++;
		}
		for (int i = 0; i < NB; i++) {
			int dh, ds, ah, as;
			fscanf(stdin, "%d:%d %d:%d\n", &dh, &ds, &ah, &as);
			da[dai].D = dh*60+ds;
			da[dai].A = ah*60+as;
			da[dai].na = 0;
			dai++;
		}

		qsort(da, NA+NB, sizeof(DA), (int(*)(const void*, const void*))cmp_da);

		// solve
		int N = NA+NB;
		int n[2] = {};
		for (int i = 0; i < N; i++) {
			if (da[i].u) {
				continue;
			}
			da[i].u = 1;
			n[da[i].na]++;
			DA tmp = da[i];
			for (int j = i+1; j < N; j++) {
				if (da[j].u) { continue; }
				if (tmp.na == da[j].na) { continue; }
				if (tmp.A + T <= da[j].D) {
					da[j].u = 1;
					tmp = da[j];
				}
			}
		}

		printf("Case #%d: %d %d\n", Ci+1, n[1], n[0]);
	}

	return 0;
}
