/*
 * Sun Aug 10 00:50:45 KST 2008
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
const int inf = 1000000000;
const long long infll = 1000000000000000000LL;
const double eps = 1e-10;
const double pi = acos(-1.0);

const int dir[4][2] = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
int cases, cas = 1;
int n, repeat;
string op;
vector<pair<double, double> > ps;

bool check(double x, double y, vector<pair<double, double> >& ps) {
    int n = ps.size(), cnt = 0;
    double x1, y1, x2, y2;
    for (int i = 1; i < n; ++i) {
        x1 = ps[i - 1].first; y1 = ps[i - 1].second; x2 = ps[i].first; y2 = ps[i].second;
        if (fabs(x1 - x2) > eps) continue;
        if (y1 > y2) swap(y1, y2);
        if (x1 > x && y1 < y && y2 > y) {
            cnt++;
        }
    }
    x1 = ps[0].first; y1 = ps[0].second; x2 = ps[n - 1].first; y2 = ps[n - 1].second;
    if (fabs(x1 - x2) < eps) {
        if (y1 > y2) swap(y1, y2);
        if (x1 > x && y1 < y && y2 > y) {
            cnt++;
        }
    }
    if (cnt % 2 == 1) return false;

    bool up = false, down = false, left = false, right = false;
    for (int i = 1; i < n; ++i) {
        x1 = ps[i - 1].first; y1 = ps[i - 1].second; x2 = ps[i].first; y2 = ps[i].second;
        if (fabs(x1 - x2) < eps) {
            if (y1 > y2) swap(y1, y2);
            if (y1 < y && y2 > y && x1 < x) {
                left = true;
            }
            if (y1 < y && y2 > y && x1 > x) {
                right = true;
            }
        } else {
            if (x1 > x2) swap(x1, x2);
            if (x1 < x && x2 > x && y1 < y) {
                up = true;
            }
            if (x1 < x && x2 > x && y1 > y) {
                down = true;
            }
        }
        if ((up && down) || (left && right)) {
            return true;
        }
    }
    x1 = ps[0].first; y1 = ps[0].second; x2 = ps[n - 1].first; y2 = ps[n - 1].second;
    if (fabs(x1 - x2) < eps) {
        if (y1 > y2) swap(y1, y2);
        if (y1 < y && y2 > y && x1 < x) {
            left = true;
        }
        if (y1 < y && y2 > y && x1 > x) {
            right = true;
        }
    } else {
        if (x1 > x2) swap(x1, x2);
        if (x1 < x && x2 > x && y1 < y) {
            up = true;
        }
        if (x1 < x && x2 > x && y1 > y) {
            down = true;
        }
    }
    if ((up && down) || (left && right)) {
        return true;
    }

    return false;
}

int main() {
    for (scanf("%d", &cases); cases--; ) {
        int x = 0, y = 0, d = 0;
        scanf("%d", &n);
        ps.clear(); ps.push_back(make_pair(0, 0));
        for (int k = 0; k < n; ++k) {
            string tmp;
            cin >> tmp >> repeat;
            op = "";
            for (int i = 0; i < repeat; ++i) {
                op += tmp;
            }
            for (unsigned i = 0; i < op.size(); ) {
                int len = 0, pos = i;
                while (pos < (int) op.size() && op[pos] == 'F') {
                    len++; pos++;
                }
                i = pos + 1;
                if (len == 0) {
                    if (pos < (int) op.size()) {
                        if (op[pos] == 'L') {
                            d = (d + 3) % 4;
                        } else if (op[pos] == 'R') {
                            d = (d + 1) % 4;
                        }
                    }
                    continue;
                }
                x += dir[d][0] * len; y += dir[d][1] * len;
                ps.push_back(make_pair(x, y));
                if (pos < (int) op.size()) {
                    if (op[pos] == 'L') {
                        d = (d + 3) % 4;
                    } else if (op[pos] == 'R') {
                        d = (d + 1) % 4;
                    }
                }
            }
        }
        int ans = 0;
        for (int i = -101; i <= 101; ++i) for (int j = -101; j <= 101; ++j) {
            double x = i + 0.5, y = j + 0.5;
            if (check(x, y, ps)) {
                ans++;
            }
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
