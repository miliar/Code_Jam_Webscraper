#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
//#include <cmath>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <ctime>
#include <utility>
using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<long> VL;
typedef vector<string> VS;
typedef pair<int,int> PII;

#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define ALL(c) (c).begin(),(c).end()
#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(b); --i)

#define pb push_back
#define mp make_pair
#define st first
#define nd second

LL gcd(LL a, LL b) { return b?gcd(b,a%b):a; }
int bc(LL x) { return x?bc(x>>1)+(x&1):0; }

inline int rnd(int n) { return rand()%n; }

inline double gd() { double x; scanf("%lf",&x); return x; }
inline int gi() { int x; scanf("%d",&x); return x; }
inline LL gl() { LL x; scanf("%lld",&x); return x; }
inline LD gld() { LD x; scanf("%llf",&x); return x; }
inline char gc() { char x[2]; scanf("%s",x); return x[0]; }
inline void gs(char *x) { scanf("%s",x); }

int l,u,g,n;
double w;
double lx[1000],ly[1000],ux[1000],uy[1000],x[1000],y1[1000],y2[1000],y[1000];
double area[1000], AREA=0;

double bs(int i, double ar) {
//    printf("bs %d %lf\n",i,ar);
    double L=x[i],R=x[i+1];
    while (R-L>1e-8) {
        double M = (L+R)*0.5;
        double tmp = (x[i+1]-M)*(((y[i]*(x[i+1]-M)+y[i+1]*(M-x[i]))/(x[i+1]-x[i]))+y[i+1]);
  //      printf("M = %lf tmp = %lf ar = %lf\n",M,tmp,ar);
        if (tmp < ar)
            R = M;
        else
            L = M;
    }
    return (L+R)*0.5;
}

void single_case(int case_number) {
    AREA = 0.0;

    w = gd();
    l = gi();
    u = gi();
    g = gi();

    REP(i,l) { lx[i] = gd(); ly[i] = gd(); x[i]=lx[i]; }
    REP(i,u) { ux[i] = gd(); uy[i] = gd(); x[i+l] = ux[i]; }

    n = l+u;
    sort(x,x+n);
    n = unique(x,x+n)-x;
    REP(i,n) {
        int j = 0;
        while(lx[j]<x[i]) j++;
        if (lx[j]==x[i]) { y1[i] = ly[j]; continue; }
        y1[i] = (ly[j-1]*(lx[j]-x[i])+ly[j]*(x[i]-lx[j-1]))/(lx[j]-lx[j-1]);
    }
    REP(i,n) {
        int j = 0;
        while(ux[j]<x[i]) j++;
        if (ux[j]==x[i]) { y2[i] = uy[j]; continue; }
        y2[i] = (uy[j-1]*(ux[j]-x[i])+uy[j]*(x[i]-ux[j-1]))/(ux[j]-ux[j-1]);
    }
    REP(i,n-1) {
        area[i] = (y2[i]-y1[i]+y2[i+1]-y1[i+1])*(x[i+1]-x[i]);
        AREA += area[i];
    }
    REP(i,n) y[i] = y2[i]-y1[i];

    //REP(i,n) printf("%lf %lf\n",x[i],y[i]);
    //REP(i,n-1) printf("%lf\n",area[i]);

    printf("Case #%d:\n",case_number);

    AREA /= (double)g;
    int it=0;
    //printf("g=%d\n",g);
    //printf("AREA = %lf\n",AREA);
    REP(i, g-1) {
        double off = 0.0;
        while (off<AREA) {
            off += area[it];
            it++;
        }
        it--;
        off -= area[it];
        double res = bs(it, area[it] - (AREA - off));
        y[it] = (y[it]*(x[it+1]-res)+y[it+1]*(res-x[it]))/(x[it+1]-x[it]);
        x[it] = res;
        area[it] -= (AREA - off);
        printf("%0.7lf\n",res);
    }


        

}

int main() {
    int j;
    scanf("%d",&j);
    REP(i,j) single_case(i+1);
    return 0;
}


