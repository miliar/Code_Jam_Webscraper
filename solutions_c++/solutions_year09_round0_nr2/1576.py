#include <stdio.h>
#include <algorithm>
using namespace std;

int T, H, W, A[100][100];
int U[10000]; char P[10000];

int uroot(int a) { return U[a] < 0 ? a : U[a] = uroot(U[a]); }
void uset(int a, int b) {
	a = uroot(a); b = uroot(b);
	if (a == b) return;
	if (U[b] < U[a]) swap(a, b);
	U[a] += U[b]; U[b] = a;
}

int main() {
	scanf("%d", &T);
	for (int case_x = 1; case_x <= T; case_x++) {
		printf("Case #%d:\n", case_x);
		scanf("%d%d", &H, &W);
		for (int y = 0; y < H; y++)
		 for (int x = 0; x < W; x++)
		  scanf("%d", &A[x][y]);
		for (int i = 0; i < W * H; i++)
		 U[i] = -1, P[i] = 0;
		for (int y = 0; y < H; y++)
		 for (int x = 0; x < W; x++) {
			int al = A[x][y], tx = x, ty = y;
			if (0 < y && A[x][y - 1] < al)
			 tx = x, ty = y - 1, al = A[tx][ty];
			if (0 < x && A[x - 1][y] < al)
			 tx = x - 1, ty = y, al = A[tx][ty];
			if (x + 1 < W && A[x + 1][y] < al)
			 tx = x + 1, ty = y, al = A[tx][ty];
			if (y + 1 < H && A[x][y + 1] < al)
			 tx = x, ty = y + 1, al = A[tx][ty];
			uset(y * W + x, ty * W + tx);
		}
		char alp = 'a';
		for (int y = 0; y < H; y++)
		 for (int x = 0; x < W; x++, printf(x == W ? "\n" : " ")) {
			int id = uroot(y * W + x);
			if (!P[id]) P[id] = alp, alp++;
			printf("%c", P[id]);
		}
	}
	return 0;
}
