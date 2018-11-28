#include <iostream>
#include <vector>
#include <string.h>
#include <queue>
#include <cmath>
#include <map>
#include <algorithm>
using namespace std;
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int _; scanf("%d", &_); _;})
#define sz size()
#define pb push_back
#define mkp make_pair
#define INF 1e8
#define MAX 27
typedef vector<int> VI;
typedef double D;



inline double dist(int x1, int y1, int x2, int y2) {
    return sqrt((D)((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)));
}
#define eps 1e-9

int main() {
    int kases = GI;
    FOR(kase,1,kases+1) {
        int n = GI, mn = INF, x[n], y[n], r[n];
        REP(i,n) {
            x[i] = GI, y[i] = GI, r[i] = GI;
            mn = min(r[i], mn);
        }
        D ansr = 1e100;
        
        REP(i,n) REP(j,i) {
            double xd = ((D)x[i] + x[j]) / 2, yd = ((D)y[i] + y[j]) / 2;
            double rr = (dist(x[i],y[i],x[j],y[j]) + r[i] + r[j]) / 2.;
            REP(k,n) if(k != i && k != j) {
                if(r[k] - rr > eps) rr = r[k];
            }            
            if(ansr - rr > eps) ansr = rr;
//            cout << i <<" and " << j << endl;
//            cout << rr << endl;
        }
        if(n == 1) ansr = r[0];
        if(n == 2) ansr = max(r[0], r[1]);
        printf("Case #%d: %.7lf\n", kase, ansr);
    }


}
