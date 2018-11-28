#include <stdlib.h>
#include <stdio.h>
#include <string.h>

const int dir[4][2] = {{-1, 0}, {0, -1}, {0, +1}, {+1, 0}};

int mat[110][110], H, W;
char cont, ans[110][110];

void go(int a, int b) {
	if (ans[a][b] != 0) return;
	bool sink = true;
	for (int i=0;i<4;i++) {
		int ii = a + dir[i][0];
		int jj = b + dir[i][1];
		if (ii >= 0 && ii < H && jj >= 0 && jj < W && mat[ii][jj] < mat[a][b])
			sink = false;
	}
	if (sink) {
		ans[a][b] = cont;
		cont++;
		return;
	}
	int menor = mat[a][b];
	int menori, menorj;
	for (int i=0;i<4;i++) {
		int ii = a + dir[i][0];
		int jj = b + dir[i][1];
		if (ii >= 0 && ii < H && jj >= 0 && jj < W && mat[ii][jj] < menor) {
			menori = ii;
			menorj = jj;
			menor = mat[ii][jj];
		}
	}
	go(menori, menorj);
	ans[a][b] = ans[menori][menorj];
}


int main() {
	int T, _42=1;
	scanf(" %d", &T);
	while (T--) {
		scanf(" %d %d", &H, &W);
		for (int i=0;i<H;i++) {
			for (int j=0;j<W;j++) {
				scanf(" %d", &mat[i][j]);
			}
		}
		memset(ans, 0, sizeof(ans));
		cont = 'a';
		for (int i=0;i<H;i++) {
			for (int j=0;j<W;j++) if (ans[i][j] == 0) {
				go(i, j);
			}
		}
		printf("Case #%d:\n", _42++);
		for (int i=0;i<H;i++) {
			for (int j=0;j<W-1;j++) {
				printf("%c ", ans[i][j]);
			}
			printf("%c\n", ans[i][W-1]);
		}
	}
	return 0;
}
