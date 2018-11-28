/*
 * Sun Aug 10 00:22:40 KST 2008
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

const int lim = (1 << 10);
int cases, cas = 1;
int n, m;
char board[16][16];
int gooddesk[16];
int mem[2][1 << 10];
int bitcount[1 << 10];

bool leftright(int mask) {
    for (int i = 1; i < m; ++i) if ((mask & (1 << i)) && (mask & (1 << (i - 1)))) {
        return false;
    }
    return true;
}

int main() {
    for (int i = 0; i < lim; ++i) {
        bitcount[i] = 0;
        for (int j = 0; j < 10; ++j) if (i & (1 << j)) {
            bitcount[i]++;
        }
    }
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            scanf("%s", board[i]);
            gooddesk[i] = 0;
            for (int j = 0; j < m; ++j) if (board[i][j] == '.') {
                gooddesk[i] |= (1 << j);
            }
        }
        int now = 0, next;
        for (int mask = 0; mask < (1 << m); ++mask) {
            if ((gooddesk[0] & mask) == mask && leftright(mask)) {
                mem[now][mask] = bitcount[mask];
            } else {
                mem[now][mask] = 0;
            }
        }
        for (int row = 1; row < n; ++row) {
            next = (now ^ 1);
            for (int i = 0; i < (1 << m); ++i) {
                mem[next][i] = 0;
            }
            for (int mask = 0; mask < (1 << m); ++mask) if ((gooddesk[row] & mask) == mask && leftright(mask)) {
                for (int pre = 0; pre < (1 << m); ++pre) if ((gooddesk[row - 1] & pre) == pre && leftright(pre)) {
                    int mm = (1 << m) - 1;
                    for (int j = 0; j < m; ++j) if (pre & (1 << j)) {
                        if (j - 1 >= 0) {
                            mm &= (~(1 << (j - 1)));
                        }
                        if (j + 1 < m) {
                            mm &= (~(1 << (j + 1)));
                        }
                    }
                    if ((mm & mask) == mask) {
                        mem[next][mask] = max(mem[next][mask], mem[now][pre] + bitcount[mask]);
                    }
                }
            }
            now = next;
        }
        int ans = 0;
        for (int mask = 0; mask < (1 << m); ++mask) if ((gooddesk[n - 1] & mask) == mask && leftright(mask)) {
            ans = max(ans, mem[now][mask]);
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
