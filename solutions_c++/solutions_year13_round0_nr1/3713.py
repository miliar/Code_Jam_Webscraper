#include <cstdio>

enum {
	FIELD_SIZE = 4
};

bool isWon(char **field, char X) {
	// Tell if X player won (playing on FIELD_SIZE by FIELD_SIZE field)
	for (int i = 0; i < FIELD_SIZE; i++) {
		bool win_row = true;
		for (int j = 0; j < FIELD_SIZE; j++) {
			if (field[i][j] != X && field[i][j] != 'T') {
				win_row = false;
				break;
			}
		}
		if (win_row) return true;
	}
	for (int i = 0; i < FIELD_SIZE; i++) {
		bool win_column = true;
		for (int j = 0; j < FIELD_SIZE; j++) {
			if (field[j][i] != X && field[j][i] != 'T') {
				win_column = false;
				break;
			}
		}
		if (win_column) return true;
	}

	bool win_main_diag = true;
	for (int i = 0; i < FIELD_SIZE; i++) {
		if (field[i][i] != X && field[i][i] != 'T') {
			win_main_diag = false;
			break;
		}
	}
	if (win_main_diag) return true;

	bool win_add_diag = true;
	for (int i = 0; i < FIELD_SIZE; i++) {
		if (field[i][FIELD_SIZE - i - 1] != X && field[i][FIELD_SIZE - i - 1] != 'T') {
			win_add_diag = false;
			break;
		}
	}
	if (win_add_diag) return true;

	return false;
}
bool isFinished(char **field) {
	// Tell if game finished (where are no '.' symbols left)
	for (int i = 0; i < FIELD_SIZE; i++) {
		for (int j = 0; j < FIELD_SIZE; j++) {
			if (field[i][j] == '.') {
				return false;
			}
		}
	}
	return true;
}

int main() {
	int T;
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("output.txt", "w");
	char **field = new char*[FIELD_SIZE];
	for (int i = 0; i < FIELD_SIZE; i++) {
		field[i] = new char[FIELD_SIZE];
	}
	fscanf(fin, "%d\n", &T);
	for (int test_case = 0; test_case < T; test_case++) {
		for (int i = 0; i < FIELD_SIZE; i++) {
			for (int j = 0; j < FIELD_SIZE; j++) {
				fscanf(fin, "%c", &field[i][j]);
			}
			fscanf(fin, "\n");
		}

		fprintf(fout, "Case #%d: ", test_case + 1);
		if (isWon(field, 'X')) {
			fprintf(fout, "X won\n");
		} else if(isWon(field, 'O')) {
			fprintf(fout, "O won\n");
		} else if (!isFinished(field)) {
			fprintf(fout, "Game has not completed\n");
		} else {
			fprintf(fout, "Draw\n");
		}
	}

	return 0;
}