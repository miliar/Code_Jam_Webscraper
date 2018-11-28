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
        int n,w,l;
        printf("Case #%d: ", test);
        cin >> n >> w >> l;
        vii r(n);
        for (int i = 0; i < n; ++i) {
            cin >> r[i].first;
            r[i].second = i;
        }
        vector<pii> x(n);
        sort(r.begin(), r.end());
//        cerr << r.size() << endl;
        vi pos(1, 0), h(1, r.back().first), wid(1, r.back().first);
        int it = (int)r.size() - 2;
        map<int, int> q;
        q[h[0]] = 0;
        for (; it >= 0; --it) {
            if (pos.back() + wid.back() + 2 * r[it].first > w)
                break;
//            cerr << pos.back() << " " << wid.back() << endl;
            pos.push_back(pos.back() + wid.back() + r[it].first);
            wid.push_back(r[it].first);
            h.push_back(r[it].first);
            q[h.back()] = (int)h.size() - 1;
            x[r[it].second].first = pos.back();
            x[r[it].second].second = 0;
        }
        while (it >= 0) {
            int i = (q.begin())->second;
            q.erase(q.begin());
            int cur = pos[i];
            int hnew = h[i] + 2 * r[it].first;
            for (; it >= 0; --it) {
                if (cur + r[it].first > pos[i] + wid[i] || cur > w) {
//                    if (i != pos.size() - 1 || cur + r[it].first > pos[i] + wid[i])
                    break;
                }
                x[r[it].second].first = cur;
                x[r[it].second].second = h[i] + r[it].first;
                cur += 2 * r[it].first;
            }
            h[i] = hnew;
            q.insert(pii(h[i], i));
        }
        for (int i = 0; i < n; ++i)
            printf("%d %d ", x[i].first, x[i].second);
        printf("\n");
    }
    return 0;
}
