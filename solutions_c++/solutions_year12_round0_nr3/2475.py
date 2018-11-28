#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <memory>
#include <cassert>
using namespace std;

#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); (i)++)
#define REP(i, n) for (int (i) = 0; (i) < n; (i)++)
#define SIZE(a) (int)(a).size()
#define PB push_back
#define ALL(a) (a).begin(), (a).end()
#define FORD(i, a, b) for(int (i) = (a); (i) >= (b); (i)--)
#define MP make_pair
#define DBG(x) cout << #x << " = " << x << endl

#define MX 2000000

string i2s(int x) {
    stringstream ss;
    ss << x;
    string s;
    ss >> s;
    return s;
}

int s2i(const string& s) {
    stringstream ss;
    ss << s;
    int i;
    ss >> i;
    return i;
}

vector<int> a[MX + 1];
int seen[MX + 1];

bool better(const string& s, int off_a, int off_b) {
    int n = SIZE(s);
    REP(i, n) {
        char a = s[(i + off_a) % n];
        char b = s[(i + off_b) % n];
        if (a < b)
            return true;
        if (a > b)
            return false;
    }
    return false; // 111
}

int main() {
    memset(seen, 0, MX + 1);
    vector<string> reprs(MX + 1);
    FOR(i, 1, MX) {
        reprs[i] = i2s(i);
        string s = reprs[i];
        int best_offset = 0;
        FOR(j, 1, SIZE(s) - 1) {
            if (s[j] == '0') {
                continue;
            }
            if (better(s, j, best_offset)) {
                best_offset = j;
            }
        }
        string canon = s.substr(best_offset) + s.substr(0, best_offset);
        int tgt = s2i(canon);
        if (SIZE(reprs[tgt]) == SIZE(reprs[i])) {
            a[tgt].push_back(i);
        }
    }
    vector<int> inds;
    FOR(i, 1, MX) {
        if (SIZE(a[i]) >= 2) {
            inds.push_back(i);
            sort(ALL(a[i]));
            assert(a[i][0] == i);
        }
    }

    int T;
    cin >> T;
    REP(zzz, T) {
        int A, B;
        cin >> A >> B;
        long long res = 0;
        REP(i, SIZE(inds)) {
            vector<int> &v = a[inds[i]];
            int mn = v[0];
            int mx = v[SIZE(v) - 1];
            if (mn >= A && mx <= B) {
                res += SIZE(v) * (SIZE(v) - 1) / 2;
            } else if (A > mx || B < mn) {
                continue;
            } else {
                int cnt = 0;
                REP(j, SIZE(v)) if (v[j] >= A && v[j] <= B) ++cnt;
                res += cnt * (cnt - 1) / 2;
            }
        }
        cout << "Case #" << zzz + 1 << ": " << res << endl;
    }
}
