#include <iostream>
#include <cstdio>

using namespace std;

bool grid[2][300][300];

int get(int k, int x, int y) {
	if(grid[k][x][y] && !grid[k][x-1][y] && !grid[k][x][y-1]) return false;
	if(!grid[k][x][y] && grid[k][x-1][y] && grid[k][x][y-1]) return true;
	return grid[k][x][y];
}

int solve() {
	int R;
	scanf("%d", &R);
	memset(grid, false, sizeof(grid));

	int total = 0;


	for(int i = 0; i < R; i++) {
		int X1, Y1, X2, Y2;
		scanf("%d %d %d %d", &X1, &Y1, &X2, &Y2);
		for(int j = X1; j <= X2; j++) 
			for(int k = Y1; k <= Y2; k++) {
				total++;
				grid[0][j][k] = true;				
			}
	}

	int result = 0;

	while(total) {
		total = 0;
		result++;
		for(int i = 1; i <= 300; i++)
			for(int j = 1; j <= 300; j++) {
				grid[result%2][i][j] = get((result+1)%2, i, j);	
				total += grid[result%2][i][j];				
			}
	}

	return result;
}
int main() {
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) printf("Case #%d: %d\n", i, solve());
}