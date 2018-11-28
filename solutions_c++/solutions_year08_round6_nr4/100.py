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
int n, m;
vector<pair<int, int> > ff, ss;

bool check(const vector<pair<int, int> >& a, const vector<pair<int, int> >& b) {
    if (a.size() != b.size()) {
        return false;
    }
    int n = a.size();
    for (int i = 0; i < n; ++i) if (a[i] != b[i]) {
        return false;
    }
    return true;
}

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d", &n);
        ff.clear();
        for (int i = 0; i < n - 1; ++i) {
            int a, b;
            scanf("%d%d", &a, &b);
            ff.push_back(make_pair(a - 1, b - 1));
            ff.push_back(make_pair(b - 1, a - 1));
        }
        sort(ff.begin(), ff.end());
        scanf("%d", &m);
        ss.clear();
        for (int i = 0; i < m - 1; ++i) {
            int a, b;
            scanf("%d%d", &a, &b);
            ss.push_back(make_pair(a - 1, b - 1));
            ss.push_back(make_pair(b - 1, a - 1));
        }
        sort(ss.begin(), ss.end());
        int num[16];
        for (int i = 0; i < n; ++i) {
            num[i] = i;
        }
        bool ok = false;
        do {
            vector<pair<int, int> > tmp;
            for (unsigned i = 0; i < ff.size(); ++i) {
                int x = num[ff[i].first], y = num[ff[i].second];
                if (x < m && y < m) {
                    tmp.push_back(make_pair(x, y));
                }
            }
            sort(tmp.begin(), tmp.end());
            if (check(tmp, ss)) {
                ok = true;
                break;
            }
        } while (next_permutation(num, num + n));
        if (ok) {
            printf("Case #%d: YES\n", cas++);
        } else {
            printf("Case #%d: NO\n", cas++);
        }
    }
    return 0;
}
