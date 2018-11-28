#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <utility>
#include <cstring>


using namespace std;
typedef long long LL;
template <typename T> inline T Abs(const T& x) { return x < 0 ? -x : x; }
template <typename T> inline T Sqr(const T& x) { return x * x; }
template <typename T> inline string ToString(const T& x) { ostringstream out; out << x; return out.str(); }
template <typename T> string ToString(T begin, T end) { 
    string res = "{";
    for (T it = begin; it != end; ++it)
        res += (it == begin ? "" : ", ") + ToString(*it);
    return res + "}";
}

void Solve() {
    LL W, L;
    int n;
    cin >> n >> W >> L;
    vector<pair<LL, int> > r(n);
    vector<double> x(n), y(n);
    for (int i = 0; i < n; ++i) {
        cin >> r[i].first;
        r[i].second = i;
    }
    sort(r.rbegin(), r.rend());
    vector< pair<LL, LL> > a;
    int cur = 0;
    double cy = 0;
    while (cur < n) {
        double ny = cy + r[cur].first * 2;
        LL sz = r[cur].first;
        int last = -r[cur].first;
        while (cur < n && last + r[cur].first <= W) {
            y[r[cur].second] = cy;
            x[r[cur].second] = last + r[cur].first;
            last = last + 2*r[cur].first;
            ++cur;
        }
        cy = ny;
    }
    for (int i = 0; i < n; ++i)
        printf("%.1lf %.1lf ", x[i], y[i]);
    cout << endl;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int testsNum;
    cin >> testsNum;

    for (int t = 1; t <= testsNum; ++t) {
        cout << "Case #" << t << ": ";
        Solve();
    }


    return 0;
}
