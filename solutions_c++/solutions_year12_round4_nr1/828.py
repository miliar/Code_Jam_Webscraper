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
        printf("Case #%d: ", test);
        int n;
        cin >> n;
        vi d(n), l(n), ma(n);
        for (int i = 0; i < n; ++i)
            cin >> d[i] >> l[i];
        int it = 1, cur = d[0], len = d[0], D, yes = 0;
        ma[0] = d[0];
        cin >> D;
        for (int i = 0; i < d.size(); ++i) {
//            cout << ma[i] << endl;
            if (d[i] + ma[i] >= D) {
                printf("YES\n");
                yes = 1;
                break;
            }
            while (it < d.size() && d[it] <= d[i] + ma[i]) {
                ma[it] = min(l[it], d[it] - d[i]);
                ++it;
            }
        }
        if (!yes) {
            printf("NO\n");
        }
/*        vii q;
        for (int i = 0; i < n; ++i) {
            q.push_back(pii(d[i] - l[i], d[i]));
        }
        sort(q.begin(), q.end());
        map<int, int> was;
        while (1) {
//            cout << cur << " " << len << endl;
            if (cur + len >= D) {
                printf("YES\n");
                break;
            }
            int best = 0, ma = 0;
            while (it < d.size() && d[it] <= cur + len) {
                was[min(d[it] - cur, l[it])] = it;
                if (d[it] + min(d[it] - cur, l[it]) > ma) {
                    ma = d[it] + min(d[it] - cur, l[it]);
                    best = it;
                }
                ++it;
            }
//            int newcur = -*(was.lower_bound(-cur-len));
//            len = newcur - len;
            if (ma == 0) {
                printf("NO\n");
                break;
            } else {
                cur = d[best];
                len = ma - d[best];
            }
        }*/
    }
    return 0;
}
