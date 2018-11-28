#include <iostream>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

int64 n, w, l;
vector<int64> x, y;
double pi = 4 * atan(1.0);

void do_it(int64 add_x, int64 add_y, vector<pair<int64, int64> >& r) {
    if (r.empty())
        return;
    x[r[0].second] = add_x + r[0].first;
    y[r[0].second] = add_y + r[0].first;
    if (add_x == 0)
        x[r[0].second] = add_x;
    if (add_y == 0)
        y[r[0].second] = add_y;
    int64 sum = 0;
    int64 pos = 1;
    vector<bool> ok(n, false);
    ok[0] = true;
    vector<pair<int64, int64> > r1;
    int64 val_x = add_x;
    int64 val_y = add_y + 2 * r[0].first;
    if (add_y == 0)
        val_y = add_y + r[0].first;
    for (int64 i = sz(r) - 1; i >= 0; --i) {
        if (ok[i])
            continue;
        if (5 * pi * (sum + r[i].first * r[i].first) >= (w - val_x) * (l - val_y))
            continue;
        ok[i] = true;
        sum += r[i].first;
        r1.pb(r[i]);
    }
    do_it(val_x, val_y, r1);
    
    sum = 0;
    vector<pair<int64, int64> > r2;
    val_x = add_x + 2 * r[0].first;
    val_y = add_y;
    if (add_x == 0)
        val_x = add_x + r[0].first;
    
    for (int64 i = sz(r) - 1; i >= 0; --i) {
        if (ok[i])
            continue;
        if (5 * pi * (sum + r[i].first * r[i].first) >= (w - val_x) * (l - val_y))
            continue;
        sum += r[i].first;
        ok[i] = true;
        r2.pb(r[i]);
    }
    do_it(val_x, val_y, r2);
    
    val_x = add_x + 2 * r[0].first;
    val_y = add_y + 2 * r[0].first;
    if (add_x == 0)
        val_x = add_x + r[0].first;
    if (add_y == 0)
        val_y = add_y + r[0].first;
    
    vector<pair<int64, int64> > r3;
    for (int64 i = 0; i < sz(r); ++i) {
        if (ok[i])
            continue;
        r3.pb(r[i]);
    }
    do_it(val_x, val_y, r3);
}

void solve() {
    x.clear();
    y.clear();
    cin >> n >> w >> l;
    x.assign(n, -1);
    y.resize(n, -1);
    vector<pair<int64, int64> > r(n);
    for (int64 i = 0; i < n; ++i) {
        int64 val;
        cin >> val;
        r[i] = mp(val, i);
     }
    sort(all(r));
    reverse(all(r));
    do_it(0, 0, r);
    for (int i = 0; i < n; ++i) {
         if (x[i] > w || y[i] > l)
              cout << "aaaaa" << endl;
         cout << x[i] << " " << y[i] << " ";
    }
    
    cout << endl;
          
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int t;
    cin >> t;
    for (int tests = 0; tests < t; ++tests) {
        cout << "Case #" << tests + 1 << ": ";
        solve();
    }   
    return 0;
}
