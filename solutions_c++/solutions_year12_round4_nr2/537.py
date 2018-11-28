#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <cstring>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <complex>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <cassert>
#include <queue>
#include <iterator>

typedef long long LL;
typedef long double LD;

using namespace std;

LD dist(LL x1, LL y1, LL x2, LL y2) {
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main() {
#ifndef LOCAL
//  freopen(".in", "r", stdin);
//  freopen(".out", "w", stdout);
#endif

    int nTests;
    cin >> nTests;
    for (int test = 1; test <= nTests; test++) {
        int n, w, l;
        cin >> n >> w >> l;

        vector<pair<int, int> > r(n), ans(n);
        for (int i = 0; i < n; i++) {
            cin >> r[i].first;
            r[i].second = i;
        }
        sort(r.begin(), r.end(), greater< pair<int, int> >());

        vector<bool> done(n);
        int s = -1;
        while (true) {
            int R = -1;
            for (int i = 0; i < n; i++)
                if (!done[i]) {
                    R = r[i].first;
                    break;
                }
            if (R == -1)
                break;

            if (s >= 0)
                s += R;
            else
                s = 0;
            if (s > w)
                assert(0);

            int t = -R;
            for (int i = 0; i < n; i++)
                if (!done[i] && t + r[i].first <= l) {
                    done[i] = true;
                    ans[r[i].second] = make_pair(s, t + r[i].first);

                    t += 2 * r[i].first;
                }

            s += R;
        }

        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++)
                if (dist(ans[r[i].second].first, ans[r[i].second].second, ans[r[j].second].first, ans[r[j].second].second) < 
                            r[i].first + r[j].first - 1e10)
                    assert(0);

        cout << "Case #" << test << ": ";
        for (int i = 0; i < n; i++) {
            if (i)
                cout << ' ';
            cout << ans[i].first << ' ' << ans[i].second;
            assert(0 <= ans[i].first && ans[i].first <= w && 0 <= ans[i].second && ans[i].second <= l);
        }
        cout << '\n';
    }

    return 0;
}


