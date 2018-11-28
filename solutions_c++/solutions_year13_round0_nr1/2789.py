#include <bits/stdc++.h>
#define fr(a,b,c) for(int a = b; a < c; a++)
#define rp(a,b) fr(a,0,b)
using namespace std;

int di[] = {1,1,0,1};
int dj[] = {1,0,1,-1};
char g[10][10];

int dfs(int i, int j, int k, char p, int niv) {
	if (niv == 4) return ((p == 'X') ? 1 : 2);
	if (i < 0 || i >= 4 || j < 0 || j >= 4) return 0;
	//printf("%d %d %d %c %d %c\n", i, j, k, p, niv, g[i][j]);
	if (g[i][j] != p && g[i][j] != 'T') return 0;
	return dfs(i+di[k], j+dj[k], k, p, niv+1);
}

int win(int i, int j) {
	return dfs(i,j,0,'X',0)|dfs(i,j,0,'O',0)|dfs(i,j,1,'X',0)|dfs(i,j,1,'O',0)|dfs(i,j,2,'X',0)|dfs(i,j,2,'O',0)|dfs(i,j,3,'X',0)|dfs(i,j,3,'O',0);
}

int main() {
	int cas = 1;
	int T; scanf("%d", &T);
	while (T--) {
		bool draw = 1;
		rp(i,4) {
			scanf("%s", g[i]);
			rp(j,4) if (g[i][j] == '.') draw = 0;
		}
		int res = 0;
		rp(i,4) {
			res |= win(0,i);
			if (i) res |= win(i,0);
		}
		printf("Case #%d: ", cas++);
		if (!res && !draw) printf("Game has not completed\n");
		else if (!res && draw) printf("Draw\n");
		else if (res&1) printf("X won\n");
		else printf("O won\n");
	}
	return 0;
}