/*
 * Sat May  8 14:09:33 KST 2010
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
long long times, lim, n, g[1024];
long long earn[1024], start[1024];
bool v[1024];

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%lld%lld%lld", &times, &lim, &n);
        for (int i = 0; i < n; ++i) {
            scanf("%lld", &g[i]);
        }

        memset(v, false, sizeof(v));
        long long cur = 0, now = 0;
        for (now = 0; now < times && !v[cur]; ++now) {
            start[now] = cur;
            v[cur] = true;
            earn[now] = 0;
            long long left = lim;
            for (int k = 0; k < n && left >= g[cur]; ++k) {
                left -= g[cur];
                earn[now] += g[cur];
                cur = (cur + 1) % n;
            }
        }

        if (now >= times) {
            long long ans = 0;
            for (int i = 0; i < times; ++i) {
                ans += earn[i];
            }
            printf("Case #%d: %lld\n", cas++, ans);
            continue;
        }

        long long first = 0;
        for (int i = 0; i < now; ++i) if (start[i] == cur) {
            first = i;
            break;
        }

        long long loop = now - first, ans = 0, loopearn = 0;
        for (int i = 0; i < first; ++i) {
            ans += earn[i];
        }
        for (int i = first; i < now; ++i) {
            loopearn += earn[i];
        }
        long long mod = (times - first) % loop, cnt = (times - first) / loop;
        for (int k = 0; k < mod; ++k) {
            ans += earn[first + k];
        }
        ans += loopearn * cnt;
        printf("Case #%d: %lld\n", cas++, ans);
    }
    return 0;
}
