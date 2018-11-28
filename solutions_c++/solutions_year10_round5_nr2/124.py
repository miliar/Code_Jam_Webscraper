#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <climits> 
#include <cfloat> 
#include <map> 
#include <utility> 
#include <set> 
#include <iostream> 
#include <memory> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <sstream> 
#include <complex> 
#include <stack> 
#include <queue> 
#include <numeric>
#include <cassert>

#define FOR(i, min, max) for (int i = (min); i < (max); ++i) 
#define FORE(i, min, max) for (int i = (min); i <= (max); ++i) 
#define REP(i, n) for (int i = 0; i < (n); ++i) 
#define REPV(vec, i) for (int i = 0; i < (int)(vec.size()); ++i) 
#define FOR_EACH(vec, it) for (typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); ++it)

using namespace std; 
static const double EPS = 1e-12; 
typedef long long ll; 

#define MAX_T 1000000LL

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        ll L;
        int N;
        cin >> L >> N;
        vector<ll> B(N);
        REP(i, N)
            cin >> B[i];
        ll maxB = *max_element(B.begin(), B.end());
        ll offset = max(0LL, (L-MAX_T)/maxB);
        L = L-offset*maxB;
        vector<ll> w(L+1, LONG_LONG_MAX);
        w[0] = 0LL;
        REPV(B, i) {
            REP(j, L-B[i]+1) if (w[j] != LONG_LONG_MAX) {
                w[j+B[i]] = min(w[j+B[i]], w[j]+1LL);
            }
        }
        cerr << _t+1 << endl;
        if (w[L] == LONG_LONG_MAX)
            cout << "Case #" << _t+1 << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << _t+1 << ": " << w[L]+offset << endl;
    }

    return 0;
}

