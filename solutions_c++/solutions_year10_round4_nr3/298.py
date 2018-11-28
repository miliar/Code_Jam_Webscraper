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

#define MAX_N 300
int mem[MAX_N][MAX_N];

bool isAllDie(void) {
    REP(i, MAX_N) REP(j, MAX_N) if (mem[i][j])
        return false;
    return true;
}

void next(void) {
    for (int i = MAX_N-1; i >= 1; --i) for (int j = MAX_N-1; j >= 1; --j) {
        if (mem[i][j] && !mem[i-1][j] && !mem[i][j-1])
            mem[i][j] = 0;
        if (!mem[i][j] && mem[i-1][j] && mem[i][j-1])
            mem[i][j] = 1;
    }
}

int solve(vector<int> &X1, vector<int> &Y1, vector<int> &X2, vector<int> &Y2) {
    memset(mem, 0, sizeof(mem));
    REPV(X1, t) {
        FORE(i, Y1[t], Y2[t]) FORE(j, X1[t], X2[t]) {
            mem[i][j] = 1;
        }
    }
    int ret = 0;
    while(!isAllDie()) {
        next();
        ++ret;
    }
    return ret;
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int R;
        cin >> R;
        vector<int> X1(R), Y1(R), X2(R), Y2(R);
        REP(i, R) {
            cin >> X1[i] >> Y1[i] >> X2[i] >> Y2[i];
        }
        cerr << _t+1 << endl;
        cout << "Case #" << _t+1 << ": " << solve(X1, Y1, X2, Y2) << endl;
    }

    return 0;
}

