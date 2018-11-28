#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<char, char> pcc;

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        int c, d, n;
        map<pcc, char> comp;
        vector<vector<char> > bad(256);
        string s;
        cin >> c;
        for (int i = 0; i < c; ++i) {
            cin >> s;
            if (s[0] > s[1])
                swap(s[0], s[1]);
            comp[pcc(s[0], s[1])] = s[2];
        }
        cin >> d;
        for (int i = 0; i < d; ++i) {
            cin >> s;
            bad[s[0]].push_back(s[1]);
            bad[s[1]].push_back(s[0]);
        }
        cin >> n >> s;
        vector<char> cur;
        for (int i = 0; i < s.size(); ++i) {
            bool add = true;
            if (cur.size()) {
                char x = s[i], y = cur.back();
                if (x > y)
                    swap(x, y);
                map<pcc, char>::iterator it = comp.find(pcc(x, y));
                if (it != comp.end()) {
                    cur.pop_back();
                    cur.push_back(it->second);
                    add = 0;
                }
            }
            if (add)
                cur.push_back(s[i]);
            bool ok = true;
            for (int it = 0; it < bad[cur.back()].size(); ++it) for (int it1 = 0; it1 + 1 < cur.size(); ++it1) {
                if (cur[it1] == bad[cur.back()][it]) {
                    ok = false;
                    break;
                }
            }
            if (!ok) {
                cur.resize(0);
            }
        }
        cout << "Case #" << test << ": [";
        for (int i = 0; i + 1 < cur.size(); ++i)
            cout << cur[i] << ", ";
        if (!cur.empty())
            cout << cur.back();
        cout << "]\n";
    }
    return 0;
}
