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
#define SCAN_INT() (*({int _si;scanf("%d", &_si); &_si;}))
#define REP(i,n) for( int i=0;i<int(n);++i)
namespace my_namespace {
};
#define FOR(i,p,k) for( int i=p; i<int(k); ++i)
using namespace my_namespace;
void problem()
{
    int n = SCAN_INT();
    int m = SCAN_INT();
    int a = SCAN_INT();
    FOR(x1, 0, n + 1) FOR(x2, 0, n + 1) if (max(x1, x2) - min(x1, x2) <= n)
        FOR(y1, 0, m + 1) FOR(y2, -m, m + 1) {
        int minx = min(0, min(x1, x2));
        int maxx = max(x1, x2);
        int miny = min(0, min(y1, y2));
        int maxy = max(y1, y2);
        if (maxx - minx > n || maxy - miny > m)
            continue;
        int area =::abs(x1 * y2 - x2 * y1);
        if (area == a) {
            x1 -= minx;
            x2 -= minx;
            y1 -= miny;
            y2 -= miny;
            printf("%d %d %d %d %d %d\n", x1, y1, -minx, -miny, x2, y2);
            return;
        }
        }
    printf("IMPOSSIBLE\n");
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
