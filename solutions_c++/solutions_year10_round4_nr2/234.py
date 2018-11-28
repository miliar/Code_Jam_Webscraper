#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int Inf = 1000000000 + 7;

#define two(a) (1 << (a))

int f[1 << 11][11];
int Cost[1 << 11];
int M[1 << 11];
int P, N;

int dfs(int d, int buys, int l, int r) {
    if(l == r) {
        if(buys <= M[l]) f[d][buys] = 0; else f[d][buys] = Inf;
        return f[d][buys];
    } 
    if(f[d][buys] != -1) return f[d][buys];
    int m = (l + r) / 2;
    f[d][buys] = min(dfs(2 * d, buys, l, m) + dfs(2 * d + 1, buys, m + 1, r), dfs(2 * d, buys - 1, l, m) + dfs(2 * d + 1, buys - 1, m + 1, r) + Cost[d]);
    if(f[d][buys] >= Inf)
        f[d][buys] = Inf;

    return f[d][buys];
}
int main() {
//    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("B-small-attempt1.in", "r", stdin);
//    freopen("input.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    int T, test = 1;

    for(scanf("%d", &T); T; T --) {
        printf("Case #%d: ", test ++);
        scanf("%d", &P);
        N = 1 << P;
        for(int i = 0; i < N; i ++) scanf("%d", &M[i]);
        for(int i = 0; i < P; i ++) 
            for(int j = 0; j < two(P - 1 - i); j ++) {
                scanf("%d", &Cost[two(P - 1 - i) + j]);
            }
        memset(f, -1, sizeof(f));
        printf("%d\n", dfs(1, P, 0, N - 1));
    }
    return 0;
}

