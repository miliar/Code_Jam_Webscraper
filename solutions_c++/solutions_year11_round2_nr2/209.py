#include <stdio.h>
#include <algorithm>
#include <numeric>
using namespace std;
#define rep(i, n) for(int i=0; i<(int)(n); i++)

int n, p[300], v[300];
double D;

bool can(double t) {
    double s = -1e100;
    rep(i, n) {
        const double w = D*(v[i]-1);
        const double b = max(s+D, p[i]-t);
        if(b+w>p[i]+t) return false;
        s = b + w;
    }
    return true;
}

int main() {
    int T;
    scanf("%d", &T);
    rep(_t, T) {
        scanf("%d %lf", &n, &D);
        rep(i, n) scanf("%d%d", p+i, v+i);
        double l=0, r=accumulate(v, v+n, 0)*D;
        rep(i, 100000) {
            double mid = (l+r)/2;
            if(can(mid)) r = mid;
            else l = mid;
        }
        printf("Case #%d: %.8f\n", _t+1, r);
    }
    return 0;
}
