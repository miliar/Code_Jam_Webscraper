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
#define MP make_pair
#define COND(p) if( p)
namespace my_namespace {
};
#define SCAN_INT() (*({int _si;assert(1==scanf("%d", &_si)); &_si;}))
#define PII pair<int,int>
#define VPII vector<PII>
#define FOR(i,p,k) for( int i=p; i<int(k); ++i)
using namespace my_namespace;
int a[10002];
void problem()
{
    int n;
    assert(1 == scanf("%d", &n));
    VPII vec;
    REP(i, n) {
        int a, b;
        assert(2 == scanf("%d%d", &a, &b));
        vec.push_back(MP(a, b));
    }
    vec.push_back(MP(SCAN_INT(), 2000000000));
    REP(i, n + 1)
     a[i] = -1;
    a[0] = vec[0].first;
    REP(i, n) COND(a[i] >= 0) {
        int r = a[i];
        FOR(j, i + 1, n + 1) {
            if (vec[j].first > vec[i].first + r)
                break;
            a[j] = max(a[j], min(vec[j].second, vec[j].first - vec[i].first));
        }
    }
    printf("%s\n", a[n] >= 0 ? "YES" : "NO");
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
