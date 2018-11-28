#include <stdio.h>
#include <string.h>

int nprob, prob;
int L, T;
char S[20];
int mat[210][210][4];
int vis[210][210];
int tag[210][210];
int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, -1, 0, 1 };


void dfs(int x, int y) {
	if (vis[x][y]) return;
	vis[x][y] = 1;
	if (x > 0 && mat[x][y][2] == 0) dfs(x-1, y);
	if (x < 209 && mat[x][y][0] == 0) dfs(x+1, y);
	if (y > 0 && mat[x][y][1] == 0) dfs(x, y-1);
	if (y < 209 && mat[x][y][3] == 0) dfs(x, y+1);
}

int main() {
///	freopen("a.in", "r", stdin);
///	freopen("a.out", "w", stdout);
	
	scanf("%d", &nprob);
	for (prob = 1; prob <= nprob; prob++) {
		memset(mat, 0, sizeof(mat));
		
		int x = 105, y = 105, d = 0;
		scanf("%d", &L);
		for (int i = 0; i < L; i++) {
			scanf("%s%d", S, &T);
			while (T--) {
				for (int j = 0; S[j]; j++) {
					if (S[j] == 'L') {
						d = (d + 1) & 3;
					} else if (S[j] == 'R') {
						d = (d + 3) & 3;
					} else if (S[j] == 'F') {
						if (d == 0) {
							mat[x][y-1][3] = mat[x][y][1] = 1;
						} else if (d == 3) {
							mat[x-1][y][0] = mat[x][y][2] = 1;
						}
						x += dx[d]; y += dy[d];
						if (d == 1) {
							mat[x-1][y][0] = mat[x][y][2] = 1;
						} else if (d == 2) {
							mat[x][y-1][3] = mat[x][y][1] = 1;
						}
					}
				}
			}
		}
		
		memset(vis, 0, sizeof(vis));
		dfs(0, 0);
		
		memset(tag, 0, sizeof(tag));
		for (int i = 0; i < 210; i++) {
			for (int j = 1; j < 210; j++) {
				if (vis[j][i] && ((tag[j-1][i]&1) || !vis[j-1][i] && mat[j][i][2]))
					tag[j][i] |= 1;
			}
			for (int j = 208; j >= 0; j--) {
				if (vis[j][i] && ((tag[j+1][i]&2) || !vis[j+1][i] && mat[j][i][0]))
					tag[j][i] |= 2;
			}
		}
		for (int j = 0; j < 210; j++) {
			for (int i = 1; i < 210; i++) {
				if (vis[j][i] && ((tag[j][i-1]&4) || !vis[j][i-1] && mat[j][i][1]))
					tag[j][i] |= 4;
			}
			for (int i = 208; i >= 0; i--) {
				if (vis[j][i] && ((tag[j][i+1]&8) || !vis[j][i+1] && mat[j][i][3]))
					tag[j][i] |= 8;
			}
		}
		
		int ans = 0;
		for (int i = 0; i < 210; i++)
			for (int j = 0; j < 210; j++)
				if ((tag[i][j] & 3) == 3 || (tag[i][j] & 12) == 12)
					ans++;
					
		printf("Case #%d: %d\n", prob, ans);
	}
	
	return 0;
}
