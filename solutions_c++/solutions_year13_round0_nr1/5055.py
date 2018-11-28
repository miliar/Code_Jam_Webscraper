#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

int check(char board[4][4])
{
	for (int i = 0; i < 4; ++i) {
		int X = 0, O = 0;
		for (int j = 0; j < 4; ++j) {
			char c = board[j][i];
			if (c == 'X' || c == 'T') ++X;
			if (c == 'O' || c == 'T') ++O;
		}
		if (X == 4) return 1;
		if (O == 4) return -1;
	}

	for (int i = 0; i < 4; ++i) {
		int X = 0, O = 0;
		for (int j = 0; j < 4; ++j) {
			char c = board[i][j];
			if (c == 'X' || c == 'T') ++X;
			if (c == 'O' || c == 'T') ++O;
		}
		if (X == 4) return 1;
		if (O == 4) return -1;
	}

	{
		int X = 0, O = 0;
		for (int i = 0; i < 4; ++i) {
			char c = board[i][i];
			if (c == 'X' || c == 'T') ++X;
			if (c == 'O' || c == 'T') ++O;
		}
		if (X == 4) return 1;
		if (O == 4) return -1;
	}

	{
		int X = 0, O = 0;
		for (int i = 0; i < 4; ++i) {
			char c = board[3 - i][i];
			if (c == 'X' || c == 'T') ++X;
			if (c == 'O' || c == 'T') ++O;
		}
		if (X == 4) return 1;
		if (O == 4) return -1;
	}

	return 0;
}

int main() {
  int T; scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
	fprintf(stderr, "Case #%d of %d...\n", Ti, T);
	
	bool empty = false;
	char board[4][4];
	for (int i = 0; i < 4; ++i) {
		char buf[8];
		scanf("%s\n", buf);
		for (int j = 0; j < 4; ++j) {
			board[j][i] = buf[j];
			if (buf[j] == '.') empty = true;
		}
	}

	int res = check(board);
	if (res == 1) printf("Case #%d: X won\n", Ti);
	else if (res == -1) printf("Case #%d: O won\n", Ti);
	else if (empty) printf("Case #%d: Game has not completed\n", Ti);
	else printf("Case #%d: Draw\n", Ti);
  }
  return 0;
}
