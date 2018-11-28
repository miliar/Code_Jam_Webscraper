#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <cassert>

#define FI first
#define SE second
#define PB push_back
using namespace std;
typedef long long LL;
typedef pair<int, int> PI;
#define INF 1000000000000LL
#define MAXN 10000

LL t[MAXN][12];

LL solve() {
    for (int i = 0; i < MAXN; i++)
        for (int j = 0; j < 12; j++)
            t[i][j] = INF;
    int n;
    scanf("%d", &n);
    int N = (1 << n);
    for (int i = 2 * N - 1; i >= N; i--) {
        int p;
        scanf("%d", &p);
        for (int j = 0; j <= p; j++) {
            t[i][j] = 0;
        }
    }
    for (int i = N - 1; i > 0; i--) {
        int p;
        scanf("%d", &p);
        for (int j = 0; j <= n; j++) {
            t[i][j] = min(t[i * 2][j] + t[i * 2 + 1][j] + p,
                    t[i * 2][j + 1] + t[i * 2 + 1][j + 1]);
        }
    }
    return t[1][0];
}

int main() {
    int te;
    scanf("%d", &te);
    for (int l = 1; l <= te; l++) {
        LL ret = solve();
        printf("Case #%d: %lld\n", l, ret);
    }
}

