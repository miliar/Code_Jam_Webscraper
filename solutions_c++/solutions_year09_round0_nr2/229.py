#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 109;
const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

bool vst[MAXN * MAXN];
int H, W;
char mat[MAXN][MAXN];
int att[MAXN][MAXN];
int cas;
vector <int> g[MAXN * MAXN];


void dfs(int u, char ch) {
	int i;
	vst[u] = true;
	mat[u / W][u % W] = ch;
	for (i = 0; i < g[u].size(); ++i)
		if (!vst[g[u][i]]) dfs(g[u][i], ch);
}



int main() {
	freopen("F:\\B-large.in", "r", stdin);
	freopen("F:\\B-large.out", "w", stdout);
	int T;
	int i, j, k, u, v;

	scanf("%d", &T);
	
	while (T--) {
		for (i = 0; i < MAXN * MAXN; ++i) g[i].clear();
		scanf("%d%d", &H, &W);
		for (i = 0; i < H; ++i)
			for (j = 0; j < W; ++j)
				scanf("%d", &att[i][j]);

		memset(vst, 0, sizeof(vst));
		char ch = 'a';
		for (i = 0; i < H; ++i)
			for (j = 0; j < W; ++j) {
				u = i * W + j;
				int x, y, r, c, min = 0x3f3f3f3f;
				x = y = -1;
				for (k = 0; k < 4; ++k) {
					r = i + dx[k];
					c = j + dy[k];
					if (!(r >= 0 && r < H && c >= 0 && c < W)) continue;
					if (att[r][c] < att[i][j] && att[r][c] < min) {
						min = att[r][c];
						x = r;
						y = c;
					}
				}
				if (x >= 0) {
					v = x * W + y;
					g[u].push_back(v);
					g[v].push_back(u);
				}
			}
		for (i = 0; i < H; ++i)
			for (j = 0; j < W; ++j) {
				u = i * W + j;
				if (vst[u]) continue;
				dfs(u, ch++);
			}
		printf("Case #%d:\n", ++cas);
		for (i = 0; i < H; ++i) {
			for (j = 0; j < W; ++j) {
				if (j) printf(" ");
				printf("%c", mat[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}


