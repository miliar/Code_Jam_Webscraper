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

string to_string(ll in) { stringstream ss; ss << in; return ss.str(); }

string solve() {
    ll N, L, H; cin >> N >> L >> H;
    ll mul = 1;
    ll in;
    vector<ll> v(N);
    rep(i, N) { cin >> v[i]; }
    ll ret = inf;
    for (ll i = L; i <= H; ++i) {
        bool ok = true;
        for (int j = 0; j < sz(v); ++j) {
            if (max(v[j], i) % min(v[j], i) != 0) {
                ok = false;
                break;
            }
        }
        if (ok) {
            return to_string(i);
        }
    }
    return "NO";
}

main() {
    ios_base::sync_with_stdio(false);

    int T; cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase) {
        cout << "Case #" << testcase << ": " << solve() << '\r' << endl;
    }
}
