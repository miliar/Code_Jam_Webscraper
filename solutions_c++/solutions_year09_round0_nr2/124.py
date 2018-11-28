#define _WATERSHEDS
#ifdef _WATERSHEDS
// Google Code Jam 2009 - Qualification Round (Watersheds)

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

using namespace std;

int heightmap[111][111];
char output[111][111];
char comp;

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int szX, szY;

char dfs(int x, int y) {
	int lowest = 20000;
	int nx = -1, ny = -1;
	for (int k = 0; k < 4; k++) {
		int mx = dx[k] + x;
		int my = dy[k] + y;
		if (mx < 0 || my < 0 || mx >= szX || my >= szY || heightmap[x][y] <= heightmap[mx][my]) continue;
		if (heightmap[mx][my] < lowest) {
			lowest = heightmap[mx][my];
			nx = mx;
			ny = my;
		}
	}
	// sink
	if (nx < 0) {
		if (output[x][y] != 0) return output[x][y];
		return output[x][y] = comp++;
	}
	// backtrack the solution
	output[x][y] = dfs(nx,ny);
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		memset(heightmap,0,sizeof(heightmap));
		memset(output,0,sizeof(output));
		int X, Y;
		cin >> X >> Y;
		for (int j = 0; j < X; j++) {
			for (int k = 0; k < Y; k++) {
				int val; cin >> val;
				heightmap[j][k] = val;
			}
		}
		// begin flood fill
		comp = 'a';
		szX = X;
		szY = Y;
		for (int j = 0; j < X; j++) {
			for (int k = 0; k < Y; k++) {
				if (output[j][k]) continue;
				dfs(j,k);
			}
		}
		cout << "Case #" << (i+1) << ":\n";
		for (int j = 0; j < X; j++) {
			for (int k = 0; k < Y; k++) {
				if (k != 0) cout << " ";
				cout << output[j][k];
			}
			cout << "\n";
		}
	}
	return 0;
}
#endif