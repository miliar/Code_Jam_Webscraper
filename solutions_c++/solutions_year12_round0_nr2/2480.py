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
#include <stdio.h>
using namespace std;
#define SCAN_INT() (*({int _si;assert(1==scanf("%d", &_si)); &_si;}))
#define RESET(a,uch) memset( a, uch, sizeof( a))
#define ITER(c) __typeof((c).begin())
#define VALT(c) __typeof(*(c).begin())
#define FORE(e,c) for( ITER(c) it_##e = (c).begin(), it2_##e = it_##e; it_##e!=(c).end() && it_##e==it2_##e; ++it_##e) for( VALT(c) e = *it_##e; it2_##e==it_##e; it2_##e++)
#define FOREC(e,c) for( __typeof(c) _t2_##e = c; !_t2_##e.empty(); _t2_##e.clear()) FORE(e,_t2_##e)
#define REP(i,n) for( int i=0;i<int(n);++i)
#define ALWAYS(f,p) (*({bool _fa=true;f if(!(p)) {_fa=false;break;}&_fa;}))
#define EXISTS(f,p) !(ALWAYS(f,!(p)))
#define VI vector<int>
#define FOR(i,p,k) for( int i=p; i<int(k); ++i)
#define VVI vector<VI>
#define COLLECT( t, f, p) (*({static vector<t> _col_vec; _col_vec.clear(); f _col_vec.push_back( p); &_col_vec;}))
namespace my_namespace {
    template <class X >static vector < X > VE(const X & x) {
        return vector < X > (1, x);
    } template <class X >static vector < X > &operator+=(vector < X > &vec,
     const X & el) {
        vec.push_back(el);
        return vec;
    }
    template <class X, class Y >static vector < X > operator+(vector < X > vec,
     const Y & y) {
        return vec += y;
    }
};
using namespace my_namespace;
VVI generate(int s)
{
    int m = s / 3;
    VVI results;
    FOR(v1, m - 2, m + 3) FOR(v2, m - 2, m + 3) FOR(v3, m - 2, m + 3) {
        if (v1 > v2 || v2 > v3)
            continue;
        if (v3 - v1 > 2)
            continue;
        if (v1 + v2 + v3 != s)
            continue;
        if (v1 < 0)
            continue;
        results.push_back(VE(v1) + v2 + v3);
    }
    return results;
}
int a[101][102];
void problem()
{
    int n, s, p;
    assert(3 == scanf("%d%d%d", &n, &s, &p));
    VI v = COLLECT(int, REP(i, n), SCAN_INT());
    RESET(a, 0xee);
    a[0][0] = 0;
    REP(i, n) REP(surprising, n + 1) {
        FOREC(vals, generate(v[i])) {
            int at_least_count = EXISTS(FORE(va, vals), va >= p);
            int new_surprising = surprising + (vals[2] - vals[0] == 2);
            a[i + 1][new_surprising] =
             max(a[i + 1][new_surprising], a[i][surprising] + at_least_count);
        }
    }
    printf("%d\n", a[n][s]);
}
int main()
{
    int n = SCAN_INT();
    REP(i, n) {
        printf("Case #%d: ", i + 1);
        problem();
    }
    return 0;
}
