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
#define LL long long
#define MP make_pair
#define IN(x,upper) ((x)>=0 && (x)<(upper))
#define REP(i,n) for( int i=0;i<int(n);++i)
namespace my_namespace {
};
using namespace my_namespace;
int W, H;
int find_lowest_mult(int x, int y, int x1, int y1)
{
    if (x >= 0 && y >= 0)
        return 0;
    int low = 0;
    int hi = 2000000;
    int ret = -1;
    if (x1 == 0 && x < 0 || y1 == 0 && y < 0)
        return -10000000;
    assert(x1 >= 0 && y1 >= 0);
    while (low <= hi) {
        int m = low + hi >> 1;
        int xx = x + x1 * m;
        int yy = y + y1 * m;
        if (xx >= 0 && yy >= 0) {
            ret = m;
            hi = m - 1;
        } else {
            low = m + 1;
        }
    }
    assert(ret >= 0);
    return ret;
}
int find_highest_mult(int x, int y, int x1, int y1)
{
    int low = -1000000;
    int hi = 2000000;
    int ret = -1;
    if (x1 == 0 && x >= W || y1 == 0 && y >= H)
        return -10000000;
    assert(x1 >= 0 && y1 >= 0);
    while (low <= hi) {
        int m = low + hi >> 1;
        int xx = x + x1 * m;
        int yy = y + y1 * m;
        if (xx < W && yy < H) {
            ret = m;
            low = m + 1;
        } else {
            hi = m - 1;
        }
    }
    return ret;
}
void special_case(int x1, int y1, int x2, int y2, int x, int y)
{
    if (x1 == 0) {
        swap(x1, y1);
        swap(x2, y2);
        swap(W, H);
        swap(x, y);
    }
    assert(x1);
    queue < int >q;
    vector < bool >vis(2200000);
    q.push(0);
    int acc = 0;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        if (vis[1100000 + v])
            continue;
        vis[1100000 + v] = true;
        int xx = x + v;
        int yy = y + v * y1 / x1;
        if (!IN(xx, W) || !IN(yy, H))
            continue;
        acc++;
        q.push(xx + x1 - x);
        q.push(xx + x2 - x);
    }
    printf("%d\n", acc);
}
void problem()
{
    scanf("%d%d", &W, &H);
    int x1, y1, x2, y2;
    int x, y;
    scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
    scanf("%d%d", &x, &y);
    if (x1 < 0) {
        x1 *= -1;
        x2 *= -1;
        x = W - 1 - x;
    }
    if (y1 < 0) {
        y1 *= -1;
        y2 *= -1;
        y = H - 1 - y;
    }
    if (x1 * y2 == x2 * y1) {
        return special_case(x1, y1, x2, y2, x, y);
    }
    LL acc = 0;
    int lx = x;
    int ly = y;
    int m = find_highest_mult(lx, ly, x1, y1);
    assert(m != -1);
    int hx = lx + m * x1;
    int hy = ly + m * y1;
    acc += m + 1;
    ;
    while (true) {
        lx += x2;
        ly += y2;
        hx += x2;
        hy += y2;
        ;
        int mlow = find_lowest_mult(lx, ly, x1, y1);
        int mhigh = find_highest_mult(lx, ly, x1, y1);
        ;
        if (mlow == -10000000 || mhigh == -10000000)
            break;
        int nlx = lx + mlow * x1;
        int nly = ly + mlow * y1;
        int nhx = lx + mhigh * x1;
        int nhy = ly + mhigh * y1;
        if (MP(lx, ly) > MP(nhx, nhy) || MP(hx, hy) < MP(nlx, nly))
            break;
        if (MP(lx, ly) < MP(nlx, nly)) {
            lx = nlx;
            ly = nly;
        }
        if (true || MP(hx, hy) > MP(nhx, nhy)) {
            hx = nhx;
            hy = nhy;
        };
        if (x1) {
            acc += (hx - lx) / x1 + 1;
        } else {
            acc += (hy - ly) / y1 + 1;
        }
        ;
    }
    printf("%lld\n", acc);
}
int main(int argc, char **argv)
{
    int n;
    scanf("%d", &n);
    REP(i, n) {
        printf("Case #%d: ", i + 1);
        problem();
    }
    return 0;
}
