#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(void)
{
	unsigned int T, H, W;
	int i, j, k, l;

	cin >> T;
	for (k = 0; k < T; k++) {
		unsigned char nl = 'a';
		cin >> H >> W;
		unsigned int amap[H][W];
		unsigned char dbmap[H][W];
		for (i = 0; i < H; i++) {
			for (j = 0; j < W; j++) {
				cin >> amap[i][j];
				dbmap[i][j] = 0;
			}
		}

		for (i = 0; i < H; i++) {
			for (j = 0; j < W; j++) {
				if (dbmap[i][j] != 0) continue;
				bool found = false;
				unsigned int dir[5]; //c, n, w, e, s
				unsigned int ci = i, cj = j;
				unsigned char pl;
				while (!found) {
					dbmap[ci][cj] = '*';
					dir[0] = amap[ci][cj];
					dir[1] = ci > 0 ? amap[ci-1][cj] : 20000;
					dir[2] = cj > 0 ? amap[ci][cj-1] : 20000;
					dir[3] = cj < (W - 1) ? amap[ci][cj+1] : 20000;
					dir[4] = ci < (H - 1) ? amap[ci+1][cj] : 20000;
					unsigned int smallest = 0;
					for (l = 1; l < 5; l++)
						if (dir[l] < dir[smallest])
							smallest = l;
					switch (smallest) {
					case 0:
						found = 1;
						pl = nl;
						nl++;
						break;
					case 1:
						ci--;
						if (dbmap[ci][cj] != 0) {
							found = 1;
							pl = dbmap[ci][cj];
						}
						break;
					case 2:
						cj--;
						if (dbmap[ci][cj] != 0) {
							found = 1;
							pl = dbmap[ci][cj];
						}
						break;
					case 3:
						cj++;
						if (dbmap[ci][cj] != 0) {
							found = 1;
							pl = dbmap[ci][cj];
						}
						break;
					case 4:
						ci++;
						if (dbmap[ci][cj] != 0) {
							found = 1;
							pl = dbmap[ci][cj];
						}
						break;
					}
				}
				int x, y;
				for (y = 0; y < H; y++) {
					for (x = 0; x < W; x++) {
						if (dbmap[y][x] == '*') dbmap[y][x] = pl;
					}
				}
			}
		}

		cout << "Case #" << k+1 << ":" << endl;
		for (i = 0; i < H; i++) {
			for (j = 0; j < W; j++)
				cout << dbmap[i][j] << " ";
			cout << endl;
		}
	}

	return 0;
}

