#include <cstdio>
#include <iostream>
using namespace std;
char c[5][5];
int n, m, i, j;
bool over;
bool winX, winO;
bool ff;
int T;
int x, y;
int cas;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> T;
	while (T--){
		over = true;
		winX = false; winO = false;
		x = 0; y = 0;
		for (i = 1; i <= 4; i++)
			for (j = 1; j <= 4; j++){
				cin >> c[i][j];
				if (c[i][j] == '.')
					over = false;
				if (c[i][j] == 'T')
					x = i, y = j;
			}
		c[x][y] = 'X';
		for (i = 1; i <= 4; i++){
			ff = true;
			for (j = 1; j <= 4; j++)
				ff &= c[i][j] == 'X';
			if (ff) { winX = true; break;}
			ff = true;
			for (j = 1; j <= 4; j++)
				ff &= c[j][i] == 'X';
			if (ff) { winX = true; break;}
		}
		ff = true;
		for (i = 1; i <= 4; i++)
			ff &= c[i][i] == 'X';
		if (ff) winX = true;
		ff = true;
		for (i = 1; i <= 4; i++)
			ff &= c[i][5 - i] == 'X';
		if (ff) winX = true;
		c[x][y] = 'O';
		for (i = 1; i <= 4; i++){
			ff = true;
			for (j = 1; j <= 4; j++)
				ff &= c[i][j] == 'O';
			if (ff) { winO = true; break;}
			ff = true;
			for (j = 1; j <= 4; j++)
				ff &= c[j][i] == 'O';
			if (ff) { winO = true; break;}
		}
		ff = true;
		for (i = 1; i <= 4; i++)
			ff &= c[i][i] == 'O';
		if (ff) winO = true;
		ff = true;
		for (i = 1; i <= 4; i++)
			ff &= c[i][5 - i] == 'O';
		if (ff) winO = true;
		printf("Case #%d: ", ++cas);
		if (winX) puts("X won");
		else
		if (winO) puts("O won");
		else
		if (over) puts("Draw");
		else puts("Game has not completed");
	}
}
