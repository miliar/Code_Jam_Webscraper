#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string.h>
#include <climits>
#include <vector>
#include <queue>
#include <stack>
#include <err.h>
using namespace std;

static const int HWMAX = 100;
int card[HWMAX][HWMAX];
char basins[HWMAX][HWMAX];
int T, H, W;
char sinkch;

char floodfill(int h, int w) {
	int lowalt = card[h][w];
	int dh, dw;

	if (basins[h][w] != ' ') // hit some stream/sink
		return basins[h][w];

	dh = dw = 0;
	if (h > 0 && card[h-1][w] < lowalt) { // north
		dh = -1;
		dw = 0;
		lowalt = card[h+dh][w+dw];
	}
	if (w > 0 && card[h][w-1] < lowalt) { // west
		dh = 0;
		dw = -1;
		lowalt = card[h+dh][w+dw];
	}
	if (w < W - 1 && card[h][w+1] < lowalt) { // east
		dh = 0;
		dw = 1;
		lowalt = card[h+dh][w+dw];
	}
	if (h < H - 1 && card[h+1][w] < lowalt) { // south
		dh = 1;
		dw = 0;
		lowalt = card[h+dh][w+dw];
	}

	if (dh == 0 && dw == 0) { // new sink found
		basins[h][w] = sinkch++;
	}

	//printf("(%d, %d) going (%d, %d)\n", h, w, dh, dw);

	basins[h][w] = floodfill(h+dh, w+dw);
}

int
main()
{
	cin >> T;
	for (int cas = 1; cas <= T; cas++) {
		cin >> H >> W;
		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				cin >> card[h][w];
			}
		}

		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				basins[h][w] = ' ';
			}
		}

		sinkch = 'a';
		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				floodfill(h, w);
			}
		}

		printf("Case #%d:\n", cas);
		for (int h = 0; h < H; h++) {
			for (int w = 0; w < W; w++) {
				printf("%c", basins[h][w]);
				if (w != W - 1)
					printf(" ");
			}
			printf("\n");
		}
	}

	return 0;
}
