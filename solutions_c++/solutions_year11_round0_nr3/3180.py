#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <functional>
using namespace std;
#define pb push_back 
#define mp make_pair
#define sz(v) ((int)(v).size()) 
#define rep(i,n) for(int i=0;i<(n);++i) 
#define all(a) (a).begin(),(a).end()
#define foreach(i, a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define inf (1LL << 29)
typedef long long ll;
typedef vector<int> vi;


string solve() {
    int n; cin >> n;
    vector<int> c(n);
    for (int i = 0; i < n; ++i) {
        cin >> c[i];
    }
    ll ans = -1;
    for (int i = 0; i < (1 << sz(c)); ++i) {
        ll val1 = 0, val2 = 0;
        ll sum1 = 0, sum2 = 0;
        bool ok1 = false, ok2 = false;
        for (int j = 0; j < sz(c); ++j) {
            if (i & (1 << j)) {
                val1 ^= c[j];
                sum1 += c[j];
                ok1 = true;
            } else {
                val2 ^= c[j];
                sum2 += c[j];
                ok2 = true;
            }
        }
        if (val1 == val2 && ok1 && ok2) {
            ans = max(ans, max(sum1, sum2));
        }
    }
    if (ans == -1) return "NO";
    stringstream ss;
    ss << ans;
    return ss.str();
}

main() {
    ios_base::sync_with_stdio(false);

    int T; cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase) {
        cout << "Case #" << testcase << ": " << solve() << '\r' << endl;
    }
}
