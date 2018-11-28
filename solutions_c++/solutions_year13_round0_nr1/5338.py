#include <cstdio>
#include <cstdlib>
#define MAXN (1 << 3)
using namespace std;

const int N = 4;
char grid[MAXN][MAXN];

void print(int);

inline void solve(int test) {
	int ans = 0;
	
	printf("Case #%d: ", test);
	for (int i=0; i < N; ++i) {
		int x = 0, o = 0;
		for (int j=0; j < N; ++j) {
			if (grid[i][j] == 'O') o++;
			if (grid[i][j] == 'X') x++;
			if (grid[i][j] == 'T') { x++; o++; }
		}
		
		if (x == 4) { ans = 1; print(ans); return; }
		if (o == 4) { ans = 2; print(ans); return; }
	}
	
	for (int i=0; i < N; ++i) {
		int x = 0, o = 0;
		for (int j=0; j < N; ++j) {
			if (grid[j][i] == 'O') o++;
			if (grid[j][i] == 'X') x++;
			if (grid[j][i] == 'T') { x++; o++; }
		}
		
		if (x == 4) { ans = 1; print(ans); return; }
		if (o == 4) { ans = 2; print(ans); return; }
	}		
	
	int x = 0, o = 0;
	for (int j=0; j < N; ++j) {
		if (grid[j][j] == 'O') o++;
		if (grid[j][j] == 'X') x++;
		if (grid[j][j] == 'T') { x++; o++; }
	}
	
	if (x == 4) { ans = 1; print(ans); return; }
	if (o == 4) { ans = 2; print(ans); return; }
	
	x = 0, o = 0;
	for (int j=0; j < N; ++j) {
		if (grid[j][N-j-1] == 'O') o++;
		if (grid[j][N-j-1] == 'X') x++;
		if (grid[j][N-j-1] == 'T') { x++; o++; }
	}
	
	if (x == 4) { ans = 1; print(ans); return;}
	if (o == 4) { ans = 2; print(ans); return; }

	for (int i=0; i < N; ++i)
		for (int j=0; j < N; ++j)
			if (grid[i][j] == '.')
				ans = 3;
	
	print(ans);
}

inline void print(int ans) {
	if (ans == 0) printf("Draw\n");
	if (ans == 1) printf("X won\n");
	if (ans == 2) printf("O won\n");
	if (ans == 3) printf("Game has not completed\n");
}

inline void read() {
	for (int i=0; i < N; ++i)
		scanf("%s", grid[i]);
}

int main() {
	int brt = 0, test = 0;
	scanf("%d", &brt);
	
	while (brt --) {
		read();
		solve(++test);
	}
	return 0;
}