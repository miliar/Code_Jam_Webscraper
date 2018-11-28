/*
 * Sun Aug 10 00:08:41 KST 2008
 */
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
const long long infll = 1000000000000000000LL;
const double eps = 1e-10;
const double pi = acos(-1.0);

int cases, cas = 1;
long long mem[128][128];
bool rock[128][128];
int n, m, cnt;

int main() {
    for (scanf("%d", &cases); cases--; ) {
        memset(rock, false, sizeof(rock));
        scanf("%d%d%d", &n, &m, &cnt);
        for (int i = 0; i < cnt; ++i) {
            int x, y;
            scanf("%d%d", &x, &y);
            rock[x - 1][y - 1] = true;
        }
        memset(mem, 0, sizeof(mem));
        mem[0][0] = 1;
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) if (!rock[i][j]) {
            int x = i + 1, y = j + 2;
            if (x >= 0 && x < n && y >= 0 && y < m && !rock[x][y]) {
                mem[x][y] = (mem[x][y] + mem[i][j]) % 10007;
            }
            x = i + 2; y = j + 1;
            if (x >= 0 && x < n && y >= 0 && y < m && !rock[x][y]) {
                mem[x][y] = (mem[x][y] + mem[i][j]) % 10007;
            }
        }
        printf("Case #%d: %lld\n", cas++, mem[n - 1][m - 1]);
    }
    return 0;
}
