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
#define SCAN_INT() (*({int _si;assert(1==scanf("%d", &_si)); &_si;}))
#define RESET(a,uch) memset( a, uch, sizeof( a))
#define REP(i,n) for( int i=0;i<int(n);++i)
namespace my_namespace {
};
using namespace my_namespace;
int a[2 * 4096];
void problem()
{
    RESET(a, 0x7f);
    int n = SCAN_INT();
    REP(i, 1 << n) {
        a[(1 << n) + i] = SCAN_INT();
    }
    REP(i, (1 << n) - 1)
     SCAN_INT();
    int tot = 0;
    for (int i = (1 << n) - 1; i >= 1; i--) {
        int m = min(a[2 * i], a[2 * i + 1]);
        if (!m)
            tot++;
        else
            m--;
        a[i] = m;
    }
    printf("%d\n", tot);
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
