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

int main() {
    int nTests = 0;
    scanf("%d\n", &nTests);

    FOR (test, 1, nTests) {

        int N, S, p;
        scanf("%d%d%d", &N, &S, &p);

        int ans = 0;
        REP (i, N) {
            int score = 0;
            scanf("%d", &score);

            if (score >= p) {
                int x = score - 3*p;
                // can achieve score without needing surprising triplet
                if (x >= 0 || (-2 <= x && x <= -1)) {
                    ++ans;
                    // can achieve score with needing surprising triplet
                } else if (-4 <= x && x <= -3) {
                    if (S > 0) {
                        --S;
                        ++ans;
                    }
                }
                // if x < -2 cannot achieve the score without gap of at
                // least 3
            }
        }

        printf("Case #%d: ", test);
        printf("%d\n", ans);
    }

    return 0;
}
