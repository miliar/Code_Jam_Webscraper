#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define FORQ(i,a,b) for (int i=(a);i<=(b);++i)
#define FORD(i,a,b) for (int i=(a)-1;i>=(b);--i)
#define FORE(i,x) for (__typeof__((x).begin()) i=(x).begin();i!=(x).end();++i)

#define PB push_back
#define MP make_pair
#define F first
#define S second

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef long  double K;

struct WW {
    K b,e,w;
    bool operator < (const WW & a) const {
        return b < a.b;
    }
};

struct CMP {
    bool operator () (const WW &a, const WW & b) const {
        return a.w < b.w; 
    }
};

int main() {
    int lw;
    scanf("%d",&lw);
    FOR(z,1,lw+1) {
        K res = 0.0;
        K x, s, r, t; int n;
        scanf("%Lf%Lf%Lf%Lf%d",&x,&s,&r,&t,&n);
        vector<WW> D;
        FOR(i,0,n) {
            WW w;
            scanf("%Lf%Lf%Lf",&w.b,&w.e,&w.w);
            D.PB(w);
        }
        sort(D.begin(), D.end());
        if (0 < D[0].b) {
            WW w;
            w.b = 0;
            w.e = D[0].b;
            w.w = 0;
            D.PB(w);

        }
        FOR(i,0,n-1) {
            if (D[i].e < D[i+1].b) {
                WW w;
                w.b = D[i].e;
                w.e = D[i+1].b;
                w.w = 0;
                D.PB(w);
            }
        }
        if (D[n-1].e < x) {
                WW w;
                w.b = D[n-1].e;
                w.e = x;
                w.w = 0;
                D.PB(w);
        }
        sort(D.begin(), D.end(), CMP());
        n = D.size();

        FOR(i,0,n) {
            K b,e,w;
            b = D[i].b; 
            e = D[i].e;
            w = D[i].w;
            K d = e-b;
            K nst = d / (r+w);
            if (nst <= t) {
                t -= nst;
                res += nst;
            } else {
                K nsd = (r+w) * t;
                d -= nsd;
                res += t;
                t = 0;
                K st = d / (s+w);
                res += st;
            }
        }
        printf("Case #%d: %.10Lf\n", z, res);
    }
    return 0;
}
