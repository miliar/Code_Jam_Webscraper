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

map<pair<int, int>, bool> mem[2];

bool canWinR(int a, int b, int turn) {
    if (a == b)
        return false;
    if (a > b)
        swap(a, b);
    if (a == 1)
        return true;
    pair<int, int> t(a, b);
    if (mem[turn].find(t) == mem[turn].end()) {
        bool win = false;
        int nb = b%a;
        if (nb == 0)
            nb += a;
        while(nb != b) {
            if (!canWinR(a, nb, 1-turn)) {
                win = true;
                break;
            }
            nb += a;
        }
        mem[turn][t] = win;
    }
    return mem[turn][t];
}

bool canWin(int a, int b) {
    return canWinR(a, b, 0);
}

int solve(int a1, int a2, int b1, int b2) {
    int ret = 0;
    FORE(a, a1, a2) FORE(b, b1, b2) {
        if (canWin(a, b))
            ++ret;
    }
    return ret;
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int a1, a2, b1, b2;
        cin >> a1 >> a2 >> b1 >> b2;
        cout << "Case #" << _t+1 << ": " << solve(a1, a2, b1, b2) << endl;
    }
    return 0;
}
