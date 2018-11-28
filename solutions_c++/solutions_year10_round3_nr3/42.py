#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

#define MAX_N 520

int N, M;
int C[MAX_N][MAX_N];
int D[MAX_N][MAX_N];
int Sizes[MAX_N];

void read() {
    char sir[1024];
    string b16 = "0123456789ABCDEF";
    scanf("%d %d", &M, &N);
    for (int i = 1; i <= M; ++i) {
        scanf("%s", sir);
        for (int j = 1; j * 4 <= N; ++j) {
            int ord = b16.find(sir[j - 1]);
            for (int k = 0; k < 4; ++k)
                C[i][4 * j - k] = ((ord >> k) & 1);
        }
    }
}

void build_DP() {
    for (int i = M; i >= 1; --i)
        for (int j = N; j >= 1; --j)
            if (C[i][j] == -1) {
                D[i][j] = 0;
            } else {
                D[i][j] = 1;
                if (!(i < M && C[i + 1][j] + C[i][j] == 1))
                    continue;
                if (!(j < N && C[i][j + 1] + C[i][j] == 1))
                    continue;
                int L = min(D[i + 1][j], D[i][j + 1]);
                D[i][j] = max(D[i][j], L);
                if (i + L <= M && j + L <= N && C[i][j] == C[i + L][j + L])
                    D[i][j] = max(D[i][j], L + 1);
            }
}

void solve() {
    int sol = 0;
    bool done = false;
    memset(Sizes, 0, sizeof(Sizes));
    while (!done) {
        build_DP();
        int dmax = -1;
        int dx, dy;
        for (int i = 1; i <= M; ++i)
            for (int j = 1; j <= N; ++j)
                if (dmax < D[i][j]) {
                    dmax = D[i][j];
                    dx = i;
                    dy = j;
                }

        if (dmax < 1) {
            done = true;
        } else {
            if (Sizes[dmax] == 0)
                ++sol;
            ++Sizes[dmax];
            for (int i = dx; i < dx + dmax; ++i)
                for (int j = dy; j < dy + dmax; ++j)
                    C[i][j] = -1;
        }
    }
    printf("%d\n", sol);
    for (int i = N; i > 0; --i)
        if (Sizes[i] > 0) {
            printf("%d %d\n", i, Sizes[i]);
        }
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        read();
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
