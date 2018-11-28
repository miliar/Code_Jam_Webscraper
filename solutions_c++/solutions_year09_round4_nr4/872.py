#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int n;
int x[5], y[5], r[5];

void readin(){
    scanf("%d", &n);
    for(int i=0; i<n; ++i){
        scanf("%d%d%d", &x[i], &y[i], &r[i]);
    }
}

inline double sqr(double x){return x*x;}
double dis(int x1,int y1,int x2,int y2){
    return sqrt(sqr(x1-x2) + sqr(y1-y2));
}

void solve(){
    if(n == 1){
        printf("%d\n", r[0]);
        return;
    }else if(n == 2){
        printf("%d\n", max(r[0], r[1]));
        return;
    }
    
    double res = 1e100;
    double r1,r2;
    int xx[3],yy[3],rr[3],d2;
    
    for(int i=0; i<3; ++i){
        r1 = r[i];d2 = 0;
        for(int j=0; j<3; ++j){
            if(i != j){
                rr[d2] = r[j];
                xx[d2] = x[j];
                yy[d2] = y[j];
                ++d2;
            }
        }
        r2 = dis(xx[0], yy[0], xx[1], yy[1]) + rr[0] + rr[1];
        r2 /= 2.0;
        res = min(res, max(r1,r2));
    }
    printf("%.6f\n", res);
}

int main(){
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; ++i){
        readin();
        printf("Case #%d: ", i);
        solve();
    }
}
