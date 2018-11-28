#include<algorithm>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<vector>
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) for(int i=0;i<(n);++i)
#define fup FOR
#define fdo FORD
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define SIZE(x) ((int)(x).size())
#define siz SIZE
#define CLR memset((x),0,sizeof (x))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SQR(a) ((a)*(a))

#define DEBUG 0
#define debug(x) {if(DEBUG) cerr << #x << " = " << x << endl;}
#define debugv(x) {if(DEBUG) {cerr << #x << " = "; FORE(it,(x)) cerr << *it << " . "; cerr  <<endl;}}

using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef VI vi;
typedef LL lli;

const int inf = 1000000000;
const LD EPS  = 1e-9;


void solve(int tcase) {
    printf("Case #%d:\n", tcase);
    int w,l,u,g;
    scanf("%d%d%d%d", &w, &l, &u, &g);
    vector<pair<LD, LD> > U;
    vector<pair<LD, LD> > L;
    REP(i, l) {
        int x,y;
        scanf("%d%d", &x, &y);
        L.PB(MP(x,y));
    }
    REP(i, u) {
        int x,y;
        scanf("%d%d", &x, &y);
        U.PB(MP(x,y));
    }
    long double ar = 0;
    REP(i, u-1) {
        ar += (U[i+1].FI - U[i].FI)*(U[i].SE+U[i+1].SE)/2;
    }
    REP(i, l-1) {
        ar -= (L[i+1].FI - L[i].FI)*(L[i].SE+L[i+1].SE)/2;
    }
    long double rem = ar/g;
    long double h = U[0].SE - L[0].SE;
    long double delta;
    long double x = 0;

    int i = 0;
    int j = 0;
    int cnt = 0;
    while(i < u-1 && j < l-1) {
        delta = (U[i+1].SE-U[i].SE)/(U[i+1].FI - U[i].FI) - (L[j+1].SE-L[j].SE)/(L[j+1].FI-L[j].FI);
        debug(rem); 
        debug(delta); 
       LD nw;
       if (abs(delta) > EPS) {
           if (h*h+2*rem*delta < EPS) nw = w+1; 
           else {
               nw = (-h + sqrt(h*h+2*rem*delta))/(delta);
           }
           if (nw < 0) nw = w+1;
       } else {
           nw = rem / h;
       }
       debug(nw); 
       if (nw+x > U[i+1].FI-EPS || nw+x > L[j+1].FI-EPS) {
           LD nnw = min(U[i+1].FI, L[j+1].FI)-x;
           rem -= (2*h+delta*nnw)*nnw/2;
           h  += delta*nnw;
           if (U[i+1].FI < x+nnw +EPS) ++i;
           if (L[j+1].FI < x+nnw +EPS) ++j;
           x += nnw;
       } else {

           ++cnt;
           if (cnt < g+1) printf("%.9Lf\n", x+nw);
           x += nw;
           h += delta*nw;
           rem = ar/g;
       }
    }


}

int main() {
    int t;
    scanf("%d", &t);
    REP(i, t) solve(i+1);
    return 0;
}
