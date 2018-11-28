#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

#include <cstdlib>
#include <ctime>
#include <cctype>
#include<string.h>
using namespace std;

#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))

#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second
#define bc __builtin_popcount
typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;
typedef long long LL;


double p[200], v[200];
int C, D;
int chk(){
    REP(i, C) if (v[i]>1) return 0;
    FOR(i,1,C){
        if (p[i]-p[i-1]<D) return 0;
    }
    return 1;
}

double solve(double x){
    double cp = p[0]-x;
    REP(i, C){
        int n = v[i];
        while (n--){
            if (fabs(p[i]-cp)>x+1e-9) return 0;
            cp += D;
        }
        if (i<C-1){
            cp = max(cp, p[i+1]-x);
        }
    }
    return 1;
}



int main()
{
    freopen("in.txt", "r", stdin);
    freopen("o.txt", "w", stdout);
    int T=SS;
    FOR(t,1,T+1){
        cout<<"Case #"<<t<<": ";
        C = SS; D = SS;
        REP(i, C){
            p[i] = SS;
            v[i] = SS;
        }
        double ans = 0.0;
        if (chk()){
            ans = 0.0;
        }
        else{
            double u=1000000.0*1000000.0, l = 0.0;
            while (fabs(u-l)>1e-9){
                double mid = (u+l)/2.0;
                if (solve(mid)){
                    u =mid;
                }
                else{
                    l=mid;
                }
            }
            ans = u;
        }
        printf("%.8lf\n", ans);
    }
    return 0;
}
