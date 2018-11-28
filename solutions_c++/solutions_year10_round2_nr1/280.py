#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>

#define FI first
#define SE second
#define PB push_back

using namespace std;
typedef long long LL;
typedef pair<int, int> PI;

LL solve() {
    set<string> ex;
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        ex.insert(s);
    }
    int ret = 0;
    for (int i = 0; i < m; i++) {
        string s;
        cin >> s;
        s += '/';
        int r = s.size();
        for (int j = 1; j < r; j++) {
            if (s[j] == '/') {
                string ss = s.substr(0, j);
                if (ex.find(ss) == ex.end()) {
                    ex.insert(ss);
                    ret++;
                }
                //cout << ss << " " << ret << endl;
            }
        }
    }
    return ret;
}


int main() {
    ios_base::sync_with_stdio(0);
    int te;
    cin >> te;
    for (int l = 1; l <= te; l++) {
        LL ret = solve();
        cout << "Case #" << l << ": " << ret << endl;
    }
}

