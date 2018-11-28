#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <string.h>
using namespace std;

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<VVI> VVVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<VVB> VVVB;
typedef vector<ll> VL;
typedef vector<VL> VVL;
typedef vector<VVL> VVVL;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<VVC> VVVC;
typedef vector<string> VS;
typedef vector<VS> VVS;
typedef vector<VVS> VVVS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef vector<VD> VVD;
const double INF = 1e25;

double solve(VL& v, int j, int k, int n, int t) {
    double res = 0;
    int c = v.size();
    for (int i = 0; i < n; ++i) {
        if (i != k and i != j) res += 2*v[i%c];
        else {
            if (res + 2*v[i%c] < t) res += 2*v[i%c];
            else if (res > t) res += v[i%c];
            else {
                double first = (t - res)*0.5;
                res = res + (t - res) + (v[i%c] - first);
            }
        }
    }
    return res;
}

int main() {
    cout.setf(ios::fixed);
    cout.precision(0);
    int casos;
    cin >> casos;
    for (int cas = 1; cas <= casos; ++cas) {
        ll L, t, n, c;
        cin >> L >> t >> n >> c;
        VL v(c), sum(c);
        for (int i = 0; i < c; ++i) cin >> v[i];
        cout << "Case #" << cas << ": ";
        double res = INF;
        if (L == 0) cout << solve(v, -1, -1, n, t) << endl;
        else if (L == 1) {
            for (int i = 0; i < n; ++i) res = min(solve(v, i, -1, n, t), res);
            cout << res << endl;
        }
        else {
            for (int i = 0; i < n; ++i) {
                for (int j = i; j < n; ++j) {
                    res = min(res, solve(v, i, j, n, t));
                }
            }
            cout << res << endl;
        }
    }
}
