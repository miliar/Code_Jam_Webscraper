// brute

#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <iostream>
#include <cassert>
#include <utility>
#include <vector>
#include <set>

using namespace std;

const int nmax = 101;

struct train {
    int s, f, w;
    bool operator < (const train & b) const {
        return s < b.s;
    }
};

int n, m;
int t;
pair < int, int > ans;
train a[nmax*2];
multiset < pair < int, int > > q;

void init() {
    scanf("%d", &t);
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i) {
        int x, y;
        train temp;
        scanf("%d:%d", &x, &y);
        temp.s = x*60 + y;
        scanf("%d:%d", &x, &y);
        temp.f = x*60 + y;
        temp.w = 1;
        a[i] = temp;
    }
    for (int i = 0; i < m; ++i) {
        int x, y;
        train temp;
        scanf("%d:%d", &x, &y);
        temp.s = x*60 + y;
        scanf("%d:%d", &x, &y);
        temp.f = x*60 + y;
        temp.w = 2;
        a[i + n] = temp;
    }

    sort(a, a + n+ m);
}

void solve() {
    int ansx = 0, ansy = 0;
    int x = 0, y = 0;
    q.clear();
    for (int i = 0; i < n + m; ++i) {
        while (!q.empty() && q.begin()->first <= a[i].s) {
            if (q.begin()->second == 1) y--; else x--;
            q.erase(q.begin());
        }
                
        if (a[i].w == 1) {
            x++;
            ansx = max(ansx, x);
            q.insert(make_pair(a[i].f + t, 1));
        } else {
            y++;
            ansy = max(ansy, y);
            q.insert(make_pair(a[i].f + t, 2));
        }
    }
    ans = make_pair(ansx, ansy);
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testcnt;
    scanf("%d", &testcnt);
    for (int testid = 0; testid < testcnt; ++testid) {
        init();
        solve();
        printf("Case #%d: %d %d\n", testid + 1, ans.first, ans.second);
    }
    
    return 0;
}
