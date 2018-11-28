#include <cstdio>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
	int c;
	scanf("%d", &c);
	bool grid[2][100][100];
	for(int i = 0; i < c; i++) {
		int r;
		scanf("%d", &r);
		for(int j = 0; j < 2; j++) {
			for(int k = 0; k < 100; k++) {
				fill(grid[j][k], grid[j][k]+100, false);
			}
		}
		for(int j = 0; j < r; j++) {
			int x1, y1, x2, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for(int k = x1-1; k < x2; k++) {
				for(int l = y1-1; l < y2; l++) {
					grid[0][k][l] = true;
				}
			}
		}
		bool empty = r==0;
		int count = 0;
		while (!empty) {
			count ++;
			empty = true;
			for(int j = 0; j < 100; j++) {
				for(int k = 0; k < 100; k++) {
					if(j==0 && k==0) grid[1][j][k] = false;
					else if (j==0) grid[1][j][k] = grid[0][j][k] && grid[0][j][k-1];
					else if (k==0) grid[1][j][k] = grid[0][j][k] && grid[0][j-1][k];
					else {
						grid[1][j][k] = (grid[0][j][k] && (grid[0][j-1][k] || grid[0][j][k-1]))
                                                            ||  (grid[0][j][k-1] && grid[0][j-1][k]);
					}
					if(grid[1][j][k]) empty = false;
				}
			}
			for(int j = 0; j < 100; j++) {
				for(int k = 0; k < 100; k++) {
					grid[0][j][k] = grid[1][j][k];
				}
			}
		}
		printf("Case #%d: %d\n", i+1, count);
	}
	return 0;
}
