/*
 * Sat Jun  5 22:14:33 CST 2010
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
const int dir[2][2] = { { -1, 0 }, { 0, -1 } };
const int inf = 1000000000;
const long long infll = 1000000000000000000LL;
const double eps = 1e-10;
const double pi = acos(-1.0);

int cases, cas = 1;
int n;

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d", &n);
        set<pair<int, int> > s[2]; int now = 0;
        for (int i = 0; i < n; ++i) {
            int x1, y1, x2, y2; scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            for (int x = x1; x <= x2; ++x) for (int y = y1; y <= y2; ++y) {
                s[now].insert(make_pair(x, y));
            }
        }
        int ans = 0;
        while (!s[now].empty()) {
cerr << s[now].size() << endl;
            ans++;
            int next = (now ^ 1); s[next].clear();
            for (set<pair<int, int> >::const_iterator it  = s[now].begin(); it != s[now].end(); ++it) {
                bool ok = false;
                for (int d = 0; d < 2 && !ok; ++d) {
                    int x = it->first + dir[d][0], y = it->second + dir[d][1];
                    if (s[now].find(make_pair(x, y)) != s[now].end()) {
                        ok = true;
                    }
                }
                if (ok) {
                    s[next].insert(make_pair(it->first, it->second));
                }
            }
            for (set<pair<int, int> >::const_iterator it  = s[now].begin(); it != s[now].end(); ++it) {
                int x = it->first - 1, y = it->second + 1;
                if (s[now].find(make_pair(x, y)) != s[now].end()) {
                    s[next].insert(make_pair(it->first, it->second + 1));
                }
                x = it->first + 1; y = it->second - 1;
                if (s[now].find(make_pair(x, y)) != s[now].end()) {
                    s[next].insert(make_pair(it->first + 1, it->second));
                }
            }
            now = next;
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
