#include <cstdio>
#define rep(i, a, b) for(int i=int(a); i<int(b); i++)

char grid[4][4];

bool checkwin(char c) {
	rep(i, 0, 4) {
		bool win = true;
		rep(j, 0, 4) {
			if(!(grid[i][j] == c || grid[i][j] == 'T'))
				win = false;
		}

		if(win)
			return true;
	}

	rep(j, 0, 4) {
		bool win = true;
		rep(i, 0, 4) {
			if(!(grid[i][j] == c || grid[i][j] == 'T'))
				win = false;
		}

		if(win)
			return true;
	}

	bool win = true;
	for(int i=0, j=0; i<4 && j<4; i++, j++) {
		if(!(grid[i][j] == c || grid[i][j] == 'T'))
			win = false;
	}
	if(win)
		return true;

	win = true;
	for(int i=0, j=3; i<4 && j>=0; i++, j--) {
		if(!(grid[i][j] == c || grid[i][j] == 'T'))
			win = false;
	}
	if(win)
		return true;

	return false;
}

void solve() {

	bool emptyboxes = false;

	rep(i, 0, 4) {
		char str[5];
		scanf("%s", str);

		rep(j, 0, 4) {
			grid[i][j] = str[j];
			if(str[j] == '.')
				emptyboxes = true;
		}
	}

	bool xwon = checkwin('X');

	if(xwon) {
		printf("X won\n");
		return;
	}

	bool owon = checkwin('O');

	if(owon) {
		printf("O won\n");
		return;
	}

	if(emptyboxes) {
		printf("Game has not completed\n");
		return;
	}

	printf("Draw\n");

	return;

}

int main() {
	int T;
	scanf("%d", &T);
	
	rep(i, 0, T) {
		printf("Case #%d: ", i+1);
		solve();
	}
}
