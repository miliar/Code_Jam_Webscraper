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

int n, D;
vector <pair <int, int> > p;

string solve() {
    sort(p.begin(), p.end());
    vector <vector <char> > was(n, vector <char> (n));
    queue <pair <int, int> > q;
    q.push(make_pair(0, 1));
    was[0][1] = true;
    while (!q.empty()) {
        pair <int, int> pos = q.front(); q.pop();
        int len = min(p[pos.second].first - p[pos.first].first, p[pos.second].second);
        for (int j = pos.second + 1; j < n; ++j) {
            if (p[pos.second].first + len < p[j].first) continue;
            LL dist = p[j].first - p[pos.second].first;
            if (LL(len) * len > LL(p[pos.second].second) * p[pos.second].second + LL(dist) * dist) continue;
            pair <int, int> new_pos = make_pair(pos.second, j);
            if (!was[new_pos.first][new_pos.second]) {
                was[new_pos.first][new_pos.second] = true;
                q.push(new_pos);
            }
        }
    }
    bool ans = false;
    for (int i = 0; i < n; ++i)
        ans = ans || was[i][n - 1];
    return ans ? "YES" : "NO";
}

int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cin >> n;
        p.resize(n + 1);
        p[0] = make_pair(0, 0);
        for (int i = 1; i <= n; ++i)
            cin >> p[i].first >> p[i].second;
        cin >> D;
        p.push_back(make_pair(D, 0));
        n += 2;
        cout << "Case #" << tt << ": " << solve() << '\n';
    }

    return 0;
}
