#include <stdio.h>

int main() {

	int t, i, j, k;
	int dot = 0;
	int countX, countD, countT;
	char moves[4][5];
	FILE *fin, *fout;

	fin = fopen("A-large.in", "r");
	fout = fopen("A-large.out", "w");

	fscanf(fin, "%d", &t);

	for (i = 1; i <= t; i++) {
		for (j = 0; j < 4; j++) {
			fscanf(fin, "%s", &moves[j]);
		}
		dot = 0;
		//horizontal scanning
		for (j = 0; j < 4; j++) {
			countX = 0;
			countT = 0;
			countD = 0;
			for (k = 0; k < 4; k++) {
				if (moves[j][k] == 'X') {
					countX++;
				}
				if (moves[j][k] == '.') {
					countD++;
				}
				if (moves[j][k] == 'T') {
					countT++;
				}
			}
			if ((countX == 3 && countT == 1) || countX == 4) {
				fprintf(fout, "Case #%d: X won\n", i);
				goto out;
			} else if (countX == 0 && countD == 0) {
				fprintf(fout, "Case #%d: O won\n", i);
				goto out;
			} else if (countD != 0) {
				dot = 1;
			}
		}
		//vertical scanning
		for (k = 0; k < 4; k++) {
			countX = 0;
			countT = 0;
			countD = 0;
			for (j = 0; j < 4; j++) {
				if (moves[j][k] == 'X') {
					countX++;
				}
				if (moves[j][k] == '.') {
					countD++;
				}
				if (moves[j][k] == 'T') {
					countT++;
				}
			}
			if ((countX == 3 && countT == 1) || countX == 4) {
				fprintf(fout, "Case #%d: X won\n", i);
				goto out;
			} else if (countX == 0 && countD == 0) {
				fprintf(fout, "Case #%d: O won\n", i);
				goto out;
			} else if (countD != 0) {
				dot = 1;
			}
		}
		// -ve slope diagonal scanning
		countX = 0;
		countT = 0;
		countD = 0;
		for (k = 0, j = 0; k < 4 && j < 4; k++, j++) {
			if (moves[j][k] == 'X') {
				countX++;
			}
			if (moves[j][k] == '.') {
				countD++;
			}
			if (moves[j][k] == 'T') {
				countT++;
			}
		}
		if ((countX == 3 && countT == 1) || countX == 4) {
			fprintf(fout, "Case #%d: X won\n", i);
			goto out;
		} else if (countX == 0 && countD == 0) {
			fprintf(fout, "Case #%d: O won\n", i);
			goto out;
		} else if (countD != 0) {
			dot = 1;
		}

		// +ve slope diagonal scanning
		countX = 0;
		countT = 0;
		countD = 0;
		for (k = 0, j = 3; k < 4 && j >= 0; k++, j--) {
			if (moves[j][k] == 'X') {
				countX++;
			}
			if (moves[j][k] == '.') {
				countD++;
			}
			if (moves[j][k] == 'T') {
				countT++;
			}
		}
		if ((countX == 3 && countT == 1) || countX == 4) {
			fprintf(fout, "Case #%d: X won\n", i);
			goto out;
		} else if (countX == 0 && countD == 0) {
			fprintf(fout, "Case #%d: O won\n", i);
			goto out;
		} else if (countD != 0) {
			dot = 1;
		}

		if (dot == 1) {
			fprintf(fout, "Case #%d: Game has not completed\n", i);
		} else {
			fprintf(fout, "Case #%d: Draw\n", i);
		}
		out: ;
	}
	return 0;
}
