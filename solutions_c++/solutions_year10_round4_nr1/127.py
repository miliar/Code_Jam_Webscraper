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
#define MAXN 300
#define PP 105

int t[MAXN][MAXN];

LL solve() {
    for (int i = 0; i < MAXN; i++) {
        for (int j = 0; j < MAXN; j++)
            t[i][j] = 0;
    }
    int n;
    scanf("%d", &n);
    vector<PI> v;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            int p;
            scanf("%d", &p);
            int y = i;
            int x = n - i - 1 + 2 * j;
            t[x][y] = p + 1;
            v.PB(PI(x, y));
        }
    }
    for (int i = n - 2; i >= 0; i--) {
        for (int j = 0; j <= i; j++) {
            int p;
            scanf("%d", &p);
            int y = 2 * n - i - 2;
            int x = n - i - 1 + 2 * j;
            t[x][y] = p + 1;
            v.PB(PI(x,y));
        }
    }
    int ret = INF;
    for (int i = 0; i <= PP; i++) {
        for (int j = 0; j <= PP; j++) {
            int w = 0;
            bool czy = true;
            for (int k = 0; k < v.size() && czy; k++) {
                int x = v[k].FI;
                int y = v[k].SE;
                int x2 = 2 * i - x;
                int y2 = 2 * j - y;
                if (x2 >= 0 && t[x2][y] != 0 && t[x2][y] != t[x][y]) czy = false;
                if (y2 >= 0 && t[x][y2] != 0 && t[x][y2] != t[x][y]) czy = false;
                w = max(w, abs(i - x) + abs(j - y));
            }
            if (czy) {
                w++;
                ret = min(ret, w * w - n * n);
            }
        }
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

