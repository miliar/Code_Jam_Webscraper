#include <cstdio>
#include <cmath>
#include <cstdlib>

char map[4][5];

void input() {
	for(int i = 0;i < 4;i ++) scanf("%s", map[i]);
}

int win(char c) {
	for(int i = 0;i < 4;i ++) {
		int ok = 1;
		for(int j = 0;j < 4;j ++) if(map[i][j] != c&&map[i][j] != 'T') { ok = 0; break;}
		if(ok) return 1;
	}

	for(int i = 0;i < 4;i ++) {
		int ok = 1;
		for(int j = 0;j < 4;j ++) if(map[j][i] != c&&map[j][i] != 'T') { ok = 0; break;}
		if(ok) return 1;
	}

	int ok = 1;
	for(int i = 0;i < 4;i ++) if(map[i][i] != c&&map[i][i] != 'T') { ok = 0; break; }
	if(ok) return 1;

	ok = 1;
	for(int i = 0;i < 4;i ++) if(map[i][3-i] != c&&map[i][3-i] != 'T') { ok = 0; break; }
	if(ok) return 1;

	return 0;
}

int count() {
	int res = 0;
	for(int i = 0;i < 4;i ++) for(int j = 0;j < 4;j ++) if(map[i][j] != '.') ++ res;

	return res;
}

void solve() {
	if(win('X')) printf("X won\n");
	else if(win('O')) printf("O won\n");
	else if(count() == 16) printf("Draw\n");
	else printf("Game has not completed\n");
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int cas = 1;cas <= t;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
	return 0;
}