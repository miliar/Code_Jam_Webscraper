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

int solve(int P, vector<int> &w) {
    vector<bool> mem((1<<P)-1, false);
    REP(i, 1<<P) {
        int left = P-w[i];
        int mask = (1<<(P-1));
        int p = 0;
        while(left) {
            mem[p] = true;
            if (i & mask)
                p = 2*p+2;
            else
                p = 2*p+1;
            mask >>= 1;
            --left;
        }
    }
    int ret = 0;
    REP(i, 1<<P) if (mem[i])
        ++ret;
    return ret;
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int P;
        cin >> P;
        vector<int> w(1<<P);
        REP(i, (1<<P))
            cin >> w[i];
        cout << "Case #" << _t+1 << ": " << solve(P, w) << endl;
        REP(i, (1<<P)-1)  // remove 1
            cin >> w[0];
    }
    return 0;
}

