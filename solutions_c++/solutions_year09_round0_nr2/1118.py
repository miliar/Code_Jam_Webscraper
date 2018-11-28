#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

#define MAXN 128

const int dr[] = { -1, 0, 0, 1 };
const int dc[] = { 0, -1, 1, 0 };

int T;
int H, W;
int alt[MAXN][MAXN];
int neighbour[MAXN][MAXN];
int wuz[MAXN][MAXN];
int mapper[32];
int kaunter;

inline bool check_bounds(int r, int c) {
	return r >= 0 && c >= 0 && r < H && c < W;
}

int visit(int r, int c) {
	if (wuz[r][c] != -1)
		return wuz[r][c];

	int d = neighbour[r][c];
	if (d == -1)
		return wuz[r][c] = kaunter++;
	else {
		int nr = r + dr[d], nc = c + dc[d];
		return wuz[r][c] = visit(nr, nc);
	}
}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d%d", &H, &W);

		memset(neighbour, -1, sizeof neighbour);
		memset(wuz, -1, sizeof wuz);

		for (int r = 0; r < H; ++r)
			for (int c = 0; c < W; ++c)
				scanf("%d", &alt[r][c]);

		for (int r = 0; r < H; ++r)
			for (int c = 0; c < W; ++c) {
				int best = alt[r][c];

				for (int d = 0; d < 4; ++d) {
					int nr = r + dr[d], nc = c + dc[d];

					if (! check_bounds(nr, nc))
						continue;

					if (alt[nr][nc] < best) {
						best = alt[nr][nc];
						neighbour[r][c] = d;
					}
				}
			}

		kaunter = 0;
		for (int r = 0; r < H; ++r)
			for (int c = 0; c < W; ++c)
				if (wuz[r][c] == -1)
					wuz[r][c] = visit(r, c);

		printf("Case #%d:\n", tc);

		memset(mapper, -1, sizeof mapper);
		char next_char = 'a';
		for (int r = 0; r < H; ++r) {
			for (int c = 0; c < W; ++c) {
				int w = wuz[r][c];
				if (mapper[w] == -1) mapper[w] = next_char++;

				printf("%c%s", (char)mapper[w], c == W-1 ? "" : " ");
			}
			printf("\n");
		}
	}

	return EXIT_SUCCESS;
}
