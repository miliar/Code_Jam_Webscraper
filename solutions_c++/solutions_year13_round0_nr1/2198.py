#include <iostream>

using namespace std;

char g[10][10];

bool ok(char c) {
	int str = -1, stb = -1;
	for(int i = 0; i < 4; i ++)
		for(int j = 0; j < 4; j ++)
			if (g[i][j] == 'T')
				str = i, stb = j;
	if (str != -1)
		g[str][stb] = c;
	bool ok = false;
	bool ok_diag1 = true, ok_diag2 = true;
	for(int i = 0; i < 4; i ++) {
		bool ok_str = true;
		bool ok_stb = true;
		for(int j = 0; j < 4; j ++) {
			if (g[i][j] != c)
				ok_str = false;
			if (g[j][i] != c)
				ok_stb = false;
		}
		if (ok_str || ok_stb) {
			ok = true;
			break;
		}
		if (g[i][i] != c)
			ok_diag1 = false;
		if (g[i][3 - i] != c)
			ok_diag2 = false;
	}
	ok |= ok_diag1;
	ok |= ok_diag2;
	if (str != -1)
		g[str][stb] = 'T';
	return ok;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for(int k = 1; k <= t; k ++) {
		bool draw = true;
		for(int i = 0; i < 4; i ++) {
			for(int j = 0; j < 4; j ++) {
				scanf("%c", &g[i][j]);
				if (g[i][j] == '.')
						draw = false;
			}
			scanf("\n");
		}
		printf("Case #%d: ", k);
		if (ok('X'))
			printf("X won\n");
		else if (ok('O'))
			printf("O won\n");
		else {
			if (draw)
				printf("Draw\n");
			else 
				printf("Game has not completed\n");
		}
	}

	return 0;
}