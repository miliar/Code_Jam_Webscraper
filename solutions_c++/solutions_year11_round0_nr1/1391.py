#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

#define mp make_pair
#define pb push_back
#define ll long long
#define mp make_pair


const int maxn = 200000;
int a[maxn];
char who[maxn];
vector <int> x, y;


int main() {
    int t, n, now, sum, minf, w1, w2, res, last1, last2, inc;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        w1 = w2 = 1, last1 = 0, last2 = 0;
        res = 0;
        x.clear(), y.clear();
        for (int j = 0; j < n; ++j) {
            cin >> who[j] >> a[j]; 
            if (who[j] == 'O') x.pb(a[j]); else y.pb(a[j]);
        }
        for (int j = 0; j < n; ++j) {
            if (who[j] == 'O') {
                inc = abs(w1 - a[j]) + 1;
                if (last2 != (int) y.size()) 
                    w2 += min(inc, abs(w2 - y[last2])) * (w2 < y[last2] ? 1 : -1);
                ++last1;
                w1 = a[j];
                res += inc;
            } else {
                inc = abs(w2 - a[j]) + 1;
                if (last1 != (int) x.size()) 
                   w1 += min(inc, abs(w1 - x[last1])) * (w1 < x[last1] ? 1 : -1);
                ++last2;
                w2 = a[j];
                res += inc;
            }
        }
        cout << "Case #" << i << ": " << res << "\n";
    }
}
