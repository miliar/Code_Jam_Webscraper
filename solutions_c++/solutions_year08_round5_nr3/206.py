#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 100;
const int maxs = 2000;

int opt[2][maxs];
char tab[maxn][maxn];
int R, C, full;

int Digit(int v) {
    int res = 0;
    for (; v; res += (v & 1), v >>= 1);
    return res;
}

void Init() {
    scanf("%d %d", &R, &C);
    int i;
    for (i = 0; i < R; i++)
	scanf("%s", tab[i]);
    full = 1 << C;
}

bool Check(int a, int b, const char *str) {
    int i;
    for (i = 0; i < C; i++)
	if ((1 << i) & b) {
	    if (str[i] != '.') return 0;
	    if (i && ((1 << (i - 1)) & b)) return 0;
	    if (i + 1 < C && ((1 << (i + 1)) & b)) return 0;
	    if (i && ((1 << (i - 1)) & a)) return 0;
	    if (i + 1 < C && ((1 << (i + 1)) & a)) return 0;
	}
    return 1;
}

void Work() {
    int t, curr = 0, prev = 0, i, j;
    for (i = 0; i < full; i++)
	opt[0][i] = -1;
    opt[0][0] = 0;
    for (t = 0; t < R; t++) {
	curr = 1 - prev;
	for (i = 0; i < full; i++)
	    opt[curr][i] = -1;
	for (i = 0; i < full; i++)
	    if (opt[prev][i] >= -1) {
		for (j = 0; j < full; j++)
		    if (Check(i, j, tab[t])) {
			opt[curr][j] = max(opt[curr][j], opt[prev][i] + Digit(j));
		    }
	    }
	prev = curr;
    }
    int ans = 0;
    for (i = 0; i < full; i++)
	ans = max(ans, opt[curr][i]);
    printf("%d\n", ans);
}

int main() {
    int t, i;
    scanf("%d", &t);
    for (i = 0; i < t; i++) {
	printf("Case #%d: ", i + 1);
	Init();
	Work();
    }
    return 0;
}
