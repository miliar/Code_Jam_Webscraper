#include <cstdio>
#include <cstring>

const int MAX = 100000;
int alt[100][100];
int map[100][100][4]; // from N, W, E, S
int map2[100][100][4]; // toward N, W, E, S
char label[100][100];

void name(int j, int k)
{
	if (map[j][k][0] || map2[j][k][0]) {
		if (!label[j-1][k]) {
			label[j-1][k] = label[j][k];
			name(j-1, k);
		}
	}
	if (map[j][k][1] || map2[j][k][1]) {
		if (!label[j][k-1]) {
			label[j][k-1] = label[j][k];
			name(j, k-1);
		}
	}
	if (map[j][k][2] || map2[j][k][2]) {
		if (!label[j][k+1]) {
			label[j][k+1] = label[j][k];
			name(j, k+1);
		}
	}
	if (map[j][k][3] || map2[j][k][3]) {
		if (!label[j+1][k]) {
			label[j+1][k] = label[j][k];
			name(j+1, k);
		}
	}
}

int main()
{
	int N;
	scanf("%d", &N);
	for (int i=1; i<=N; ++i) {
		int H, W;
		memset(map, 0, sizeof(map));
		memset(map2, 0, sizeof(map));
		memset(label, 0, sizeof(label));
		scanf("%d %d", &H, &W);
		for (int j=0; j<H; ++j)
			for (int k=0; k<W; ++k)
				scanf("%d", &(alt[j][k]));
		for (int j=0; j<H; ++j) {
			for (int k=0; k<W; ++k) {
				int north = (j > 0)?(alt[j-1][k]):MAX;
				int west = (k > 0)?(alt[j][k-1]):MAX;
				int east = (k < W-1)?(alt[j][k+1]):MAX;
				int south = (j < H-1)?(alt[j+1][k]):MAX;
				int current = alt[j][k];
				int toward = -1;
				if (current > north) {
					current = north;
					toward = 0;
				}
				if (current > west) {
					current = west;
					toward = 1;
				}
				if (current > east) {
					current = east;
					toward = 2;
				}
				if (current > south) {
					current = south;
					toward = 3;
				}
				switch (toward) {
				case -1:
					break;
				case 0:
					map[j-1][k][3] = 1;
					map2[j][k][0] = 1;
					break;
				case 1:
					map[j][k-1][2] = 1;
					map2[j][k][1] = 1;
					break;
				case 2:
					map[j][k+1][1] = 1;
					map2[j][k][2] = 1;
					break;
				case 3:
					map[j+1][k][0] = 1;
					map2[j][k][3] = 1;
					break;
				}
			}
		}
		char sink = 'a';
		for (int j=0; j<H; ++j) {
			for (int k=0; k<W; ++k) {
				if (!label[j][k]) {
					label[j][k] = sink;
					name(j, k);
					++sink;
				}
			}
		}
		printf("Case #%d:\n", i);
		for (int j=0; j<H; ++j) {
			for (int k=0; k<W; ++k) {
				printf("%c ", label[j][k]);
			}
			putchar('\n');
		}
	}
	return 0;
}

