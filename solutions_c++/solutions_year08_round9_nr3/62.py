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
#define IN(x,upper) ((x)>=0 && (x)<(upper))
template <class X >class Maxer {
    X v;
    bool e;
public:
     Maxer() {
        e = true;
    } Maxer < X > &operator<<(const X & nv) {
        if (e || nv > v) {
            v = nv;
            e = false;
        }
        return *this;
    }
    const X & get() const {
        return v;
    } bool empty() {
        return e;
    }
};
#define REP(i,n) for( int i=0;i<int(n);++i)
namespace my_namespace {
};
#define FOR(i,p,k) for( int i=p; i<int(k); ++i)
using namespace my_namespace;
int r, c;
int a[50][50];
int value(int mask)
{
    REP(i, r) REP(j, c) {
        int left = a[i][j];
        FOR(ii, i - 1, i + 2) FOR(jj, j - 1, j + 2) COND(IN(ii, r) && IN(jj, c)) {
            if (mask >> ii * c + jj & 1)
                left--;
        }
        if (left)
            return -1;
    }
    int acc = 0;
    REP(j, c)
     acc += mask >> r / 2 * c + j & 1;
    return acc;
}
void problem()
{
    scanf("%d%d", &r, &c);
    REP(i, r) REP(j, c)
     scanf("%d", a[i] + j);
    Maxer < int >best;
    REP(mask, (1 << r * c)) {
        int v = value(mask);
        if (v < 0)
            continue;
        best << v;
    }
    assert(!best.empty());
    printf("%d\n", best.get());
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
