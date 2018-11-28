#include <iostream> 
#include <vector> 
#include <string> 
#include <math.h> 
#include <algorithm>
#include <map>
#include <set> 

#define sz(x) ((int)x.size()) 
#define all(x) (x).begin(), (x).end() 
#define pb(x) push_back(x) 
#define mp(x, y) make_pair(x, y) 

typedef long long int64; 

using namespace std;

void solve() {
    int64 x, s, r, n;
    long double t;
    cin >> x >> s >> r >> t >> n;
    long double T = t;
    multiset<pair<int64, int64> > a;
    for (int64 i = 0; i < n; ++i) {
        int64 b, e, w;
        cin >> b >> e >> w;
        a.insert(mp(w, e - b));
        x -= (e - b);
    }
    a.insert(mp(0, x));
    long double ans = 0;
    while (true) {
        if (t < 0)
            break;
        if (a.empty())
            break;
        int64 w = (*a.begin()).first;
        int64 len = (*a.begin()).second;
        if ((long double)len < t * (r + w)) {
             t -= (long double)len / (r + w);
        } else {
            ans += ((long double)len - t * (r + w)) / (s + w); 
            t = 0;
        }
        a.erase(a.begin());
    }
    ans += (T - t);
    for (multiset<pair<int64, int64> >::iterator it = a.begin(); it != a.end(); ++it) {
        int64 w = (*it).first;
        int64 len = (*it).second;
        ans += ((long double)len / (s + w));
    }
    printf("%.10lf\n", (double)ans);
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int test = 0; test < t; ++test) {
        cout << "Case #" << test + 1 << ": ";
        solve();
    }
    
    int x;
    cin >> x;
    return 0;
}
