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

const int inf = INT_MAX/2;

int solve(vector<int> &w, int D, int I, int M) {
    vector<int> mem(256, 0);
    int size = w.size();
    REP(i, size) {
        vector<int> next(256, inf);
        // none
        REP(j, 256) if (abs(j-w[i]) <= M) {
            next[w[i]] = min(next[w[i]], mem[j]);
            assert(next[w[i]] >= 0);
        }
        // delete
        REP(j, 256) {
            next[j] = min(next[j], mem[j]+D);
            assert(next[j] >= 0);
        }
        // insert
        REP(j, 256) {
            REP(k, 256) {
                int d = abs(k-j);
                int num = M == 0 ? (d == 0 ? 0 : inf) : (d+M-1)/M-1;
                if (num < 0)
                    num = 0;
                if (num != inf) {
                    next[k] = min(next[k], mem[j]+num*I+abs(w[i]-k));
                }
                assert(next[k] >= 0);
            }
        }
        // change w[i]->k
        REP(j, 256) {
            FORE(dj, -M, M) {
                int k = j+dj;
                if (0 <= k && k < 256) {
                    int d = abs(k-w[i]);
                    next[k] = min(next[k], mem[j]+d);
                    assert(next[k] >= 0);
                }
            }
        }
        mem = next;
    }
    return *min_element(mem.begin(), mem.end());
}

int main(void)
{
    int T;
    cin >> T;
    REP(_t, T) {
        int D, I, M, N;
        cin >> D >> I >> M >> N;
        vector<int> w(N);
        REP(i, N)
            cin >> w[i];
        cout << "Case #" << _t+1 << ": " << solve(w, D, I, M) << endl;
    }
    return 0;
}

