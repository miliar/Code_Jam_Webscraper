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
template <class T >int BC(T v)
{
    int cnt = 0;
    for (; v; v &= v - 1)
        cnt++;
    return cnt;
}
#define COND(p) if( p)
#define RESET(a,uch) memset( a, uch, sizeof( a))
#define REP(i,n) for( int i=0;i<int(n);++i)
namespace my_namespace {
};
#define ALWAYS(f,p) (*({bool _fa=true;f if(!(p)) {_fa=false;break;}&_fa;}))
#define EXISTS(f,p) !(ALWAYS(f,!(p)))
using namespace my_namespace;
int b[11][1 << 10];
void problem()
{
    int m, n;
    scanf("%d%d\n", &m, &n);
    bool a[10][10] = { };
    REP(i, m) {
        char b[11];
        scanf("%s\n", b);
        REP(j, n)
         a[i][j] = b[j] == '.';
    }
    RESET(b, -1);
    b[0][0] = 0;
    int r = 0;
    REP(cnt, m) {
        REP(mask, 1 << n) {
            if (EXISTS(REP(i, n), !a[cnt][i] && mask >> i & 1))
                continue;
            if (EXISTS(REP(i, n - 1), (mask >> i & 3) == 3))
                continue;
            int bc = BC(mask);
            int nm = 0;
            REP(i, n) COND(mask >> i & 1) {
                if (i + 1 < n)
                    nm |= 1 << i + 1;
                if (i - 1 >= 0)
                    nm |= 1 << i - 1;
            }
            REP(pmask, 1 << n) COND(b[cnt][pmask] >= 0 && (pmask & nm) == 0) {
                b[cnt + 1][mask] = max(b[cnt + 1][mask], b[cnt][pmask] + bc);
                r = max(r, b[cnt + 1][mask]);
            }
        }
    }
    printf("%d\n", r);
    return;
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
