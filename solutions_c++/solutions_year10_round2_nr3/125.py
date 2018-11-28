#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>

#include <iostream>
#include <algorithm>
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <iostream>

#define TASK "c"
#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)
#define CLR(x) memset(x, 0, sizeof(x))
#define forn(i, n) for (int i = 0; i < n; i++)

using namespace std;

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int INF = 0x3f3f3f3f;
const int64 INF64 = (int64)INF * (int64)INF;

const int N = 600;
const int MOD = 100003;

int c[N][N], f[N][N], g[N];

int main() {
    freopen(TASK ".in", "rt", stdin);
    freopen(TASK ".out", "wt", stdout);

    CLR(c);
    forn(i, N) c[i][0] = 1; 
    for(int i = 1; i < N; i++) 
        for(int j = 1; j < N; j++) 
            c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD;
    
    CLR(f);
    f[2][1] = 1;
    for (int n = 3; n < N; n++) {
        f[n][1] = 1;
        for (int k = 2; k < n; k++) {
            for (int l = 0; l <= n - k - 1; l++) {
                int64 temp = ((int64)c[n - k - 1][l] * (int64)f[k][k - l - 1]) % MOD;
                f[n][k] = (f[n][k] + temp) % MOD;
            }
        }
    }

    CLR(g);
    for (int n = 2; n < N; n++) {
        for (int i = 0; i < N; i++)
            g[n] = (g[n] + f[n][i]) % MOD;
    }
                                                          

    int T;
    scanf("%d", &T);
    forn(t, T) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: %d\n", t + 1, g[n]);
    }

    return 0;
}
