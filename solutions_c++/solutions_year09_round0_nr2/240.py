#include <cstdio>
#include <iostream>

using namespace std;

int map_label[102][102];
int map_alti[102][102];

int now_label;

int get_maplabel(int row, int col, int H, int W) {
	int& d = map_label[row][col];
	if (d != -1)
		return d;

	int minrow = row;
	int mincol = col;
	int min_alti = map_alti[row][col];

	if (row > 0) {
		if (map_alti[row-1][col] < min_alti) {
			min_alti = map_alti[row-1][col];
			minrow = row - 1;
			mincol = col;
		}
	}
	if (col > 0) {
		if (map_alti[row][col-1] < min_alti) {
			min_alti = map_alti[row][col-1];
			minrow = row;
			mincol = col-1;
		}
	}
	if (col < W - 1) {
		if (map_alti[row][col+1] < min_alti) {
			min_alti = map_alti[row][col+1];
			minrow = row;
			mincol = col+1;
		}
	}
	if (row < H - 1) {
		if (map_alti[row+1][col] < min_alti) {
			min_alti = map_alti[row+1][col];
			minrow = row + 1;
			mincol = col;
		}
	}

	if (minrow == row && mincol == col) {
		d = now_label++;
		return d;
	}
	d = get_maplabel(minrow, mincol, H, W);
	return d;
}

int main() {
	int T, H, W;
	int i,j,k,m,n;
	scanf("%d", &T);

	for (i = 0; i < T; ++i) {
		memset(map_alti, 0, sizeof(map_alti));
		scanf("%d %d", &H, &W);
		for (j = 0; j < H; ++j) {
			for (k = 0; k < W; ++k) {
				scanf("%d", &map_alti[j][k]);
			}
		}

		now_label = 0;
		memset(map_label, -1, sizeof(map_label));
		cout << "Case #" << i + 1 << ":" << endl;

		char mapped[100];
		memset(mapped,0,sizeof(mapped));
		char now_mapping = 'a';

		for (j = 0; j < H; ++j) {
			for (k = 0; k < W; ++k) {
				int label = get_maplabel(j,k,H,W);
				if (mapped[label] == 0) {
					mapped[label] = now_mapping++;
				}
				cout << mapped[label];
				if (k != W-1)
					cout << ' ';
			}
			cout << endl;
		}
	}
}