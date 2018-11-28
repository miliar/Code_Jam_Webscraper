#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <complex>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <climits>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,start,end) for (int var=(start); var<=(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(end); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

// typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector< vector<int> > VVI;
typedef vector< vector<bool> > VVB;

int a[1010];

int main() {
    int nTests = 0;
    cin >> nTests;

    FOR (test, 1, nTests) {
        int N = 0;
        cin >> N;
        int patrickSum = 0;
        int seanSum = 0;
        REP (i, N) {
            cin >> a[i];
            patrickSum ^= a[i];
            seanSum += a[i];
        }

        cout << "Case #" << test << ": ";

        vector<PII> lst;
        int best = 0;
        lst.PB(MP(0, 0));
        REP (i, N) {
            int sz = SIZE(lst);
            REP (j, sz) {
                lst.PB(MP(lst[j].ST ^ a[i], lst[j].ND + a[i]));
                if (lst[j].ND + a[i] < seanSum &&
                    (lst[j].ST ^ a[i]) == (patrickSum ^ (lst[j].ST ^ a[i]))) {
                    // cout << lst[j].ND + a[i] << endl;
                    best = max(best,
                               max(lst[j].ND + a[i],
                                   seanSum - (lst[j].ND + a[i])));
                }
            }
        }

        // best[0][0] = 1;
        // FOR (i, 1, N) {
        //     REP (j, 1000010) {
        //         best[i][j] |= best[i-1][j];
        //         if (j-a[i] >= 0) {
        //             best[i][j] |= best[i-1][j-a[i]];
        //         }
        //     }
        // }

        if (best == 0) cout << "NO\n";
        else cout << best << '\n';
    }

    return 0;
}
