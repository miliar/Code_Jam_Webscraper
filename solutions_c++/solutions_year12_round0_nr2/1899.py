#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

const int INF = (~0U>>2);
const double eps = 1e-6;

#define rep(i, n) for (int i = 0; i < n; i++)
#define SZ(a) (int)(a.size())
#define foreach(i, a) for (__typeof(a.begin()) it = a.begin(); it != a.end(); it++)

int N, S, p, f[105][105], t[105];

void solve() {
    scanf("%d %d %d", &N, &S, &p);
    rep(i, N) scanf("%d", &t[i]);
    memset(f, 0, sizeof(f));
    for (int j = 1; j <= S; j++) f[0][j] = -INF;
    f[0][0] = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j <= S; j++) {
            if (f[i][j] < 0) continue;
            if (t[i] % 3 == 0) {
                int a = t[i] / 3;
                if (a && j < S) { // a-1 a a+1
                    if (a + 1 >= p) {
                        f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + 1);
                    } else {
                        f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j]);
                    }
                }
                if (a >= p) { // a a a
                    f[i + 1][j] = max(f[i + 1][j], f[i][j] + 1);
                } else {
                    f[i + 1][j] = max(f[i + 1][j], f[i][j]);
                }
            } else
            if (t[i] % 3 == 1) {
                int a = t[i] / 3;
                if (a && j < S) { // a-1 a+1 a+1
                    if (a + 1 >= p) {
                        f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + 1);
                    } else {
                        f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j]);
                    }
                }
                if (a + 1 >= p) {
                    f[i + 1][j] = max(f[i + 1][j], f[i][j] + 1);
                } else {
                    f[i + 1][j] = max(f[i + 1][j], f[i][j]);
                }
            } else
            if (t[i] % 3 == 2) {
                int a = t[i] / 3;
                if (j < S) {
                    if (a + 2 >= p) {
                        f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + 1);
                    } else {
                        f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j]);
                    }
                }
                if (a + 1 >= p) {
                    f[i + 1][j] = max(f[i + 1][j], f[i][j] + 1);
                } else {
                    f[i + 1][j] = max(f[i + 1][j], f[i][j]);
                }
            }
        }
    printf("%d\n", f[N][S]);
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int testN;
    scanf("%d", &testN);
    for (int i = 1; i <= testN; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
