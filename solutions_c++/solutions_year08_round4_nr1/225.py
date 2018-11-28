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
using namespace std;
#define COND(p) if( p)
#define SCAN_INT() (*({int _si;scanf("%d", &_si); &_si;}))
#define REP(i,n) for( int i=0;i<int(n);++i)
namespace my_namespace {
};
#define FOR(i,p,k) for( int i=p; i<int(k); ++i)
using namespace my_namespace;
int values[10001];
int ops[10001];
bool changeable[10001];
int changecost[10001];
int op(int op, int a, int b)
{
    return op ? (a && b) : (a || b);
}
void problem()
{
    int m = SCAN_INT();
    int vv = SCAN_INT();
    int o = 1;
    REP(i, (m - 1) / 2) {
        int a = SCAN_INT();
        int b = SCAN_INT();
        ops[o] = a;
        changeable[o] = b;
        o++;
    }
    REP(i, (m + 1) / 2) {
        values[o] = SCAN_INT();
        o++;
    }
    for (int i = int (o) - 1; i >= int (1); i--) {
        if (i * 2 + 1 < o)
            values[i] = op(ops[i], values[2 * i], values[2 * i + 1]);
    }
    if (values[1] == vv) {
        printf("%d\n", 0);
        return;
    }
    FOR(i, 1, o)
     changecost[i] = 1000000;
    for (int i = int (o) - 1; i >= int (1); i--) {
        if (i * 2 + 1 >= o)
            continue;
        int &v = changecost[i];
        v = 1000000;
        REP(v1, 2) REP(v2, 2) COND(op(ops[i], v1, v2) != values[i]) {
            v =
             min(v,
             (v1 != values[2 * i] ? changecost[2 * i] : 0) + (v2 !=
              values[2 * i + 1] ? changecost[2 * i + 1] : 0));
        }
        if (changeable[i]) {
            REP(v1, 2) REP(v2, 2) COND(op(1 - ops[i], v1, v2) != values[i]) {
                v =
                 min(v,
                 1 + (v1 != values[2 * i] ? changecost[2 * i] : 0) + (v2 !=
                  values[2 * i + 1] ? changecost[2 * i + 1] : 0));
            }
        }
    }
    if (changecost[1] == 1000000)
        printf("IMPOSSIBLE\n");
    else
        printf("%d\n", changecost[1]);
}
int main()
{
    int n;
    scanf("%d", &n);
    REP(i, n) {
        printf("Case #%d: ", i + 1);
        problem();
    }
    return 0;
}
