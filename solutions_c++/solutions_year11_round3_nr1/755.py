#include <cstdio>
#include <cmath>
const int WHITE = 0;
const int BLUE = 1;
const int RED[] = {0, 2, 3, 4, 5};
const int MAX_R = 55;
const char OUTPUTCHAR[] = {'.', '#', '/', '\\', '\\', '/'};
using namespace std;
int N;

int grid[MAX_R][MAX_R];
void solve(int caseNum) {
	printf("Case #%d: \n", caseNum);
	for(int i = 1; i < MAX_R; i++) {
		for(int j = 1; j < MAX_R; j++) {
			grid[i][j] = 0;
		}
	}
	int R, C;
	scanf("%d %d\n", &R, &C);
	for(int i = 1; i <= R; i++) {
		for(int j = 1; j <= C; j++) {
			char x;
			scanf("%c ", &x);
			if(x == '.') grid[i][j] = WHITE;
			else if(x == '#') grid[i][j] = BLUE;
			else {
				printf("Input Failed.\n");
				return;
			}
		}
	}
	for(int i = 1; i <= R; i++) {
		for(int j = 1; j <= C; j++) {
			if(grid[i][j] == BLUE) {
				if(grid[i + 1][j] == BLUE && grid[i + 1][j + 1] == BLUE && grid[i][j + 1] == BLUE) {
					grid[i][j] = RED[1];
					grid[i][j + 1] = RED[2];
					grid[i + 1][j] = RED[3];
					grid[i + 1][j + 1] = RED[4];

				}
				else {
					printf("Impossible\n");
					return;
				}
			}
		}
	}
	for(int i = 1; i <= R; i++) {
		for(int j = 1; j <= C; j++) {
			printf("%c", OUTPUTCHAR[grid[i][j]]);
		}
		printf("\n");
	}

	return;
}

int main() {

	freopen("small.txt", "r", stdin);
	freopen("smallout.txt", "w", stdout);
	scanf("%d", &N);
	for(int i = 1; i <= N; i++) solve(i);

	freopen("large.txt", "r", stdin);
	freopen("largeout.txt", "w", stdout);
	scanf("%d", &N);
	for(int i = 1; i <= N; i++) solve(i);
	return 0;
}
