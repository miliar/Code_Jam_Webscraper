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
#define LD long double
#define SCAN_INT() (*({int _si;scanf("%d", &_si); &_si;}))
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
}};
#define REP(i,n) for( int i=0;i<int(n);++i)
#define SZ size()
#define PLD pair<LD,LD>
namespace my_namespace {
    template <class X >static vector < X > VE(const X & x) {
        return vector < X > (1, x);
    } template <class X >static vector < X > &operator+=(vector < X > &vec,
     const X & el) {
        vec.push_back(el);
        return vec;
    }
    template <class X, class Y >static vector < X > operator+(vector < X > vec,
     const Y & y) {
        return vec += y;
    }
};
using namespace my_namespace;
LD solve(vector < PLD > vec)
{
    int n = vec.SZ;
    Miner < LD > miner;
    REP(i, n) REP(j, i + 1) {
        LD p =
         (vec[i].first * vec[j].second +
         vec[j].first * vec[i].second) / (vec[i].second + vec[j].second);
        Maxer < LD > maxer;
        REP(k, n)
         maxer << fabsl(p - vec[k].first) / vec[k].second;
        miner << maxer.get();
    }
    return miner.get();
}
LD wmid(LD x1, LD p1, LD x2, LD p2)
{
    return (x1 * p2 + x2 * p1) / (p1 + p2);
}
LD dist(vector < LD > a, vector < LD > b)
{
    LD sum = 0;
    REP(o, 3) {
        sum += fabsl(a[o] - b[o]);
    }
    return sum;
}
void problem()
{
    int n = SCAN_INT();
    vector < vector < LD > > vec;
    REP(i, n) {
        LD a, b, c, d;
        scanf("%Lf%Lf%Lf%Lf", &a, &b, &c, &d);
        vec += VE(a) + b + c + d;
    }
    LD l = 0;
    LD u = 1e20;
    LD m;
    REP(cnt, 1000) {
        m = (l + u) / 2;
        bool ok = true;
        REP(i, n) REP(j, i) {
            vector < LD > ve;
            REP(o, 3)
             ve += wmid(vec[i][o], vec[i][3], vec[j][o], vec[j][3]);
            LD d1 = dist(vec[i], ve) / vec[i][3];
            LD d2 = dist(vec[j], ve) / vec[j][3];
            if (d1 > m || d2 > m) {
                ok = false;
            }
        }
        if (ok)
            u = m;
        else
            l = m;
    }
    printf("%Lf\n", m);
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
