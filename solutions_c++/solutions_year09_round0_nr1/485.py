#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int dict[5000][15];  // [D][L]
int patt[15];        // [L]

int main() {
	FILE* fid = fopen("A-large.in", "r");
	FILE* fout = fopen("AA.out", "w");

	int L, D, N;

	fscanf(fid, "%d%d%d", &L, &D, &N);


	char buf[600];

	for (int i = 0; i < D; i++) {
		fscanf(fid, "%s", buf);

		//printf("Test W: \"%s\"\n", buf);

		for (int j=0; j < L; j++) {
			dict[i][j] = 1 << (buf[j]-'a');
		}
	}

	for (int cas = 1; cas <= N; ++cas) {

		fscanf(fid, "%s", buf);

		//printf("Test P: \"%s\"\n", buf);


		char *ptr = buf;

		for (int j=0; j < L; j++) {
			if ('(' == *ptr) {
				patt[j] = 0;
				++ptr;

				while (')' != *ptr) {
					patt[j] |= 1 << (*ptr - 'a');
					++ptr;
				}

				++ptr;

			} else {
				patt[j] = 1 << (*ptr - 'a');
				++ptr;
			}
		}


		int count = 0;


		for (int i=0; i < D; i++) {
			for (int j=0; j < L; j++) {
				if (0 == (dict[i][j] & patt[j])) {
					goto loop;
				}
			}
			++count;
			loop:;
		}

		fprintf(fout, "Case #%d: %d\n", cas, count);

	}


	return 0;
}

