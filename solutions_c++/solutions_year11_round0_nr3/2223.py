#include <iostream>
#include <bitset>
#include <cstdio>
#include <sstream>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <numeric>
#include <functional>
#include <string>
#include <cstdlib>
#include <cmath>
#include <list>

using namespace std;

#define FOR(i,a,b) for(int i=(a),_b(b);i<_b;++i)
#define FORD(i,a,b) for(int i=(a),_b(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define UNIQUE(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back

#define X first
#define Y second

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long long ll;

int main() {
#ifdef LOCAL
	freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
#endif
    int t;
    cin >> t;
    FOR (nt, 1, t+1) {
        int n;
        cin >> n;
        int r = 0;
        int g;
        int S = 0;
        int mi = -1u/4;
        REP (i, n) {
            cin >> g;
            r ^= g;
            S += g;
            mi = min(mi, g);
        }
        cout << "Case #" << nt << ": ";
        if (r) {
            cout << "NO\n";
        } else {
            cout << S-mi << endl;
        }
    }
	return 0;
}
