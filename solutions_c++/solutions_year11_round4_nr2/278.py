#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
const double pi = acos(-1.0);
const double eps = 1E-7;
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)

int a[505][505], f[505][505], p[505][505], q[505][505];
int n, m, D;

inline bool chk(int u, int v, int w)
{
    if (w % 2) {
        int x = w / 2 + u, y = w / 2 + v;
        int sp = p[u + w - 1][v + w - 1] - p[u + w - 1][v - 1] - p[u - 1][v + w - 1] + p[u - 1][v - 1];
        sp -= u * a[u][v] + u * a[u][v + w - 1] + (u + w - 1) * a[u + w - 1][v] + (u + w - 1) * a[u + w - 1][v + w - 1];
        int sq = q[u + w - 1][v + w - 1] - q[u + w - 1][v - 1] - q[u - 1][v + w - 1] + q[u - 1][v - 1];
        sq -= v * a[u][v] + (v + w - 1) * a[u][v + w - 1] + v * a[u + w - 1][v] + (v + w - 1) * a[u + w - 1][v + w - 1];
        int s2 = f[u + w - 1][v + w - 1] - f[u + w - 1][v - 1] - f[u - 1][v + w - 1] + f[u - 1][v - 1] - a[u][v] - a[u][v + w - 1] - a[u + w - 1][v] - a[u + w - 1][v + w - 1];
        if (sp == x * s2 && sq == y * s2) return 1; return 0;
    } else {
        int x = u * 2 + w - 1, y = v * 2 + w - 1;
        int sp = p[u + w - 1][v + w - 1] - p[u + w - 1][v - 1] - p[u - 1][v + w - 1] + p[u - 1][v - 1];
        sp -= u * a[u][v] + u * a[u][v + w - 1] + (u + w - 1) * a[u + w - 1][v] + (u + w - 1) * a[u + w - 1][v + w - 1];
        int sq = q[u + w - 1][v + w - 1] - q[u + w - 1][v - 1] - q[u - 1][v + w - 1] + q[u - 1][v - 1];
        sq -= v * a[u][v] + (v + w - 1) * a[u][v + w - 1] + v * a[u + w - 1][v] + (v + w - 1) * a[u + w - 1][v + w - 1];
        int s2 = f[u + w - 1][v + w - 1] - f[u + w - 1][v - 1] - f[u - 1][v + w - 1] + f[u - 1][v - 1] - a[u][v] - a[u][v + w - 1] - a[u + w - 1][v] - a[u + w - 1][v + w - 1];
        if (sp * 2 == x * s2 && sq * 2 == y * s2) return 1; return 0;
    }
}

char ts[10005];

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    int Test, tts = 0;
    for (scanf("%d", &Test); Test--; ) {
        printf("Case #%d: ", ++tts);
        scanf("%d%d%d", &n, &m, &D);
        for (int i = 1; i <= n; ++i) {
            scanf("%s", ts + 1);
            int u = 0, v = 0, w = 0;
            for (int j = 1; j <= m; ++j) {
                a[i][j] = ts[j] - '0';
                u += a[i][j];
                v += a[i][j] * i;
                w += a[i][j] * j;
                f[i][j] = f[i - 1][j] + u;
                p[i][j] = p[i - 1][j] + v;
                q[i][j] = q[i - 1][j] + w;
            }
        }

        int ans = 0;
        for (int i = 1; i <= n - 2; ++i)
        for (int j = 1; j <= m - 2; ++j)
        for (int k = min(n - i + 1, m - i + 1); k >= 3; --k) {
            if (k < ans) break;
            if (chk(i, j, k)) ans = k;
        }

        if (ans < 3) puts("IMPOSSIBLE"); else printf("%d\n", ans);
    }
    return 0;
}
