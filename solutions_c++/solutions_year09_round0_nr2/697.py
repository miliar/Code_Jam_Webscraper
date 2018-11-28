#include <iostream>
#include <algorithm>
#include <fstream>
#include <queue>

using namespace std;

int b[200][200], t, h, w, xs[4] = {-1, 0, 0, 1}, ys[4] = {0, -1, 1, 0};;
char bs[200][200], st;

bool low(int X, int Y, int x, int y) {
	int los = 100000, lo = -1;
	for (int k=0;k<4;k++) {
		if (x+xs[k] < 0 || x+xs[k] >= h || y+ys[k] < 0 || y+ys[k] >= w || b[x+xs[k]][y+ys[k]] >= b[x][y])
			continue;
		if (b[x+xs[k]][y+ys[k]] < los) {
			los = b[x+xs[k]][y+ys[k]];
			lo = k;
		}
	}
	if (x+xs[lo] == X && y+ys[lo] == Y)
		return true;
	return false;
}

int main() {
	FILE *fin, *fout;
    fin = fopen("B-large.in", "r");
    fout = fopen("watersheds.out", "w");
	fscanf(fin, "%d", &t);
	for (int r=0;r<t;r++) {
		st = 'a';
		fscanf(fin, "%d %d", &h, &w);
		for (int i=0;i<h;i++) {
			for (int j=0;j<w;j++) {
				fscanf(fin, "%d", &b[i][j]);
			}
		}
		for (int i=0;i<h;i++) {
			for (int j=0;j<w;j++) {
				int s = 0;
				for (int k=0;k<4;k++) {
					if (i+xs[k] < 0 || i+xs[k] >= h || j+ys[k] < 0 || j+ys[k] >= w || b[i+xs[k]][j+ys[k]] >= b[i][j])
						continue;
					s++;
				}
				if (!s) {
					queue< int > x, y;
					bool V[200][200] = {false};
					x.push(i), y.push(j);
					while (!x.empty()) {
						int tx = x.front(), ty = y.front();
						x.pop(), y.pop();
						if (V[tx][ty])
							continue;
						V[tx][ty] = true;
						bs[tx][ty] = st;
						for (int k=0;k<4;k++) {
							if (tx+xs[k] < 0 || tx+xs[k] >= h || ty+ys[k] < 0 || ty+ys[k] >= w || b[tx+xs[k]][ty+ys[k]] <= b[tx][ty])
								continue;
							if (low(tx, ty, tx+xs[k], ty+ys[k])) {
								x.push(tx+xs[k]);
								y.push(ty+ys[k]);
							}
						}
					}
					st++;
				}
			}
		}
		char now = 'a', alpha[30] = {0};
		for (int i=0;i<h;i++) {
			for (int j=0;j<w;j++) {
				if (!alpha[bs[i][j]-'a']) {
					alpha[bs[i][j]-'a'] = now;
					now++;
				}
			}
		}
		for (int i=0;i<h;i++) {
			for (int j=0;j<w;j++) {
				bs[i][j] = alpha[bs[i][j]-'a'];
			}
		}
		fprintf(fout, "Case #%d:\n", r+1);
		for (int i=0;i<h;i++) {
			for (int j=0;j<w;j++) {
				fprintf(fout, "%c", bs[i][j]);
				if (j == w-1)
					fprintf(fout, "\n");
				else
					fprintf(fout, " ");
			}
		}
	}
	return 0;
}
