#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int M = 510, N = 20, MOD = 10000;

char _s[M];
int _dp[M][N];
int _pos[256][N];
int _pend[256];

int DP(int m) {
    memset(_dp, 0, sizeof(_dp));
    
    // don't forget this.
    _dp[0][0] = 1;
    
    int i, j, k;
    for (i = 1; i <= m; ++i) {
        memcpy(_dp[i], _dp[i - 1], sizeof(_dp[0]));
        int *p = _pos[_s[i]];
        int pend = _pend[_s[i]];
        for (j = 0; j < pend; ++j) {
            k = p[j];
            _dp[i][k] = (_dp[i][k] + _dp[i - 1][k - 1]) % MOD;
        }
    }
    return _dp[m][19];
}

void InitP() {
    char s[] = "welcome to code jam";
    for (int i = 0; 0 != s[i]; ++i) {
        _pos[s[i]][_pend[s[i]]++] = i + 1;
    }
}

int main() {
    // freopen("C-small.in", "r", stdin);
    // freopen("C-large.in", "r", stdin);
    // freopen("out.txt", "w", stdout);
    InitP();
    int tc;
    scanf("%d\n", &tc);
    for (int tci = 1; tci <= tc; ++tci) {
        gets(_s + 1);
        // int m = strlen(_s);
        int m = strlen(_s + 1);
        printf("Case #%d: %04d\n", tci, DP(m));
    }
    return 0;
}
