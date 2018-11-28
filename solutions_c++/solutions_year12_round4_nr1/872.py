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

void solve() {
    int64 n;
    cin >> n;
    vector<int64> x(n), y(n);
    for (int64 i = 0; i < n; ++i)
        cin >> x[i] >> y[i];
    int64 D;
    cin >> D;
    x.pb(D);
    y.pb(0);
    vector<int64> a(n + 1, -1);
    a[0] = x[0];
    for (int64 i = 0; i < n; ++i) {
        a[i] = min(y[i], a[i]);
        if (a[i] == -1)
           continue;
        for (int64 j = i + 1; j <= n; ++j)
            if (x[j] - x[i] <= a[i])
                a[j] = max(a[j], x[j] - x[i]); 
    }
    cout << (a[n] != -1 ? "YES" : "NO") << endl;
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
