#define see(n) cerr << #n << " = " << n << endl
#define seeArray(n, a) cerr << #a << " = ";\
    for (int __i__ = 0; __i__ < (int) n; ++__i__)\
        cerr << a[__i__] << " ";\
    cerr << endl;
#define seeArray2(n, m, a) cerr << #a << " = " << endl;\
    for (int __i__ = 0; __i__ < (int) n; ++__i__) {\
        for (int __j__ = 0; __j__ < (int) m; ++__j__)\
            cerr << a[__i__][__j__] << " ";\
        cerr << endl;\
    }
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <list>
#include <sstream>
#include <cctype>
#include <ctime>
using namespace std;
const int dir[8][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 }, { -1, -1 }, { -1, 1 }, { 1, -1 }, { 1, 1 } };
const int inf = 1000000000;
const int infll = 1000000000000000000LL;
const double eps = 1e-10;
const double pi = acos(-1.0);

const int maxn = 20000;
int cases, cas = 1;
int n, m, tar;
int gate[maxn];
bool change[maxn];
int val[maxn];
int ans;
int mem[maxn][2];

void solve(int now) {
    if (now > m) {
        if (val[now] == 0) {
            mem[now][0] = 0;
        } else {
            mem[now][1] = 0;
        }
        return;
    }
    solve(now * 2); solve(now * 2 + 1);
    if (gate[now] == 1) {
        mem[now][1] = min(mem[now][1], mem[now * 2][1] + mem[now * 2 + 1][1]);
        mem[now][0] = min(mem[now][0], mem[now * 2][0]);
        mem[now][0] = min(mem[now][0], mem[now * 2 + 1][0]);
    } else {
        mem[now][0] = min(mem[now][0], mem[now * 2][0] + mem[now * 2 + 1][0]);
        mem[now][1] = min(mem[now][1], mem[now * 2][1]);
        mem[now][1] = min(mem[now][1], mem[now * 2 + 1][1]);
    }

    if (change[now]) {
        gate[now] ^= 1;
        if (gate[now] == 1) {
            mem[now][1] = min(mem[now][1], mem[now * 2][1] + mem[now * 2 + 1][1] + 1);
            mem[now][0] = min(mem[now][0], mem[now * 2][0] + 1);
            mem[now][0] = min(mem[now][0], mem[now * 2 + 1][0] + 1);
        } else {
            mem[now][0] = min(mem[now][0], mem[now * 2][0] + mem[now * 2 + 1][0] + 1);
            mem[now][1] = min(mem[now][1], mem[now * 2][1] + 1);
            mem[now][1] = min(mem[now][1], mem[now * 2 + 1][1] + 1);
        }
        gate[now] ^= 1;
    }
}

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d%d", &n, &tar);
        m = (n - 1) / 2;
        for (int i = 1; i <= m; ++i) {
            int b;
            scanf("%d%d", &gate[i], &b);
            if (gate[i] != 1) {
                gate[i] = 0;
            }
            change[i] = (b == 1);
        }
        for (int i = m + 1; i <= n; ++i) {
            scanf("%d", &val[i]);
        }
        for (int i = 0; i < maxn; ++i) {
            mem[i][0] = mem[i][1] = inf;
        }
        solve(1);
        printf("Case #%d: ", cas++);
        if (mem[1][tar] < inf) {
            printf("%d\n", mem[1][tar]);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
