/*
 * Sat Jun  5 22:55:58 CST 2010
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
#include <numeric>
using namespace std;
const int dir[8][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 }, { -1, -1 }, { -1, 1 }, { 1, -1 }, { 1, 1 } };
const int inf = 1000000000;
const long long infll = 1000000000000000000LL;
const double eps = 1e-10;
const double pi = acos(-1.0);

int cases, cas = 1;
int ep;
int price[16][2048];
int miss[2048];
int mem[16][1024][1024];

int calc(int level, int from, int mask) {
    int& ret = mem[level][from][mask];
    if (ret >= 0) {
        return ret;
    }
    int to = from + (1 << (level + 1)); bool ok = true;
    for (int i = from; i < to && ok; ++i) if (miss[i] > 0) {
        ok = false;
    }
    if (ok) {
        return ret = 0;
    }
    if (level <= 0) {
        return ret = ((miss[from] <= 1 && miss[from + 1] <= 1) ? price[level][from] : inf);
    }

    int ret1 = calc(level - 1, from, mask), ret2 = calc(level - 1, from + (1 << level), mask);
    if (ret1 < inf && ret2 < inf) {
        ret = ret1 + ret2;
    } else {
        ret = inf;
    }

    int newmask = (mask ^ (1 << level));
    for (int i = from; i < to; ++i) {
        miss[i]--;
    }
    ret1 = calc(level - 1, from, newmask); ret2 = calc(level - 1, from + (1 << level), newmask);
    for (int i = from; i < to; ++i) {
        miss[i]++;
    }
    if (ret1 < inf && ret2 < inf) {
        ret = min(ret, ret1 + ret2 + price[level][from]);
    }

    return ret;
}

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d", &ep);
        for (int i = 0; i < (1 << ep); ++i) {
            scanf("%d", &miss[i]); miss[i] = ep - miss[i];
        }
        for (int level = 0; level < ep; ++level) for (int from = 0; from < (1 << ep); from += (1 << (level + 1))) {
            scanf("%d", &price[level][from]);
        }
        memset(mem, 0xff, sizeof(mem));
        int ans = calc(ep - 1, 0, 0);
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
