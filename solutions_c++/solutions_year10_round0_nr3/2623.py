#include <iostream>
#include <cstdio>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <sstream>
#include <ctime>
#include <numeric>
#include <cstring>
#include <functional>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef map<string, int> MSI;

#define REP(i, n) for (int i = 0; i < n; ++i)
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORD(i, a, b) for (int i = a-1; i >= b; --i)
#define ALL(x) x.begin(), x.end()
#define SIZE(x) (int)x.size()
#define FOREACH(it, c) for (__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define INF 987654321
#define PB push_back
#define MP make_pair
#define DEBUG(x) cerr<<#x<<": "<<x<<endl;
#define ERR(...) fprintf(stderr, __VA_ARGS__);
#define EPS 1e-9
#define INIT { REP(i,0);FOR(i,0,0);FORD(i,0,0);DEBUG("");ERR("\n");PII b=MP(SIZE(VI()), int(INF+EPS));VPII a;a.PB(b);VS s;}
#define ACC accumulate

queue<int> q;

int main(void) {
    int t;
    scanf("%d", &t);
    FOR(i, 1, t+1) {
        int r, k, n;
        scanf("%d %d %d", &r, &k, &n);
        int g;
        REP(j, n) {
            scanf("%d", &g);
            q.push(g);
        }
        int res = 0;
        REP(l, r) {
            int p = 0, poc = 0;
            while (p+1 <= n && poc+q.front() <= k) {
                int pom = q.front();
                poc += pom;
                p++;
                q.pop();
                q.push(pom);
            }
            res += poc;
        }
        while (!q.empty()) {
            q.pop();
        }
        printf("Case #%d: %d\n", i, res);
    }
    return 0;
}

                
