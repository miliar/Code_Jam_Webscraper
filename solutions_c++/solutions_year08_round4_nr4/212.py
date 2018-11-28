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
#define ALL(x) x.begin(),x.end()
template <class X >class Miner {
    X v;
    bool e;
public:
     Miner() {
        e = true;
    } Miner < X > &operator<<(const X & nv) {
        if (e || nv < v) {
            v = nv;
            e = false;
        }
        return *this;
    }
    const X & get() const {
        return v;
}};
#define SCAN_INT() (*({int _si;scanf("%d", &_si); &_si;}))
#define REP(i,n) for( int i=0;i<int(n);++i)
#define VI vector<int>
namespace my_namespace {
    template <class X >static vector < X > &operator+=(vector < X > &vec,
     const X & el) {
        vec.push_back(el);
        return vec;
}};
using namespace my_namespace;
void problem()
{
    int k = SCAN_INT();
    char b[1001];
    scanf("%s", b);
    int l = strlen(b);
    VI vi;
    REP(i, k)
     vi += i;
    Miner < int >miner;
    do {
        char a[1001];
        memcpy(a, b, l);
        REP(i, l) {
            int d = i / k * k;
            int dd = i - d;
            a[i] = b[d + vi[dd]];
        }
        int cnt = 1;
        REP(i, l - 1) {
            if (a[i] != a[i + 1])
                cnt++;
        }
        miner << cnt;
        a[l] = 0;
    } while (next_permutation(ALL(vi)));
    printf("%d\n", miner.get());
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
