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
/*template <typename T> string ToString(T begin, T end) { 
    string res = "{";
    for (T it = begin; it != end; ++it)
        res += (it == begin ? "" : ", ") + ToString(*it);
    return res + "}";
}
*/

void Solve() {
    int n;
    vector<LL> d;
    vector<LL> l;
    LL D;
    cin >> n;
    d.resize(n);
    l.resize(n);
    for (int i = 0; i < n; ++i) 
        cin >> d[i] >> l[i];
    cin >> D;

    vector<LL> ans(n, -1);
    for (int i = n-1; i >= 0; --i) {
        if (min(l[i], d[i]) >= D - d[i])
            ans[i] = D - d[i];
        for (int j = i+1; j < n; ++j)
            if (ans[j] != -1 && d[j]-d[i] <= min(l[i], d[i]) && ans[j] <= d[j]-d[i] && (ans[i] == -1 || ans[i] > d[j]-d[i])) {
                ans[i] = d[j]-d[i];
            }
    }
    if (ans[0] != -1)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
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
