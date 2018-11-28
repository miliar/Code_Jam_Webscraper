#include <iostream>
#include <cstdio>
#include <algorithm>

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define FORR(i, n) FOR(i, 0, n)
using namespace std;

char matrix[4][4];

int status() {
	bool ok = false;
	int qtd = 0, qtd1, qtd2, qtd3 = 0, qtd4 = 0, qtd5 = 0, qtd6 = 0;
	char c1 = 'X', c2 = 'O';
	FORR(i, 4) {
		qtd1 = qtd2 = 0;
		if(matrix[i][i] == 'X' || matrix[i][i] == 'T') qtd3++;
		if(matrix[i][i] == 'O' || matrix[i][i] == 'T') qtd4++;
		if(matrix[i][3-i] == 'X' || matrix[i][3-i] == 'T') qtd5++;
		if(matrix[i][3-i] == 'O' || matrix[i][3-i] == 'T') qtd6++;
		FORR(j, 4) {
			if(matrix[i][j] == '.') ok = true;
			if(matrix[i][j] == 'X' || matrix[i][j] == 'T') qtd1++;
			if(matrix[i][j] == 'O' || matrix[i][j] == 'T') qtd2++;
		}
		if(qtd1 == 4) return 0;
		if(qtd2 == 4) return 1;
		qtd1 = qtd2 = 0;
		FORR(j, 4) {
			if(matrix[j][i] == 'X' || matrix[j][i] == 'T') qtd1++;
			if(matrix[j][i] == 'O' || matrix[j][i] == 'T') qtd2++;
		}
		if(qtd1 == 4) return 0;
		if(qtd2 == 4) return 1;
	}
	if(qtd3 == 4 || qtd5 == 4) return 0;
	if(qtd4 == 4 || qtd6 == 4) return 1;
	return (ok ? 3 : 2);
}

int main() {
	int t, res;
	char c;
	scanf("%d", &t);
	FORR(l, t) {
		FORR(i, 4) {
			FORR(j, 4) {
				scanf(" %c", &matrix[i][j]);
			}
		}
		res = status();
		printf("Case #%d: ", l+1);
		if(res == 0) printf("X won\n");
		else if(res == 1) printf("O won\n");
		else if(res == 2) printf("Draw\n");
		else printf("Game has not completed\n");
	}
}
