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
        int a,b;
        cin >> a >> b;
        int mul = 1, n = 1;
        while (mul * 10 <= a) {
            mul *= 10;
            ++n;
        }
//        cerr << mul << " " << n << endl;
        int res = 0;
        for (int c = a; c <= b; ++c) {
            int m = c;
            for (int t = 0; t + 1 < n; ++t) {
                int d = m % 10;
                m = m / 10 + d * mul;
                if (m == c)
                    break;
                if (a <= m && m <= b)
                    ++res;
            }
        }
        cout << "Case #" << test << ": ";
        cout << res / 2 << endl;
    }
    return 0;
}
