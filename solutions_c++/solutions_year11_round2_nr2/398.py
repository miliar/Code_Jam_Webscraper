#define eps 1e-8
#define maxn 1000100
#include <iostream>
#include <stdio.h>
using namespace std;

double d;
int c, n, p[maxn], v, pos;

int dcmp(double x){return x<-eps?-1:x>eps;}

void init(){
    scanf("%d%lf", &c, &d);
    n = 0;
    for (int i=0; i<c; i++){
        scanf("%d%d", &pos, &v);
        for (int j=0; j<v; j++) p[n++] = pos;
    }
}

bool check(double t){
//    printf("check:%.2lf\n", t);
    double leftmost = (double)p[0] - t;
    for (int i=1; i<n; i++){
        double tg = leftmost + d;
        if (dcmp((double)p[i] + t - tg) < 0) return false;
        if (dcmp((double)p[i] - t - tg) >= 0) tg = p[i] - t;
        leftmost = tg;
    }
    return true;
}

void solve(int cas){
    double left = 0, right = d*2e6, ret=d*2e6;
    while (left <= right){
        double mid = (left + right) / 2;
        if (left + eps >= mid) break;
        if (mid + eps >= right) break;
        if (check(mid)) ret=mid, right=mid-eps;
        else left=mid+eps;
    }
    printf("Case #%d: %.7lf\n", cas, ret);
}

int main(){
    int test; scanf("%d", &test);
    for (int cas=1; cas<=test; cas++){
        init();
        solve(cas);
    }
    return 0;
}
