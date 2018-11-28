#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": ";
        int n,s,p;
        cin >> n >> s >> p;
        vi v(n);
        for (int i = 0; i < n; ++i)
            cin >> v[i];
        int cnt = 0, res = 0;
        sort(v.begin(), v.end());
        for (int i = 0; i < n; ++i) {
            if ((v[i] + 2) / 3 >= p) {
                ++res;
            } else if (cnt < s) {
                if (min((v[i] + 4) / 3, v[i]) >= p) {
                    ++res;
                    ++cnt;
                }
            }
        }
        cout << res << endl;
    }
    return 0;
}
