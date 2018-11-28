#include <stdio.h>
#include <string.h>

#define WINNER_X 0
#define WINNER_O 1
#define WINNER_NO 2

int main() {
	FILE *fin, *fout;

	fin = fopen ("input.txt", "r");
	fout = fopen ("output.txt", "w");

	int T;
	fscanf (fin, "%d", &T);

	for (int t = 1; t <= T; ++t) {
		char data[4][5];
		
		bool isThereAnEmptyCell = false;

		for (int i = 0; i < 4; ++i) {
			fscanf (fin, "%s", data[i]);

			if (!isThereAnEmptyCell) {
				for (int j = 0; j < 4; ++j) {
					if (data[i][j] == '.') {
						isThereAnEmptyCell = true;
						break;
					}
				}
			}
		}

		int winner = WINNER_NO;

		// horizontal
		for (int i = 0; i < 4; ++i) {
			int xCount = 0;
			int oCount = 0;
			bool tAppeared = false;

			for (int j = 0; j < 4; ++j) {
				if (data[i][j] == 'X') {
					++ xCount;
				} else if (data[i][j] == 'O') {
					++ oCount;
				} else if (data[i][j] == 'T') {
					tAppeared = true;
				}
			}

			if (xCount == 4 || (xCount == 3 && tAppeared)) {
				winner = WINNER_X;
				break;
			}
			if (oCount == 4 || (oCount == 3 && tAppeared)) {
				winner = WINNER_O;
				break;
			}
		}

		if (WINNER_NO == winner) {
			// vertical
			for (int j = 0; j < 4; ++j) {
				int xCount = 0;
				int oCount = 0;
				bool tAppeared = false;

				for (int i = 0; i < 4; ++i) {
					if (data[i][j] == 'X') {
						++ xCount;
					} else if (data[i][j] == 'O') {
						++ oCount;
					} else if (data[i][j] == 'T') {
						tAppeared = true;
					}
				}

				if (xCount == 4 || (xCount == 3 && tAppeared)) {
					winner = WINNER_X;
					break;
				}
				if (oCount == 4 || (oCount == 3 && tAppeared)) {
					winner = WINNER_O;
					break;
				}
			}
		}

		if (WINNER_NO == winner) {
			// diagonal 1

			int xCount = 0;
			int oCount = 0;
			bool tAppeared = false;

			for (int i = 0; i < 4; ++i) {
				if (data[i][i] == 'X') {
					++ xCount;
				} else if (data[i][i] == 'O') {
					++ oCount;
				} else if (data[i][i] == 'T') {
					tAppeared = true;
				}
			}

			if (xCount == 4 || (xCount == 3 && tAppeared)) {
				winner = WINNER_X;
			} else if (oCount == 4 || (oCount == 3 && tAppeared)) {
				winner = WINNER_O;
			}
		}

		if (WINNER_NO == winner) {
			// diagonal 2

			int xCount = 0;
			int oCount = 0;
			bool tAppeared = false;

			for (int i = 3, j = 0; i >= 0 && j < 4; --i, ++j) {
				if (data[i][j] == 'X') {
					++ xCount;
				} else if (data[i][j] == 'O') {
					++ oCount;
				} else if (data[i][j] == 'T') {
					tAppeared = true;
				}
			}

			if (xCount == 4 || (xCount == 3 && tAppeared)) {
				winner = WINNER_X;
			} else if (oCount == 4 || (oCount == 3 && tAppeared)) {
				winner = WINNER_O;
			}
		}

		if (WINNER_NO == winner) {
			if (isThereAnEmptyCell) {
				fprintf (fout, "Case #%d: Game has not completed\n", t);
			} else {
				fprintf (fout, "Case #%d: Draw\n", t);
			}
		} else if (WINNER_X == winner) {
			fprintf (fout, "Case #%d: X won\n", t);
		} else {
			fprintf (fout, "Case #%d: O won\n", t);
		}
	}

	fclose (fin);
	fclose (fout);

	return 0;
}
