#include <stdio.h>
#include <string.h>
#include <assert.h>

int main() {
    int t;
    scanf("%d", &t);

    for (int line = 1; line <= t; line++) {
	int n, k;
	scanf("%d %d", &n, &k);

	char board[50][50];
	for (int i = 0; i < n; i++) {
	    assert(getchar() == '\n');
	    for (int j = 0; j < n; j++) {
		board[i][j] = getchar();
	    }
	}

	for (int i = 0; i < n; i++) {
	    int j = n - 1;
	    for (int k = 0; k < n; k++) {
		assert(j >= 0 && j < n);
		if (board[i][j] == '.') {
		    memmove(&board[i][1], &board[i][0], j);
		    board[i][0] = '.';
		} else {
		    j--;
		}
	    }
	}

	int wins[256] = {};
	for (int i = 0; i < n; i++) {
	    for (int j = 0; j < n; j++) {
		unsigned char player = board[i][j];
		int m;

		for (m = 0; m < k; m++)
		    if (j + m >= n || board[i][j + m] != player) break;
		if (m == k) wins[player] = 1;

		for (m = 0; m < k; m++)
		    if (i + m >= n || board[i + m][j] != player) break;
		if (m == k) wins[player] = 1;

		for (m = 0; m < k; m++)
		    if (i + m >= n || j + m >= n
			|| board[i + m][j + m] != player) break;
		if (m == k) wins[player] = 1;

		for (m = 0; m < k; m++)
		    if (i + m >= n || j - m < 0
			|| board[i + m][j - m] != player) break;
		if (m == k) wins[player] = 1;
	    }
	}

	printf("Case #%d: ", line);
	if (!wins['R'] && !wins['B']) printf("Neither\n");
	if (wins['R'] && wins['B']) printf("Both\n");
	if (wins['R'] && !wins['B']) printf("Red\n");
	if (!wins['R'] && wins['B']) printf("Blue\n");
    }
}
