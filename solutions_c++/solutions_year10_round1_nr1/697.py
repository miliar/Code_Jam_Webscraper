#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#define mp make_pair
using namespace std;

char board [100][100];
int n, k;

char okR, okB;

int read () {
	n = k = okR = okB = 0;
	memset (board, 0, sizeof (board));
	scanf ("%d%d", &n, &k);
	
	for (int i = 0; i < n; ++i) {
		scanf ("%s", board[i]);
	}
}

int test (int i, int j) {
	int inci [] = { 0, 1, 1, 1 };
	int incj [] = { 1, 1, 0, -1};
	
	int pi = i, pj = j;
	for (int d = 0; d < 4; ++d) {
		int cont = 1;
		pi = i+inci[d]; pj = j+incj[d];
		while (cont < k && i < n && j < n && j >= 0) {
			if (board[pi][pj] == board[i][j]) {
				cont++;
				pi += inci[d];
				pj += incj[d];
			} else break;
		}
		//printf ("%d %d %d: %d\n", i, j, d, cont);
		if (cont == k) return 1;
	}
	return 0;
}

int caso  = 1;
void process () {
	printf ("Case #%d: ", caso++);
	for (int i = 0; i < n; ++i) {
		int pos = n-1;
		for (int j = n-1; j >= 0; --j) {
			if (board[i][j] != '.') {
				//printf ("(%d,%d,%d), %c -> %c\n", i, j, pos, board[i][pos], board[i][j]);
				board[i][pos--] = board[i][j];
			}
		}
		while (pos >= 0) {
			board[i][pos--] = '.';
		}
	}
	
	/*for (int j = 0; j < n; ++j) {
		int pos = n-1;
		for (int i = n-1; i >= 0; --i) {
			if (board[i][j] != '.') {
				board[pos--][j] = board[i][j];
			}
		}
		while (pos >= 0) {
			board[pos--][j] = '.';
		}
	}*/
	okR = okB = 0;
	for (int i = 0; i < n; ++i) {
		//printf ("%s\n", board[i]);
		for (int j = 0; j < n; ++j) {
			if (!okR && board[i][j] == 'R' && test(i,j)) {
				okR = 1;
			} else if (!okB && board[i][j] == 'B' && test(i,j)) {
				okB = 1;
			}
		}
	}
	
	if (okR && okB) {
		printf ("Both\n");
	} else if (okR) {
		printf ("Red\n");
	} else if (okB) {
		printf ("Blue\n");
	} else {
		printf ("Neither\n");
	}
}

int main () {
	int casos;
	scanf ("%d", &casos);
	while (casos--) {
		read();
		process();
	}
	
	//while (read()) process();
	return 0;	
}

