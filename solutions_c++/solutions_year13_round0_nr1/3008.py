#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char mp[5][5];
int cc[10][4];

int cid(char c) {
	if (c == 'O') return 0;
	if (c == 'X') return 1;
	if (c == 'T') return 2;
	return 3;
}

int main() {
	int test; scanf("%d", &test);
	for (int cas = 1; cas <= test; ++cas) {
		for (int i = 0; i < 4; ++i)
			scanf("%s", mp[i]);
		memset(cc, 0, sizeof cc);
		bool end = true;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				int c = cid(mp[i][j]);
				if (c == 3) end = false;
				cc[i][c]++;
				cc[4 + j][c]++;
				if (i == j) cc[8][c]++;
				if (i + j == 3) cc[9][c]++;
			}
		int k; char winner;
		for (k = 0; k < 10; ++k) {
			if (cc[k][0] == 4 || cc[k][2] == 1 && cc[k][0] == 3) {
				winner = 'O';
				break;
			}
			if (cc[k][1] == 4 || cc[k][2] == 1 && cc[k][1] == 3) {
				winner = 'X';
				break;
			}
		}
		printf("Case #%d: ", cas);
		if (k < 10) {
			printf("%c won\n", winner);
		} else {
			puts(end ? "Draw" : "Game has not completed");
		}
	}
	return 0;
}
