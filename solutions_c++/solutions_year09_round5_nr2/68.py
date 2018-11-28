
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAX_A = 26 + 5;
const int MAX_L = 10000 + 5;
const int MAX_N = 100 + 5;
const int MAX_L2 = 50 + 5;
const int MAX_K = 10 + 5;
const int MOD = 10009;

int c[MAX_N][MAX_N];

int N, K, L;
int am[MAX_A];
char expr[MAX_L];
char words[MAX_N][MAX_L2];

int rec(int at, int cnt, int mul, int have) {
//    printf("rec(%d, %d, %d)\n", at, cnt, mul);
    if (cnt == 0) {
        int sum = 0;
        for (int i = 0; i < L; ++i)
            if (i == 0 || expr[i - 1] == '+') {
                int by = 1;
                for (int j = 0; expr[i + j] >= 'a' && expr[i + j] <= 'z'; ++j)
                    by = (by * am[expr[i + j] - 'a']) % MOD;
                sum = (sum + by) % MOD;
            }
        return (sum * mul) % MOD;
    }
    if (at == N)
        return 0;
    int res = rec(at + 1, cnt, mul, have);
    for (int z = 1; z <= cnt; ++z) {
        int len = strlen(words[at]);
        for (int i = 0; i < len; ++i)
            am[words[at][i] - 'a'] += z;
        int all = have + z;
        res = (res + rec(at + 1, cnt - z, (mul * c[all][z]) % MOD, have + z)) % MOD;
        for (int i = 0; i < len; ++i)
            am[words[at][i] - 'a'] -= z;
    }
    return res;
}

int main() {
    for (int i = 0; i < MAX_N; ++i) {
        c[i][0] = 1;
        c[i][i] = 1;
        for (int j = 1; j < i; ++j)
            c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % MOD;
    }
    
    int tst;
    scanf("%d", &tst);
    for (int cas = 0; cas < tst; ++cas) {
        scanf("%s %d", expr, &K);
        L = strlen(expr);
        scanf("%d", &N);
        for (int i = 0; i < N; ++i)
            scanf("%s", words[i]);
        memset(am, 0, sizeof(am));
        printf("Case #%d:", cas + 1);
        for (int k = 1; k <= K; ++k)
            printf(" %d", rec(0, k, 1, 0));
        puts("");
    }
    return 0;
}