#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <functional>
#include <iterator>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <iomanip>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef long double LD;

int n;
vector <int> v;

vector <int> h;

int sum(int n, int delta) {
    return n * (n + 1) / 2 + delta * n;
}

bool dfs(int begin, int end, int delta = 0) {
    int j = begin;
    if (begin >= end) return true;
    h[begin] = h[end] - sum(end - begin, delta);
    while (j != end) {
        if (j > end)
            return false;
        int jj = v[j];
        if (jj != end)
            h[jj] = h[end] - sum(end - jj, delta);
        bool b = dfs(j + 1, jj, h[jj] - h[j]);
        if (!b) return false;
        j = v[j];
    }
    return true;
}

bool solve() {
    for (int i = 0; i + 1 < n; ++i)
        if (v[i] <= i) return false;

    h.resize(n);
    h[n - 1] = 1000000000;

    return dfs(0, n - 1);
}

int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cin >> n;
        v.resize(n);
        for (int i = 0; i + 1 < n; ++i) {
            cin >> v[i];
            --v[i];
        }
        v.push_back(-1);
        cout << "Case #" << tt << ": ";
        bool ans = solve();
        if (!ans)
            cout << "Impossible";
        else
            for (int i = 0; i < n; ++i)
                cout << h[i] << ' ';
        cout << '\n';
    }

    return 0;
}
