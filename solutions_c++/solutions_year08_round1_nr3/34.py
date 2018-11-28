#include <cstdio>
#include <cmath>

const int maxn = 0;
const int cmod = 10000;

int mat[2][2], orig[2][2], c[2][2], a[2][2];

void Mul(int a[2][2], int b[2][2], int c[2][2]) {
    int i, j, k;
    for (i = 0; i < 2; i++)
	for (j = 0; j < 2; j++) {
	    c[i][j] = 0;
	    for (k = 0; k < 2; k++)
		(c[i][j] += a[i][k] * b[k][j]) %= cmod;
	}
}

void Copy(int a[2][2], int b[2][2]) {
    int i, j;
    for (i = 0; i < 2; i++)
	for (j = 0; j < 2; j++)
	    a[i][j] = b[i][j];
}

void Pow(int v) {
    int i, j;
    if (!v) {
	for (i = 0; i < 2; i++)
	    for (j = 0; j < 2; j++)
		mat[i][j] = 0;
	for (i = 0; i < 2; i++)
	    mat[i][i] = 1;
	return;
    }
    Pow(v / 2);
    Mul(mat, mat, c);
    Copy(mat, c);
    if (v & 1) {
	Mul(mat, orig, c);
	Copy(mat, c);
    }
}

void Solve(int n) {
    int i, j;
    for (i = 0; i < 2; i++)
	for (j = 0; j < 2; j++)
	    a[i][j] = 0;
    a[0][0] = 6;
    a[0][1] = 28;
    Pow(n - 2);
    Mul(a, mat, c);
    int res = c[0][1] - 1;
    res %= 1000;
    if (res < 0) res += 1000;
    printf("%03d\n", res);
}

int main() {
    orig[0][0] = 0;
    orig[0][1] = -4;
    orig[1][0] = 1;
    orig[1][1] = 6;
    int t, i, n;
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
	printf("Case #%d: ", i + 1);
	scanf("%d", &n);
	Solve(n);
    }
    return 0;
}
