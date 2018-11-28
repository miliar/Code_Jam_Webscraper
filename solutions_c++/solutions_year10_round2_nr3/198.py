#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

const int maxn = 500 + 10;
const int inf = (-1u) >> 1;
const int mod = 100003;

int Case = 1, n, f[maxn][maxn], t[maxn];
int com[maxn][maxn];

void make() {
    for (int i = 0; i < maxn; ++i)
        com[i][0] = com[i][i] = 1;
    for (int i = 2; i < maxn; ++i)
        for (int j = 1; j < i; ++j)
            com[i][j] = (com[i - 1][j] + com[i - 1][j - 1]) % mod;
}

void init() {
    scanf ("%d", &n);
}

void solve() {
    printf ("Case #%d: ", Case++);
    printf ("%d\n", t[n]);
}

//#define SMALL
#define LARGE

int main() {
    string name = "C";
    #ifdef SMALL
    freopen ((name + "-small-attempt2.in").c_str(), "r", stdin);
    freopen ((name + "-small.out").c_str(), "w", stdout);
    #endif
    #ifdef LARGE
    freopen ((name + "-large.in").c_str(), "r", stdin);
    freopen ((name + "-large.out").c_str(), "w", stdout);
    #endif
    
    int testCase;
    make();
    f[2][1] = t[2] = 1;
    for (int i = 3; i < maxn; ++i) {
        f[i][1] = t[i] = 1;
        for (int k = 2; k < i; ++k) {
            f[i][k] = 0;
            int tot = i - k - 1;
            for (int j = k - 1; j >= 1; --j) {
                int need = k - 1 - j;
                if (need > tot)
                    break;
                f[i][k] = ((long long)f[k][j] * com[tot][need] % mod
                        + f[i][k]) % mod;
            }
            t[i] = (t[i] + f[i][k]) % mod;
        }
    }
    scanf ("%d\n", &testCase);
    while (testCase--) {
        init();
        solve();
    }
    
    return 0;
}

