#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

char s[4][4];

bool check(char ch) {
	for (int i = 0; i < 4; i++) {
		bool flag = true;
		for (int j = 0; j < 4; j++) if (s[i][j] != ch && s[i][j] != 'T') { flag = false; break; }
		if (flag) return true;
	}
	for (int i = 0; i < 4; i++) {
		bool flag = true;
		for (int j = 0; j < 4; j++) if (s[j][i] != ch && s[j][i] != 'T') { flag = false; break; }
		if (flag) return true;
	}
	bool flag = true;
	for (int i = 0; i < 4; i++) if (s[i][i] != ch && s[i][i] != 'T') { flag = false; break; }
	if (flag) return true;
	flag = true;
	for (int i = 0; i < 4; i++) if (s[i][3 - i] != ch && s[i][3 - i] != 'T') { flag = false; break; }
	if (flag) return true;
	return false;
}

bool find(char ch) {
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++) if (s[i][j] == ch) return true;
	return false;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		for (int i = 0; i < 4; i++) scanf("%s", s[i]);
		if (check('X')) printf("Case #%d: X won\n", cas);
		else {
			if (check('O')) printf("Case #%d: O won\n", cas);
			else {
				if (!find('.')) printf("Case #%d: Draw\n", cas);
				else printf("Case #%d: Game has not completed\n", cas);
			}
		}
	}
	return 0;
}
