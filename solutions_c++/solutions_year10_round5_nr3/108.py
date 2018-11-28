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

#define OFFSET 2000000
int mem[2*OFFSET];

ll solve(int n) {
    assert(n < 2*OFFSET);
    ll ret = 0;
    if (mem[n] >= 2) {
        ret += mem[n]/2;
        mem[n-1] += mem[n]/2;
        mem[n+1] += mem[n]/2;
        mem[n] = mem[n]%2;
        ret += solve(n-1) + solve(n+1);
    }
    return ret;
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int C;
        cin >> C;
        vector<int> P(C), V(C);
        REP(i, C)
            cin >> P[i] >> V[i];
        memset(mem, 0, sizeof(mem));
        REP(i, C)
            mem[P[i]+OFFSET] = V[i];
        ll ret = 0;
        REP(i, C)
            ret += solve(P[i]+OFFSET);
        cerr << _t+1 << endl;
        cout << "Case #" << _t+1 << ": " << ret << endl;
    }
    return 0;
}
