#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

#define REP(a, b) for(int a=0; a<(b); a++)
#define FOR(a, b, c) for(int a=(b); a<=(c); a++)
#define FORD(a, b, c) for(int a=(b); a>=(c); a--)
#define ABS(a) ((a)<0 ? -(a) : (a))
#define MP make_pair
#define F first
#define S second

int main() {
    int z;
    scanf("%d", &z);
    FOR(zz, 1, z) {
        int a, n, m;
        scanf("%d%d%d", &n, &m, &a);
        bool end = false;
        if (n*m<=a)
        FOR(Ax, 0, n) FOR(By, 0, m) if (Ax!=0 || By!=0) {
            REP(Cx, n+1) REP(Cy, m+1) if (a==ABS(Ax*By-Ax*Cy-By*Cx) && MP(Cx, Cy)!=MP(Ax, 0) && MP(Cx, Cy)!=MP(0, By)) {
                printf("Case #%d: %d %d %d %d %d %d\n", zz, Ax, 0, 0, By, Cx, Cy);
                end = true;
                goto endL;
            }
        }
        endL:
        if (!end)
            printf("Case #%d: IMPOSSIBLE\n", zz);
    }
    return 0;
}
