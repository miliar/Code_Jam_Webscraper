
// Tomasz Kulczynski
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <numeric>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long LL;
typedef double D;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for (int i=0;i<(n);++i)
#define FOR(i,a,b) for (VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(e,v) for(VAR(e,(v).begin());e!=(v).end();++e)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)(a).size())
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

int t[33][2];

int main() {
    REP(i, 31) REP(j, 2) t[i][j] = -1;
    FOR(c, 0, 10)
        FOR(b, 0, c)
            FOR(a, 0, b) {
                if(c - a > 2)
                    continue;
                t[a+b+c][c-a == 2] = max(t[a+b+c][c-a == 2], c);
            }
    int tt;
    scanf("%d",&tt);
    FOR(cas, 1, tt) {
        int n, s, p;
        scanf("%d %d %d", &n, &s, &p);
        int a[2][2];
        REP(i, 2) REP(j, 2) a[i][j] = 0;
        REP(i, n) {
            int x;
            scanf("%d", &x);
            a[t[x][0] >= p][t[x][1] >= p]++;
        }
        int ret = 0;
        int x = min(a[0][1], s);
        s -= x;
        a[0][1] -= x;
        n -= x;
        ret += x;
        x = min(a[1][1], s);
        s -= x;
        a[1][1] -= x;
        n -= x;
        ret += x;
        ret += a[1][0] + a[1][1];
        printf("Case #%d: %d\n", cas, ret);
    }
    return 0;
}
