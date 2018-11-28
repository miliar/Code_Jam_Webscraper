#include <cstdio>
#include <cstring>

const int EMAX = 2048;
const int LEV = 24 * 60;
const int HMIN = 60;

int main(void) {
	FILE *fin = fopen("large.in", "rt");
	FILE *fout = fopen("test.out", "wt");

	int N, T, NA, NB;
	int ee, es, i, j, h, m;
	int na, nb, RA, RB;
	int EA[EMAX], EB[EMAX];

	fscanf(fin, " %d", &N);

	for (i = 1; i <= N; ++i) {
		fscanf(fin, " %d", &T);

		fscanf(fin, " %d %d", &NA, &NB);

		memset(EA, 0x00, sizeof(EA));
		memset(EB, 0x00, sizeof(EB));
		for (j = 0; j < NA + NB; ++j) {
			fscanf(fin, " %d:%d", &h, &m);
			es = h * HMIN + m;

			fscanf(fin, " %d:%d", &h, &m);
			ee = h * HMIN + m + T;
			
			if (j < NA)
				--EA[es], ++EB[ee];
			else
				--EB[es], ++EA[ee];
		}
		
		na = nb = 0; RA = RB = 0;
		for (j = 0; j < LEV; ++j) {
			na += EA[j];
			nb += EB[j];

			if (na < 0) RA -= na, na = 0;
			if (nb < 0) RB -= nb, nb = 0;
		}

		fprintf(fout, "Case #%d: %d %d\n", i, RA, RB);
	}


	fclose(fin);
	fclose(fout);
	return 0;
}
