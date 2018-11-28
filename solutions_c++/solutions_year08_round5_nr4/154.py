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
#define RESET(a,uch) memset( a, uch, sizeof( a))
#define IN(x,upper) ((x)>=0 && (x)<(upper))
#define REP(i,n) for( int i=0;i<int(n);++i)
namespace my_namespace {
};
using namespace my_namespace;
int a[100][100];
int dx[] = { 1, 2 };
int dy[] = { 2, 1 };
void problem()
{
    int m, n, r;
    scanf("%d%d%d", &m, &n, &r);
    RESET(a, 0);
    a[0][0] = 1;
    REP(i, r) {
        int x, y;
        scanf("%d%d", &x, &y);
        x--;
        y--;
        a[x][y] = -1;
    }
    REP(i, m) REP(j, n) COND(a[i][j] >= 1) {
        REP(o, 2) {
            int ni = i + dx[o];
            int nj = j + dy[o];
            if (IN(ni, m) && IN(nj, n) && a[ni][nj] >= 0) {
                a[ni][nj] += a[i][j];
                a[ni][nj] %= 10007;
            }
        }
    }
    printf("%d\n", a[m - 1][n - 1]);
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
