#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <sys/time.h>
#include <utility>
#include <vector>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,a,b) for(int i=(int)(a);i>=(int)(b);--i)
#define FORE(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define FORED(i,c) for(__typeof((c).begin()) i=(c).end();i!=(c).begin();--i)
#define ITER(c) __typeof((c).begin())
#define SZ(a) (int)(a).size()

const int INF = 1000000000;
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
template<class T> inline int size(const T&c) { return c.size(); }


int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w+", stdout);
    int n;
    scanf("%d", &n);
    REP(i, n) {
        LL N, Pd, Pg;
        bool found = false;
        scanf("%lld %lld %lld", &N, &Pd, &Pg);
        for (LL D = 1; D <= N; D++) {
            if (!((Pd * D) % 100LL)) {
                found = true;
                break;
            }
        }
        if (found && !(Pd < 100LL && Pg == 100LL) && !(Pd > 0LL && Pg == 0LL))
            printf("Case #%d: Possible\n", i+1);
        else
            printf("Case #%d: Broken\n", i+1);
    }
    fclose(stdin);
    fclose(stdout);
}
