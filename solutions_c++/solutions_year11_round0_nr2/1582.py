#include <stdio.h>
#include <stdlib.h>

#include <algorithm>

FILE* fid;
FILE* fout;


using namespace std;

char combinations[256][256];
char oppositions[256][256];

char elout[200];


char* solve() {

	// Yes, this is memory inefficent but meh
	for (int y=0; y < 256; y++) {
		for (int x=0; x < 256; x++) {
			combinations[x][y] = '\0';
			oppositions[x][y] = 0;
		}
	}

	int C, D, N;

	fscanf(fid, "%d ", &C);

	for (int i=0; i < C; i++) {
		char buf[4];

		fscanf(fid, " %s ", buf);

		combinations[buf[0]][buf[1]] = combinations[buf[1]][buf[0]] = buf[2];
	}

	fscanf(fid, "%d ", &D);

	for (int i=0; i < D; i++) {
		char buf[4];

		fscanf(fid, " %s ", buf);

		//printf("Opp: '%s'\n", buf);

		oppositions[buf[0]][buf[1]] = oppositions[buf[1]][buf[0]] = 1;
	}

	fscanf(fid, "%d ", &N);

	char elements[150];

	fscanf(fid, " %s ", elements);

	char elindex = 0;

lp:	for (int i = 0; i < N; i++) {
		elout[elindex++] = elements[i];

		int oppositionallowed = 1;

		if (elindex >= 2) {
			// A combination may be possible

			char subst = combinations[elout[elindex-2]][elout[elindex-1]];

			if (subst) {
				elout[--elindex - 1] = subst;
				oppositionallowed = 0;
			}
		}

		if (oppositionallowed) {

			for (int j = 0; j < elindex-1; j++) {

				//printf(" CO(%c%c) = %d\n", elout[j], elout[elindex-1], (int)oppositions[elout[j]][elout[elindex-1]]);

				if (oppositions[elout[j]][elout[elindex-1]]) {
					// Clear all
					elindex = 0;

					break;
				}

			}

		}

		elout[elindex] = '\0';

		//printf("  {%s}\n", elout);

	}

	elout[elindex] = '\0';

	return elout;
}

int main(int argc, char** argv) {

	fid = fopen("B-large.in", "r");
	fout = fopen("B.out", "w");

	int T;
	fscanf(fid, "%d", &T);

	for (int i = 1; i <= T; i++) {

		solve();

		fprintf(fout, "Case #%d: [", i);

		for (char* j = elout; *j; ++j) {
			if (elout != j)
				fprintf(fout, ", ");

			fprintf(fout, "%c", *j);
		}

		fprintf(fout, "]\n");
	}

	return 0;
}