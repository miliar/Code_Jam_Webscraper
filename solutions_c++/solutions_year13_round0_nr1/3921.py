#include <cstdio>
#include <algorithm>
using namespace std;

char C[4][4];

bool won(char c) {
	// horizontal
	for (int i = 0; i < 4; ++i) {
		bool ok = true;
		for (int j = 0; j < 4; ++j)
			if (C[i][j] != c && C[i][j] != 'T')
				ok = false;
		if (ok) return true;
	}

	// vertical
	for (int j = 0; j < 4; ++j) {
		bool ok = true;
		for (int i = 0; i < 4; ++i)
			if (C[i][j] != c && C[i][j] != 'T')
				ok = false;
		if (ok) return true;
	}

	// NW - SE diagonal
	bool ok = true;
	for (int i = 0; i < 4; ++i)
		if (C[i][i] != c && C[i][i] != 'T')
			ok = false;
	if (ok) return true;

	// NE - SW diagonal
	ok = true;
	for (int i = 0; i < 4; ++i)
		if (C[i][3 - i] != c && C[i][3 - i] != 'T')
			ok = false;
	if (ok) return true;

	return false;
}

void solve() {
	// game won or lost
	if (won('X')) {
		printf("X won\n");
		return;
	}
	else if (won('O')) {
		printf("O won\n");
		return;
	}

	// game not completed
	for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			if (C[i][j] == '.') {
				printf("Game has not completed\n");
				return;
			}
	
	// draw
	printf("Draw\n");
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		// input
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf(" %c", &C[i][j]);

		printf("Case #%d: ", Ti);
		solve();
	}
	return 0;
}
