#include <cstdio>
using namespace std;

double gmemo[1005];
double fmemo[1005];
double co[20];

double g(int n) {
    if(n <= 1) return 0;
    if(n == 2) return 0.5d;
    if(gmemo[n] != 0.0d) return gmemo[n];
    return gmemo[n] = ((n-1)*g(n-1)+g(n-2))/n;
}

double f(int n) {
    if(n == 1) return 0;
    if(n == 2) return 2;
    if(fmemo[n] != 0.0d) return fmemo[n];

    double ret = 1.0d;
    for(int k=0; k<n; ++k) {
        if(n-k >= 20) continue;
        ret += g(k)*f(k)/co[n-k];
    }
//    printf("%d %.6lf %.6lf\n", n, ret, g(n));
    return fmemo[n] = ret/(1-g(n));
}

int in[1005];

int main() {
    for(int i=0; i<1005; ++i) gmemo[i] = fmemo[i] = 0.0d;
    co[1] = 1.0d;
    for(int i=2; i<20; ++i) co[i] = co[i-1]*i;

    int t,n;
    scanf("%d", &t);
    for(int tc=1; tc<=t; ++tc) {
        scanf("%d", &n);
        int k = 0;
        for(int i=0; i<n; ++i) {
            scanf("%d", &in[i]);
            if(in[i] != i+1) k++;
        }
        printf("Case #%d: %.6lf\n", tc, (k==0)?0.0d:f(k));
    }
}
