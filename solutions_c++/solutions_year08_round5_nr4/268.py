#include <cstdio>

const int cmod = 10007;
const int maxn = 200;

int opt[maxn][maxn];
bool used[maxn][maxn];
int H, W, R;

void Init() {
    int i, j, a, b;
    scanf("%d %d %d", &H, &W, &R);
    for (i = 0; i < H; i++)
	for (j = 0; j < W; j++)
	    opt[i][j] = used[i][j] = 0;
    for (i = 0; i < R; i++) {
	scanf("%d %d", &a, &b);
	a--;
	b--;
	used[a][b] = 1;
    }
    opt[0][0] = 1;
    for (i = 0; i < H; i++)
	for (j = 0; j < W; j++)
	    if (!used[i][j] && opt[i][j]) {
		(opt[i + 1][j + 2] += opt[i][j]) %= cmod;
		(opt[i + 2][j + 1] += opt[i][j]) %= cmod;
	    }
    printf("%d\n", opt[H - 1][W - 1]);
}

int main() {
    int t, i;
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
	printf("Case #%d: ", i + 1);
	Init();
	//Work();
    }
    return 0;
}
