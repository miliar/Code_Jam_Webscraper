#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

#define REP(i, n) for ( int i = 0; i < (n); i++ ) 
#define FOR(i, a, b) for ( int i = (a); i < (b); i++ ) 

using namespace std;

const int MAX_N = 5;

int n;
int x[MAX_N];
int y[MAX_N];
int r[MAX_N];

void fun(int cs) {
    scanf("%d", &n);
    REP(i, n) scanf("%d %d %d", &x[i], &y[i], &r[i]);

    double max_rad = r[0];
    REP(i, n) max_rad = max(max_rad, double(r[i]));

    double res;
    if ( n == 1 ) res = max_rad;
    else if ( n == 2 ) res = max_rad;
    else {
        double best = 999999999999999.0;
        REP(i, n) FOR(j, i+1, n) {
            double t = sqrt( double(x[i]-x[j]) * double(x[i]-x[j]) + double(y[i]-y[j]) * double(y[i]-y[j]) );
//            printf("%d %d\n", x[i]-x[j], y[i]-y[j]);
            t += r[i] + r[j];
            best = min(t, best);
        }
        res = max(max_rad, best/2);
    }


    printf("Case #%d: %.6lf\n", cs, res);
}

int main() {
    int T;
    scanf("%d", &T);
    REP(i, T) fun(i+1);

    return 0;
}
