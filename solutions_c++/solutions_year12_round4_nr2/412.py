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
#define REP(i,n) for( int i=0;i<int(n);++i)
namespace my_namespace {
};
#define MP make_pair
#define ALL(x) x.begin(),x.end()
#define PII pair<int,int>
#define VPII vector<PII>
#define SCAN_INT() (*({int _si;assert(1==scanf("%d", &_si)); &_si;}))
using namespace my_namespace;
VPII vec;
VPII ans;
int n, w, h;
void rec(int *pb, int e, int x1, int y1, int x2, int y2)
{
    int &b = *pb;
    if (b >= e)
        return;
    int r = vec[b].first;
    int minx = x1 ? x1 + r : x1;
    int miny = y1 ? y1 + r : y1;
    int maxx = x2 < w ? x2 - r : x2;
    int maxy = y2 < h ? y2 - r : y2;
    if (minx > maxx || miny > maxy)
        return;
    ans[b] = MP(minx, miny);
    b++;
    rec(&b, e, minx + r, y1, x2, miny + r);
    rec(&b, e, x1, miny + r, minx + r, y2);
    rec(&b, e, minx + r, miny + r, x2, y2);
}
void problem()
{
    assert(3 == scanf("%d%d%d", &n, &w, &h));
    vec.clear();
    ans.resize(n);
    REP(i, n)
     vec.push_back(MP(SCAN_INT(), i));
    sort(ALL(vec));
    reverse(ALL(vec));
    int b = 0;
    rec(&b, n, 0, 0, w, h);
    assert(b == n);
    VPII ans2(n);
    REP(i, n) {
        ans2[vec[i].second] = ans[i];
    }
    REP(i, n) {
        if (i)
            printf(" ");
        printf("%d %d", ans2[i].first, ans2[i].second);
    }
    printf("\n");
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
