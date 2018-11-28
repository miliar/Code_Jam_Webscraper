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

int xmult(int x1, int y1, int x2, int y2) {
    return x1 * y2 - x2 * y1;
}

int cases, cas = 1;
int n, m;
int area;

int calc(int x1, int y1, int x2, int y2) {
    int ret = 0;
    ret += xmult(0, 0, x1, y1);
    ret += xmult(x1, y1, x2, y2);
    ret += xmult(x2, y2, 0, 0);
    return abs(ret);
}

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d%d%d", &n, &m, &area);
        int x1, y1, x2, y2;
        for (x1 = 0; x1 <= n; ++x1) for (y1 = 0; y1 <= m; ++y1) for (x2 = 0; x2 <= n; ++x2) for (y2 = 0; y2 <= m; ++y2) {
            int tmp = calc(x1, y1, x2, y2);
            if (tmp == area) {
                goto out;
            }
        }
out:
        printf("Case #%d: ", cas++);
        if (x1 <= n) {
            printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
