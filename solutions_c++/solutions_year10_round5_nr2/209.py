#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cassert>
#include <math.h>
#include <string.h>
using namespace std;
#define LL long long
#define SCAN_INT() (*({int _si;assert(1==scanf("%d", &_si)); &_si;}))
#define REP(i,n) for( int i=0;i<int(n);++i)
namespace my_namespace {
};
#define VI vector<int>
#define ALL(x) x.begin(),x.end()
#define MP make_pair
using namespace my_namespace;
int g_OnlyTest = -1;
int g_CurrentTest;
void Init(int argc, const char **argv)
{
    const char *s = 1 < argc ? argv[1] : NULL;
    g_OnlyTest = s ? atoi(s) - 1 : -1;
}
bool ShouldSkip()
{
    return g_OnlyTest >= 0 && g_CurrentTest != g_OnlyTest;
}
int a[150][150];
void problem()
{
    int n;
    LL l;
    assert(2 == scanf("%lld%d", &l, &n));
    VI vec;
    REP(i, n)
     vec.push_back(SCAN_INT());
    sort(ALL(vec));
    int p = vec.back();
    priority_queue < pair < pair < int, LL >, int > > q;
    q.push(MP(pair < int, LL > (-0, 0), 0));
    vector < vector < pair < int, LL > > > a(p);
    int rem = l % p;
    LL best = 0x7fffffffffffffffLL;
    while (!q.empty()) {
        int steps = -q.top().first.first;
        LL len = q.top().first.second;
        int pos = q.top().second;
        assert(steps < 1000000000);
        assert(pos < p && pos >= 0);
        assert(len % p == pos);
        q.pop();
        ;
        if (len > l)
            continue;
        bool ok = true;
        if (!a[pos].empty()) {
            LL ldif = len - a[pos].back().second;
            assert(ldif % p == 0);
            assert(steps >= a[pos].back().first);
            if (ldif < 0) {
                ok = false;
            } else {
                int osteps = a[pos].back().first;
                LL adj = ldif / p;
                ok = steps < osteps + adj;
            }
            ;
        }
        if (!ok)
            continue;
        if (rem == pos) {
            assert((l - len) % p == 0);
            LL rsteps = steps + (l - len) / p;
            best = min(best, rsteps);
        }
        a[pos].push_back(pair < int, LL > (steps, len));
        ;
        REP(i, vec.size() - 1) {
            if (vec[i] == 0)
                continue;
            LL nlen = len + vec[i];
            int nsteps = steps + 1;
            int npos = (pos + vec[i]) % p;
            q.push(MP(pair < int, LL > (-nsteps, nlen), npos));
        }
    }
    if (best == 0x7fffffffffffffffLL)
        printf("IMPOSSIBLE\n");
    else
        printf("%lld\n", best);
}
int main(int argc, const char **argv)
{
    Init(argc, argv);
    int n = SCAN_INT();
    assert(0 == scanf(" "));
    for (g_CurrentTest = 0; g_CurrentTest < n; g_CurrentTest++) {
        if (!ShouldSkip())
            printf("Case #%d: ", g_CurrentTest + 1);
        problem();
    }
    return 0;
}
