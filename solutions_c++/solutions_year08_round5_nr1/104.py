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
#define MP make_pair
#define IN(x,upper) ((x)>=0 && (x)<(upper))
#define PII pair<int,int>
#define SCAN_INT() (*({int _si;scanf("%d", &_si); &_si;}))
#define REP(i,n) for( int i=0;i<int(n);++i)
namespace my_namespace {
};
#define FOR(i,p,k) for( int i=p; i<int(k); ++i)
using namespace my_namespace;
char A[6011][6011];
bool Ri[6011][6011];
bool Bo[6011][6011];
int dx[] = { 0, 1, 0, -1 };
int dy[] = { 1, 0, -1, 0 };
void problem()
{
    int l;
    scanf("%d", &l);
    int x = 3005;
    int y = 3005;
    int dir = 0;
    int minx = 1000000;
    int miny = 1000000;
    int maxx = -1000000;
    int maxy = -1000000;
    REP(i, l) {
        char b[64];
        scanf("%s", b);
        int t = SCAN_INT();
        int ll = strlen(b);
        REP(j, t) REP(k, ll) {
            char ch = b[k];
            if (ch == 'L' || ch == 'R') {
                int a = ch == 'R' ? 1 : -1;
                dir = (4 + dir + a) % 4;
                continue;
            }
            if (dir == 0)
                Ri[x][y] = 1;
            if (dir == 1)
                Bo[x][y] = 1;
            minx = min(x - 2, minx);
            miny = min(y - 2, miny);
            maxx = max(x + 2, maxx);
            maxy = max(y + 2, maxy);
            x += dx[dir];
            y += dy[dir];
            if (dir == 2)
                Ri[x][y] = 1;
            if (dir == 3)
                Bo[x][y] = 1;
            minx = min(x - 2, minx);
            miny = min(y - 2, miny);
            maxx = max(x + 2, maxx);
            maxy = max(y + 2, maxy);
        }
    }
    assert(x == 3005 && y == 3005);
    queue < PII > q;
    q.push(MP(3005, 3005));
    while (!q.empty()) {
        int xx = q.front().first;
        int yy = q.front().second;
        q.pop();
        if (A[xx][yy])
            continue;
        A[xx][yy] = 1;
        REP(o, 4) {
            int nx = xx + dx[o];
            int ny = yy + dy[o];
            if (!IN(nx, 6011) || !IN(ny, 6011) || nx < minx || nx > maxx ||
             ny < miny || ny > maxy)
                continue;
            if (o == 0 && Bo[xx][yy + 1])
                continue;
            if (o == 1 && Ri[xx + 1][yy])
                continue;
            if (o == 2 && Bo[xx][yy])
                continue;
            if (o == 3 && Ri[xx][yy])
                continue;
            q.push(MP(nx, ny));
        }
    }
    minx = max(minx, 0);
    miny = max(miny, 0);
    if (A[minx][miny])
        FOR(i, minx, maxx) FOR(j, miny, maxy)
         A[i][j] = !A[i][j];
    int ret = 0;
    FOR(i, minx, maxx) {
        bool ok = false;
        FOR(j, miny, maxy) {
            if (!ok && A[i][j] & 1)
                ok = true;
            if (ok && (A[i][j] & 1) == 0)
                A[i][j] |= 2;
        }
        ok = false;
        for (int j = int (maxy) - 1; j >= int (miny); j--) {
            if (!ok && A[i][j] & 1)
                ok = true;
            if (ok && A[i][j] & 2) {
                A[i][j] |= 8;
                ret++;
            }
        }
    }
    FOR(j, miny, maxy) {
        bool ok = false;
        FOR(i, minx, maxx) {
            if (!ok && A[i][j] & 1)
                ok = true;
            if (ok && (A[i][j] & 1) == 0)
                A[i][j] |= 4;
        }
        ok = false;
        for (int i = int (maxx) - 1; i >= int (minx); i--) {
            if (!ok && A[i][j] & 1)
                ok = true;
            if (ok && A[i][j] & 4) {
                ret += !(A[i][j] & 8);
            }
        }
    }
    FOR(i, minx - 2, maxx + 2) FOR(j, miny - 2, maxy + 2)
     A[i][j] = Ri[i][j] = Bo[i][j] = 0;
    printf("%d\n", ret);
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
