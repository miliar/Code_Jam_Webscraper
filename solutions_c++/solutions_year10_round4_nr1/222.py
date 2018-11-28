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
#define ALL(x) x.begin(),x.end()
#define MP make_pair
#define SCAN_INT() (*({int _si;assert(1==scanf("%d", &_si)); &_si;}))
#define IN(x,upper) ((x)>=0 && (x)<(upper))
#define PII pair<int,int>
#define REP(i,n) for( int i=0;i<int(n);++i)
namespace my_namespace {
};
using namespace my_namespace;
int a[150][150];
void problem()
{
    int n;
    char b[200];
    assert(b == fgets(b, sizeof(b), stdin));
    assert(1 == sscanf(b, "%d", &n));
    vector < pair < PII, int > > vec;
    REP(i, n * 2 - 1) {
        assert(b == fgets(b, sizeof(b), stdin));
        int l = strlen(b);
        REP(j, l) {
            char ch = b[j];
            if (ch < '0' || ch > '9')
                continue;
            int v1 = i - j;
            int v2 = i;
            vec.push_back(MP(MP(v1, v2), int (ch - '0')));
        }
    }
    sort(ALL(vec));
    int o = 0;
    REP(i, n) REP(j, n)
     a[i][j] = vec[o++].second;
    double mn = 10000;
    REP(xo, 2 * n) REP(yo, 2 * n) {
        if ((xo & 1) != (yo & 1))
            continue;
        double xx = xo / 2.0;
        double yy = yo / 2.0;
        bool bad = false;
        REP(i, n) REP(j, n) {
            int i2 = xo - i;
            int j2 = yo - j;
            if (!IN(i2, n) || !IN(j2, n) || a[i][j] == a[i2][j2])
                continue;
            bad = true;
            break;
        }
        if (bad)
            continue;
        mn = min(mn, max(max(n - 1 - xx, xx), max(n - 1 - yy, yy)));
    }
    int res = mn * 2 + 1 + 0.1;
    printf("%d\n", res * res - n * n);
}
int main()
{
    int n = SCAN_INT();
    assert(0 == scanf(" "));
    REP(i, n) {
        printf("Case #%d: ", i + 1);
        problem();
    }
    return 0;
}
