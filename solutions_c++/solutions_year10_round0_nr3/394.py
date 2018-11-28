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

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int R, k, N;
        cin >> R >> k >> N;
        static ll w[2000];
        REP(i, N)
            cin >> w[i];
        ll tot = 0;
        int j = 0;
        ll mem[2000];
        int nextJ[2000];
        REP(i, N) {
            mem[i] = -1;
            nextJ[i] = -1;
        }
        REP(i, R) {
            if (mem[j] != -1) {
                tot += mem[j];
                j = nextJ[j];
            } else {
                int startJ = j;
                ll cur = 0;
                while (cur+w[j] <= k) {
                    cur += w[j];
                    j = (j+1)%N;
                    if (j == startJ)
                        break;
                }
                mem[startJ] = cur;
                nextJ[startJ] = j;
                tot += cur;
            }
        }
        cerr << _t+1 << "/" << T << endl;
        cout << "Case #" << _t+1 << ": " << tot << endl;
    }
    return 0;
}

