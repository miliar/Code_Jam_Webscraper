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

int main() {
#ifndef LOCAL
//  freopen(".in", "r", stdin);
//  freopen(".out", "w", stdout);
#endif

    int nTests;
    cin >> nTests;
    for (int test = 1; test <= nTests; test++) {
        int n;
        cin >> n;

        vector<int> next(n);
        for (int i = 0; i < n - 1; i++) {
            cin >> next[i];
            next[i]--;
        }

        vector<int> y(n, (int)1e9);

        vector< pair<int, int> > ps(n - 1);
        for (int i = 0; i < n - 1; i++)
            ps[i] = make_pair(-next[i], i);
        sort(ps.begin(), ps.end());

        bool bad = false;

        for (int it = 0; it < n - 1; it++) {
            int i = ps[it].second;
            for (int wh = 0; wh < it; wh++) {
                int j = ps[wh].second;
                
                if (j > i && j < next[i]) 
                    bad = true;

                LD k = (y[next[j]] - y[j]) / (LD)(next[j] - j);
                y[i] = min(y[i], (int)(y[j] + k * (i - j)) - 1);
            }
        }

#ifdef LOCAL
        bool ok = true;
        for (int i = 0; i < n - 1; i++) {
            LD maxK = -1e9;
            int arg = -1;
            for (int j = i + 1; j < n; j++) {
                LD k = (y[j] - y[i]) / (LD)(j - i);
                if (k > maxK + 1e-10) {
                    maxK = k;
                    arg = j;
                }
            }
            // cerr << arg << ' ';
            ok &= arg == next[i];
        }
        assert(bad == !ok);
#endif

        cout << "Case #" << test << ": ";
        if (bad) 
            cout << "Impossible";
        else {
            for (int i = 0; i < n; i++) {
                if (i)
                    cout << ' ';
                cout << y[i];
                assert(y[i] >= 1);
            }
        }
        cout << '\n';
    }

    return 0;
}


