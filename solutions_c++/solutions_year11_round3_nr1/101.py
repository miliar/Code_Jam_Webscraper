#include <stdio.h>
#include <stdlib.h>

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int R, C;
		char **board;
		scanf("%d%d", &R, &C);
		board = (char**)malloc(R * sizeof(char*));

		for (int i = 0; i< R; i++) {
			board[i] = (char*)malloc((C + 1) * sizeof(char));
			scanf("%s", board[i]);
		}

		bool imposs = false;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (board[i][j] == '#') {
					if (i != R - 1 && j != C - 1 && board[i+1][j] == '#' && board[i][j+1] == '#' && board[i+1][j+1] == '#') {
						board[i][j] = board[i+1][j+1] = '/';
						board[i+1][j] = board[i][j+1] = '\\';
					} else {
						imposs = true;
						goto finish;
					}
				}
			}
		}
finish:
		printf("Case #%d:\n", t);
		if (imposs) {
			printf("Impossible\n");
		} else {
			for (int i = 0; i < R; i++) {
				printf("%s\n", board[i]);
			}
		}
	}
	return 0;
}
