#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

string grid[4], bl;

int conta(){
	char blank = 0;
	int xx, oo; xx=oo=0;
	// Horizontais:
	for (int i = 0; i<4; i++){
		for (int j = 0; j<4; j++){
			if (grid[i][j]=='X' || grid[i][j] == 'T') xx++;
			if (grid[i][j]=='O' || grid[i][j] == 'T') oo++;
			if (grid[i][j]=='.') blank = 1;
		}

		if (xx == 4) return 1;
		if (oo == 4) return 2;
		xx = oo = 0;
	}

	// Verticais:
	for (int i = 0; i<4; i++){
		for (int j = 0; j<4; j++){
			if (grid[j][i]=='X' || grid[j][i] == 'T') xx++;
			if (grid[j][i]=='O' || grid[j][i] == 'T') oo++;
		}

		if (xx == 4) return 1;
		if (oo == 4) return 2;
		xx = oo = 0;
	}

	// Diag 1:
	for (int i = 0; i<4; i++){
		if (grid[i][i]=='X' || grid[i][i] == 'T') xx++;
		if (grid[i][i]=='O' || grid[i][i] == 'T') oo++;
	}

	if (xx == 4) return 1;
	if (oo == 4) return 2;
	xx = oo = 0;

	// Diag 2:
	for (int i = 0; i<4; i++){
		if (grid[i][3-i]=='X' || grid[i][3-i] == 'T') xx++;
		if (grid[i][3-i]=='O' || grid[i][3-i] == 'T') oo++;
	}

	if (xx == 4) return 1;
	if (oo == 4) return 2;
	xx = oo = 0;

	return blank?0:3;
}

int main(){
	int t; scanf("%d", &t);
	int exec = 0;
	while (t--){
		for (int i = 0; i<4; i++)
			cin >> grid[i];

		int ans = conta();
		printf("Case #%d: ", ++exec);
		if (!ans) {
			printf("Game has not completed\n");
		} else if (ans == 1){
			printf("X won\n");
		} else if (ans == 2){
			printf("O won\n");
		} else {
			printf("Draw\n");
		}
	}
	return 0;
}