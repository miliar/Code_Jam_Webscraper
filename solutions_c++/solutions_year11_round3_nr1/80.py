#include <stdio.h>

FILE* fid;
FILE* fout;

int solve() {
	int R, C;

	fscanf(fid, "%d %d\n", &R, &C);

	char buf[80][80];

	for (int y=0; y < R+1; y++) {
		for (int x=0; x < C+1; x++) {
			buf[y][x] = '\0';
		}
	}

	for (int y = 0; y < R; y++) {
		fscanf(fid, "%s\n", buf[y]);
	}

	for (int y=0; y < R; y++) {
		for (int x = 0; x < C; x++) {

			if ('#' == buf[y][x]) {

				if (
					(y < R-1) &&
					(x < C-1) &&
					('#' == buf[y+1][x]) &&
					('#' == buf[y][x+1]) &&
					('#' == buf[y+1][x+1])) {

					buf[y][x] = buf[y+1][x+1] = '/';
					buf[y+1][x] = buf[y][x+1] = '\\';
				} else {
					return 1;
				}

			}

		}
	}

	for (int y=0; y < R; y++) {
		fprintf(fout, "%s\n", buf[y]);
	}


	return 0;
}

int main(int argc, char** argv) {
	fid = fopen("A-large.in", "r");
	fout = fopen("A.out", "w");

	int T = -1;

	fscanf(fid, "%d\n", &T);

	for (int cas=1; cas <= T ;cas++) {
		fprintf(fout, "Case #%d:\n", cas);

		if (solve()) {
			fprintf(fout, "Impossible\n");
		}
	}
}