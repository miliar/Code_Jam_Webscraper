#include <iostream>
#include <string>
#include <vector>

using namespace std;

int map[100][100];
int bas[100][100];
int flowr[100][100], flowc[100][100];
int h, w;

int dr[5] = {0, -1, 0, 0, 1};
int dc[5] = {0, 0, -1, 1, 0};


bool ok(int a, int b) {
	return (a >= 0 && a < h && b >= 0 && b < w);
}

void flood(int r, int c, int ch) {
	if (!ok(r, c)) return;
	if (bas[r][c] >= 0) return;
	bas[r][c] = ch;
	int nr = flowr[r][c];
	int nc = flowc[r][c];
	flood(nr, nc, ch);
	int i;
	for (i=1; i<5; i++) {
		nr = r+dr[i];
		nc = c+dc[i];
		if (ok(nr, nc)) {
			if (flowr[nr][nc] == r && flowc[nr][nc] == c) {
				flood(nr, nc, ch);
			}
		}
	}
}


int main () {
	int T;
	int i, j, k;
	cin >> T;
	int cse = 0;
	while (T--) {
		cin >> h >> w;
		for (i=0; i<h; i++) {
			for (j=0; j<w; j++) {
				cin >> map[i][j];
				bas[i][j] = -1;
			}
		}
		for (i=0; i<h; i++) {
			for (j=0; j<w; j++) {
				int b = 1000000000, bx, by;
				for (k=0; k<5; k++) {
					int nr = i+dr[k];
					int nc = j+dc[k];
					if (ok(nr, nc)) {
						if (map[nr][nc] < b) {
							bx = nr; by = nc;
							b = map[nr][nc];
						}
					}
				}
				flowr[i][j] = bx;
				flowc[i][j] = by;
			}
		}
		int cnt = 0;
		for (i=0; i<h; i++) {
			for (j=0; j<w; j++) {
				if (bas[i][j] == -1) {
					flood(i, j, cnt++);
				}
			}
		}
		cout << "Case #" << ++cse << ":" << endl;
		for (i=0; i<h; i++) {
			for (j=0; j<w; j++) {
				cout << char('a'+bas[i][j]);
				if (j != w-1) cout << " ";
			}
			cout << endl;
		}
	}
	return 0;
}
