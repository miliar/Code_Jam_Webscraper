#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

#define FI first
#define SE second
#define PB push_back

using namespace std;
typedef long long LL;
typedef pair<int, int> PI;

#define MAXN 500
const LL MOD = 100003;
LL npok[MAXN + 3][MAXN + 3];
LL t[MAXN + 3][MAXN + 3];
LL d[MAXN + 3];

LL solve() {
    npok[0][0] = 1;
    for (int i = 1; i <= MAXN; i++) {
        npok[i][0] = 1;
        for (int j = 1; j <= i; j++)
            npok[i][j] = (npok[i - 1][j - 1] + npok[i - 1][j]) % MOD;
    }
    t[1][0] = 1;
    for (int i = 2; i <= MAXN; i++) {
        for (int j = 1; j < i; j++) {
            for (int k = 0; k < j; k++) {
                t[i][j] += t[j][k] * npok[i - j - 1][j - k - 1];
            }
            d[i] = (d[i] + t[i][j]) % MOD;
        }
    }
}


int main() {
    solve();
    int te;
    scanf("%d", &te);
    for (int l = 1; l <= te; l++) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: %lld\n", l, d[n]);
    }
}

