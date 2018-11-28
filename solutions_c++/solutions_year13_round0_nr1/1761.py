#include <cstdio>

char b[6][6];
char sym[] = "OX";

const char *result() {
	for (int s = 0; s < 2; ++s) {
		// rows
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (b[i][j] != sym[s] && b[i][j] != 'T') {
					goto nextrow;
				}
			}
			return sym[s] == 'O' ? "O won" : "X won";
			nextrow: ;
		}
		// cols
		for (int j = 0; j < 4; ++j) {
			for (int i = 0; i < 4; ++i) {
				if (b[i][j] != sym[s] && b[i][j] != 'T') {
					goto nextcol;
				}
			}
			return sym[s] == 'O' ? "O won" : "X won";
			nextcol: ;
		}
		// diag
		for (int i = 0; i < 4; ++i) {
			if (b[i][i] != sym[s] && b[i][i] != 'T') {
				goto nextdiag;
			}
		}
		return sym[s] == 'O' ? "O won" : "X won";
		nextdiag: ;
		for (int i = 0; i < 4; ++i) {
			if (b[i][3-i] != sym[s] && b[i][3-i] != 'T') {
				goto notwon;
			}
		}
		return sym[s] == 'O' ? "O won" : "X won";
		notwon: ;
	}
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			if (b[i][j] == '.') {
				return "Game has not completed";
			}
		}
	}
	return "Draw";
}

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		for (int i = 0; i < 4; ++i) {
			scanf("%s", b[i]);
		}
		printf("Case #%d: %s\n", tt, result());
	}
}
