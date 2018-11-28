#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SZ(v) ((int)(v).size())
#define FOR(i, a, b) for (typeof(a) i = (a); i < (b); ++i)
#define FORD(i, a, b) for(typeof(a) i = (a);i >= (b); --i)
#define FOREACH(iter, v) for (typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define REP(i, n) FOR(i, 0, n)

typedef long long ll;

using namespace std;

int gcd(int a, int b)
{
    return b == 0 ? a : gcd(b, a%b);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, pd, pg;
    ll N;
    bool b;
    scanf("%d",&T);
    for (int c = 1; c <= T; ++c) {
        scanf("%lld%d%d",&N,&pd,&pg);
        if ((pd < 100 && pg == 100) || (pd > 0 && pg == 0)) {
            printf("Case #%d: Broken\n", c);
            continue;
        }
        if ((pd == 100 && pg == 100) || (pd == 0 && pg == 0)) {
            printf("Case #%d: Possible\n", c);
            continue;
        }
        b = false;
        if (N >= 100/gcd(pd,100)) {
            printf("Case #%d: Possible\n",c);
            b = true;
        }
        if (!b)
            printf("Case #%d: Broken\n", c);
    }
    return 0;
}
