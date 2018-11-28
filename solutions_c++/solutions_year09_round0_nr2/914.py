#include <stdio.h>
#include <string.h>
#include <assert.h>

#define MAXSIZE		100
#define MAXLETTERS	26
#define INF		0x10101010

int map[MAXSIZE + 2][MAXSIZE + 2];
int H, W;

int flowdir[MAXSIZE + 2][MAXSIZE + 2];
int symbol[MAXSIZE + 2][MAXSIZE + 2];
int queue[MAXSIZE * MAXSIZE][2];

//                    N   W   E   S
const int dirx[] = {  0, -1,  1,  0 };
const int diry[] = { -1,  0,  0,  1 };
const int negd[] = {  3,  2,  1,  0 };

#define OFF(map, r, c, k)	((map)[(r)+diry[k]][(c)+dirx[k]])

void solve()
{
	int i, j, k, ql, qr, min, nextsymbol;
	char symbolmap[MAXLETTERS], nextletter, *ch;

	assert(scanf("%d %d", &H, &W) == 2);

	memset(map, 0x10, sizeof(map));
	for (i = 1; i <= H; i++)
		for (j = 1; j <= W; j++)
			assert(scanf("%d", &map[i][j]) == 1);

	// find sinks
	memset(flowdir, 0xff, sizeof(flowdir));
	memset(symbol, 0xff, sizeof(symbol));
	nextsymbol = 0;
	ql = qr = 0;
	for (i = 1; i <= H; i++) {
		for (j = 1; j <= W; j++) {
			min = OFF(map, i, j, 0);
			if (min > OFF(map, i, j, 1))
				min = OFF(map, i, j, 1);
			if (min > OFF(map, i, j, 2))
				min = OFF(map, i, j, 2);
			if (min > OFF(map, i, j, 3))
				min = OFF(map, i, j, 3);

			if (min >= map[i][j]) {
				// cell is a sink
				k = -1;
				symbol[i][j] = nextsymbol++;
				queue[qr][0] = i;
				queue[qr][1] = j;
				qr++;
			}
			else if (min == OFF(map, i, j, 0))
				k = 0;
			else if (min == OFF(map, i, j, 1))
				k = 1;
			else if (min == OFF(map, i, j, 2))
				k = 2;
			else // if (min == OFF(map, i, j, 3))
				k = 3;

			flowdir[i][j] = k;
		}
	}

	// now let's "reverse" gravity and expand sinks to basins
	while (ql < qr) {
		i = queue[ql][0];
		j = queue[ql][1];
		ql++;
		for (k = 0; k < 4; k++) {
			if (OFF(flowdir, i, j, k) == negd[k]) {
				OFF(symbol, i, j, k) = symbol[i][j];
				queue[qr][0] = i + diry[k];
				queue[qr][1] = j + dirx[k];
				qr++;
			}
		}
	}

	// remap symbols to letters alphabetically and produce output
	memset(symbolmap, 0x00, sizeof(symbolmap));
	nextletter = 'a';
	for (i = 1; i <= H; i++) {
		for (j = 1; j <= W; j++) {
			ch = symbolmap + symbol[i][j];
			if (!*ch)
				*ch = nextletter++;
			if (j > 1)
				fputc(' ', stdout);
			fputc(*ch, stdout);
		}
		fputc('\n', stdout);
	}
}

int main(int argc, char **argv)
{
	int T, X;

	if (argc > 1 && !freopen(argv[1], "rt", stdin)) {
		perror(argv[1]);
		return 1;
	}
	if (argc > 2 && !freopen(argv[2], "wt", stdout)) {
		perror(argv[2]);
		return 1;
	}

	assert(scanf("%d", &T) == 1);
	fprintf(stderr, "T=%d\n", T);

	for (X = 1; X <= T; X++) {
		printf("Case #%d:\n", X);
		solve();
	}
}
