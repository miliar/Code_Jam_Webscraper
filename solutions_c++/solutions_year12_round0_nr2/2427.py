#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define MAXN 110
#define PI 3.141592653589793238

using namespace std;

bool f[MAXN][MAXN][MAXN];
bool c[MAXN][2][2];
int n, S, P;
int ntest;

int getType(int x, int y, int z) {
    int big = max(x, max(y, z));
    int small = min(x, min(y, z));
    if (big - small > 2) return -1;
    if (big - small == 2) return 1;
    return 0;
}

int main() {
    freopen("2.inp", "r", stdin);
    freopen("2.out", "w", stdout);
    
    scanf("%d", &ntest);
    for (int test = 1; test <= ntest; test++) {
        scanf("%d%d%d", &n, &S, &P);
        memset(c, false, sizeof(c));
        for (int i = 0; i < n; i++) {
            int t;
            scanf("%d", &t);
            for (int x1 = 0; x1 <= t; x1++)
                for (int x2 = 0; x2 <= t - x1; x2++) {
                    int x3 = t - x1 - x2;
                    if (x1 > 10 || x2 > 10 || x3 > 10) continue;
                    int type = getType(x1, x2, x3);
                    int best = max(x1, max(x2, x3));
                    //cout << x1 << ' ' << x2 << ' ' << x3 << ' ' << type << endl;
                    if (type != -1)
                       c[i][type][best >= P ? 1 : 0] = true;
                }
        }
        memset(f, false, sizeof(f));
        f[n][0][0] = true;
        for (int i = n; i > 0; i--)
            for (int j = 0; j <= S; j++)
                for (int k = 0; k <= n; k++)
                    if (f[i][j][k]) 
                       for (int x = 0; x <= 1; x++)
                           for (int y = 0; y <= 1; y++)
                               if (c[i - 1][x][y])
                                  f[i - 1][j + x][k + y] = true;
        int ans = 0;
        for (int k = 0; k <= n; k++)
            if (f[0][S][k]) ans = max(ans, k);
        cout << "Case #" << test << ": " << ans << endl;
    }
}
