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
#define INF 1000000000
#define MAXN 100
int t[MAXN + 3][MAXN + 3];
LL solve() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        for (int j = x1; j <= x2; j++) {
            for (int k = y1; k <= y2; k++) {
                t[j][k] = 1;
            }
        }
    }
    LL ret = 0;
    bool czy = true;
    while (czy) {
        czy = false;
        for (int i = MAXN; i > 0; i--)
            for (int j = MAXN; j > 0; j--) {
                if (t[i][j] && !t[i - 1][j] && !t[i][j - 1]) t[i][j] = 0;
                if (t[i - 1][j] && t[i][j - 1]) t[i][j] = 1;
                if (t[i][j]) czy = true;
            }
        ret++;
    }
    return ret;
}


int main() {
    int te;
    scanf("%d", &te);
    for (int l = 1; l <= te; l++) {
        LL ret = solve();
        printf("Case #%d: %lld\n", l, ret);
    }
}

