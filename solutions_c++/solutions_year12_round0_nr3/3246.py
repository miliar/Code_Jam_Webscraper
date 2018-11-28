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

const int MAX = 10001;

// cnt[k] how many recycled pairs there are in the interval
// from 0 to k
static int cnt[MAX];

static void init() {
    cnt[0] = 0;
    FOR (k, 1, MAX-1) {
        cnt[k] = cnt[k-1];

        ostringstream os;
        os << k;
        string kAsStr = os.str();
        int len = SIZE(kAsStr);
        FOR (i, 1, len-1) {
            string a = kAsStr.substr(i);
            string b = kAsStr.substr(0, i);
            if (a[0] != '0') {
                istringstream is(a + b);
                int x = 0;
                is >> x;
                if (x < k) {
                    // printf("k: %d, x: %d\n", k, x);
                    ++cnt[k];
                }
            }
        }
    }
}

static inline int go(int A, int B) {
    // return cnt[B] - cnt[A-1];

    set<PII> memo;
    int ans = 0;
    FOR (k, A, B) {
        ostringstream os;
        os << k;
        string kAsStr = os.str();
        int len = SIZE(kAsStr);
        FOR (i, 1, len-1) {
            string a = kAsStr.substr(i);
            string b = kAsStr.substr(0, i);
            if (a[0] != '0') {
                istringstream is(a + b);
                int x = 0;
                is >> x;
                if (A <= x && x < k && memo.find(MP(x, k)) == memo.end()) {
                    memo.insert(MP(x, k));
                    // printf("k: %d, x: %d\n", k, x);
                    ++ans;
                }
            }
        }
    }
    return ans;
}

int main() {
    int nTests = 0;
    scanf("%d\n", &nTests);

    init();

    FOR (test, 1, nTests) {
        int A, B;
        scanf("%d%d", &A, &B);

        printf("Case #%d: %d\n", test, go(A, B));
    }

    return 0;
}
