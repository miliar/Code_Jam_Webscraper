#include<iostream>
using namespace std;

const int n = 4;
char map[n][n];

int main() {
	int testcases;
	scanf("%d", &testcases);
	char tmp;
	for (int t = 0; t < testcases; t++) {
		//printf("Case #%d:\n", t);
		scanf("%c", &tmp);
		int tot = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				scanf("%c", &map[i][j]);
				if (map[i][j] != '.')
					tot ++;
				//printf("%c", map[i][j]);
			}
			scanf("%c", &tmp);
			//printf("\n");
		}
		bool Xwin = false, Owin = false;
		for (int i = 0; i < n; i++) {
			int X = 0, O = 0, T = 0;
			for (int j = 0; j < n; j++) {
				if (map[i][j] == 'X') X++;
				if (map[i][j] == 'O') O++;
				if (map[i][j] == 'T') T++;
			}
			if (X == n || X == n - 1 && T == 1)
				Xwin = true;
			if (O == n || O == n - 1 && T == 1)
				Owin = true;
		}
		for (int i = 0; i < n; i++) {
			int X = 0, O = 0, T = 0;
			for (int j = 0; j < n; j++) {
				if (map[j][i] == 'X') X++;
				if (map[j][i] == 'O') O++;
				if (map[j][i] == 'T') T++;
			}
			if (X == n || X == n - 1 && T == 1)
				Xwin = true;
			if (O == n || O == n - 1 && T == 1)
				Owin = true;
		}
		int X = 0, O = 0, T = 0;
		for (int i = 0; i < n; i++) {
			if (map[i][i] == 'X') X++;
			if (map[i][i] == 'O') O++;
			if (map[i][i] == 'T') T++;			
		}
		if (X == n || X == n - 1 && T == 1)
			Xwin = true;
		if (O == n || O == n - 1 && T == 1)
			Owin = true;
		X = 0, O = 0, T = 0;
		for (int i = 0; i < n; i++) {
			if (map[i][n - i - 1] == 'X') X++;
			if (map[i][n - i - 1] == 'O') O++;
			if (map[i][n - i - 1] == 'T') T++;			
		}
		if (X == n || X == n - 1 && T == 1)
			Xwin = true;
		if (O == n || O == n - 1 && T == 1)
			Owin = true;
		printf("Case #%d: ", t + 1);
		if (Xwin)
			printf("X won\n");
		else if (Owin)
			printf("O won\n");
		else if (tot == n * n)
			printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;

}