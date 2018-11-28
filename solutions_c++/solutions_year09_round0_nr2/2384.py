#include <cstdio>
#include <iostream>

using namespace std;

int heights[101][101];
int parentx[101][101];
int parenty[101][101];
char group[101][101];

char getgr(int j, int k) {
	if ((parentx[j][k] != j) || (parenty[j][k] != k)) {
		// cerr << "recur " << parentx[j][k] << " " << parenty[j][k] << endl;
		return getgr(parentx[j][k], parenty[j][k]);
	}
	// cerr << "ret" << endl;
	return group[j][k];
}

void setgr(int j, int k, char gr) {
	group[j][k] = gr;
	if ((parentx[j][k] != j) || (parenty[j][k] != k)) {
		setgr(parentx[j][k], parenty[j][k], gr);
	}
}

int main(int argc, char **argv) {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		printf("Case #%d:\n", i+1);
		int H, W;
		scanf("%d%d", &H, &W);
		for (int j = 0; j < H; ++j) {
			for (int k = 0; k < W; ++k) {
				scanf("%d", &heights[j][k]);
				parentx[j][k] = j;
				parenty[j][k] = k;
				group[j][k] = 0;
			}
		}
		for (int j = 0; j < H; ++j) {
			for (int k = 0; k < W; ++k) {
				int min = heights[j][k];
				if (j > 0) {
					if (heights[j-1][k] < min) {
						min = heights[j-1][k];
						parentx[j][k] = j-1;
						parenty[j][k] = k;
					}
				}
				if (k > 0) {
					if (heights[j][k-1] < min) {
						min = heights[j][k-1];
						parentx[j][k] = j;
						parenty[j][k] = k-1;
					}
				}
				if (k < W-1) {
					if (heights[j][k+1] < min) {
						min = heights[j][k+1];
						parentx[j][k] = j;
						parenty[j][k] = k+1;
					}
				}
				if (j < H-1) {
					if (heights[j+1][k] < min) {
						min = heights[j][k+1];
						parentx[j][k] = j+1;
						parenty[j][k] = k;
					}
				}
			}
		}
		char gr = 'a';
		for (int j = 0; j < H; ++j) {
			for (int k = 0; k < W; ++k) {
				const int g = getgr(j, k);
				if (g == 0) {
					setgr(j, k, gr);
					++gr;
				} else {
					group[j][k] = g;
				}
				if (k) {
					putc(' ', stdout);
				}
				printf("%c", group[j][k]);
			}
			puts("");
		}
	}
}
