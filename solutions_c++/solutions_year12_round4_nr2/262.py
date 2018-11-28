
// Tomasz Kulczynski
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <numeric>
using namespace std;

#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long LL;
typedef double D;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for (int i=0;i<(n);++i)
#define FOR(i,a,b) for (VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(e,v) for(VAR(e,(v).begin());e!=(v).end();++e)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)(a).size())
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

typedef pair<D, D> PDD;

#include <cassert>

LL sqr(int x) {
    return 1LL * x * x; 
}

LL dist(PII a, PII b) {
    return sqr(a.X - b.X) + sqr(a.Y - b.Y);
}

vector<PII> rob(int n, int xx, int yy, VI rr) {
    vector<PII> r;
    REP(i, n) r.PB(MP(2*rr[i], i));
    sort(ALL(r));
    reverse(ALL(r));
    int i = 0;
    vector<PII> ret(n);
    while(i < n && r[i].X > min(xx, yy)) {
        ret[r[i].Y] = MP(xx, yy);
        if(xx < r[i].X)
            yy -= r[i].X;
        else
            xx -= r[i].X;
        i++;
    }
    vector<pair<PII, PII> > pr;
    pr.PB(MP(MP(xx, yy), MP(0, 0)));
    for(; i < n; i++) {
        if(pr.empty())
            assert(false);
        pair<PII, PII> p = pr.back();
        pr.pop_back();
        if(p.X.X < r[i].X || p.X.Y < r[i].Y)
            continue;
//        assert(p.X.X >= r[i].X && p.X.Y >= r[i].Y);
        ret[r[i].Y] = MP(p.Y.X + r[i].X / 2, p.Y.Y + r[i].X / 2);
        if(i < n-1 && p.X.X - r[i].X < r[i+1].X && p.X.Y - r[i].X < r[i+1].X) {
            int r1 = r[i].X / 2, r2 = r[i+1].X / 2;
            if(dist(MP(r1, r1), MP(p.X.X - r2, p.X.Y - r2)) >= sqr(r1 + r2)) {
                ret[r[i+1].Y] = MP(p.Y.X + p.X.X - r2, p.Y.Y + p.X.Y - r2);
                i++;
            }
        }
        else {
            if(i < n-1 && p.X.X - r[i].X >= r[i+1].X)
                pr.PB(MP(MP(p.X.X - r[i].X, r[i].X), MP(p.Y.X + r[i].X, p.Y.Y)));
            if(i < n-1 && p.X.Y - r[i].X >= r[i+1].X)
                pr.PB(MP(MP(p.X.X, p.X.Y - r[i].X), MP(p.Y.X, p.Y.Y + r[i].X)));
        }
    }
    return ret;
}

int main() {
    int tt;
    scanf("%d",&tt);
    FOR(cas, 1, tt) {
        int n, xx, yy;
        scanf("%d %d %d",&n,&xx,&yy);
        VI r(n);
        REP(i, n) scanf("%d",&r[i]);
        vector<PII> res = rob(n, xx, yy, r);
        printf("Case #%d:",cas);
        FORE(it, res) printf(" %d %d",it->X, it->Y);
        puts("");
    }
    return 0;
}
