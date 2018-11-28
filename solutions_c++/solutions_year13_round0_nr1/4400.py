#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
using namespace std;
char g[10][10];
int main() {
	int T;
	scanf(" %d", &T);
	int cas = 1;
	while (T--) {
		for (int i = 0; i < 4; i++) {
			scanf(" %s", g[i]);
		}
		bool f = true;
		for (int j = 0; j < 4; j++) {
			if (g[0 + j][0 + j] != g[0][0] && g[0][0] != 'T'
					&& g[j][j] != 'T') {
				f = false;
				break;
			}
			if (g[j][j] == '.') {
				f = false;
				break;
			}
		}
		if (f) {
			char ch;
			if (g[0][0] != 'T') {
				ch = g[0][0];
			} else {
				ch = g[1][1];
			}
			printf("Case #%d: %c won\n", cas++, ch);
			continue;
		}

		f = true;
		for (int j = 0; j < 4; j++) {
			if (g[j][3 - j] != g[0][3] && g[j][3 - j] != 'T'
					&& g[0][3] != 'T') {
				f = false;
				break;
			}
			if (g[j][3 - j] == '.') {
				f = false;
				break;
			}
		}
		if (f) {
			char ch;
			if (g[0][3] != 'T') {
				ch = g[0][3];
			} else {
				ch = g[1][2];
			}
			printf("Case #%d: %c won\n", cas++, ch);
			continue;
		}
		bool out = false;
		for (int i = 0; i < 4; i++) {
			bool f = true;
			for (int j = 0; j < 4; j++) {
				if (g[i][j] != g[i][0] && g[i][0] != 'T' && g[i][j] != 'T') {
					f = false;
					break;
				}
				if (g[i][j] == '.') {
					f = false;
					break;
				}
			}
			if (f) {
				char ch;
				if (g[i][0] != 'T') {
					ch = g[i][0];
				} else {
					ch = g[i][1];
				}
				printf("Case #%d: %c won\n", cas++, ch);
				out = true;
				break;
			}
		}
		if (out)
			continue;
		for (int i = 0; i < 4; i++) {
			bool f = true;
			for (int j = 0; j < 4; j++) {
				if (g[j][i] != g[0][i] && g[0][i] != 'T' && g[j][i] != 'T') {
					f = false;
					break;
				}
				if (g[j][i] == '.') {
					f = false;
					break;
				}
			}
			if (f) {
				char ch;
				if (g[0][i] != 'T') {
					ch = g[0][i];
				} else {
					ch = g[1][i];
				}
				printf("Case #%d: %c won\n", cas++, ch);
				out = true;
				break;
			}
		}
		if (!out) {
			bool hasD = false;
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					if (g[i][j] == '.')
						hasD = true;
				}
			}
			if (hasD) {
				printf("Case #%d: Game has not completed\n", cas++);
			} else {
				printf("Case #%d: Draw\n", cas++);
			}
		}
	}
	return 0;
}
