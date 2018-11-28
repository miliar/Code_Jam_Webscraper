#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
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

inline double GD() { double x; scanf("%lf",&x); return x; }
inline int GI() { int x; scanf("%d",&x); return x; }
inline LL GL() { LL x; scanf("%lld",&x); return x; }
inline char GC() { char x[2]; scanf("%s",x); return x[0]; }
inline void GS(char *x) { scanf("%s",x); }

void single_case(int case_number) {
    double X = GD();
    double S = GD();
    double R = GD();
    double T = GD();
    int n = GI();
   
    vector<pair<double, double> > V;
    
    double Y = X;

    REP(i,n) {
        double B = GD();
        double E = GD();
        double W = GD();
        Y -= (E-B);
        V.pb(mp(W+S,(E-B)));
    }
    V.pb(mp(S,Y));

    sort(ALL(V));

    double TIM = 0.0;

    R -= S;

    FOREACH(i,V) {
        double W = i->first;
        double L = i->second;
        double dt = min(T, L/(W+R));
        T -= dt;
        TIM += (dt + (L-(W+R)*dt)/W);
    }
        

    printf("Case #%d: %.9lf\n",case_number,TIM);
    //printf("Case #%d:\n",case_number);
}

int main() {
    int j;
    scanf("%d",&j);
    REP(i,j) single_case(i+1);
    return 0;
}


