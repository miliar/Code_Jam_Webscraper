#define maxn 1010
#define eps 1e-8
#include <math.h>
#include <algorithm>
#include <stdio.h>
#include <iostream>
using namespace std;

double x, s, r, t;
double b[maxn], e[maxn], w[maxn];
int n, id[maxn];

int dcmp(double x){
    return x<-eps?-1:x>eps;
}

bool cmp(int i, int j){
    return dcmp(b[i]-b[j])<0;
}

bool cmp2(int i, int j){
    return dcmp(w[i]-w[j])<0;
}

void init(){
    scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &n);
    for (int i=0; i<n; i++)
        scanf("%lf%lf%lf", &b[i], &e[i], &w[i]), id[i] = i;
    sort(id, id+n, cmp);
}

double run(double d, double v){
    double ret = 0.0;
    if (dcmp(d)==0) return ret;
    double nt = d/(r+v);
    if (dcmp(t-nt)>=0) {
        t-=nt;
        if (dcmp(t)==0) t=0.0;
        ret = nt;
    } else {
        if (dcmp(t)!=0)
        d -= (r+v) * t;
        nt = t + d / (s+v);
        t = 0.0;
        ret = nt;
    }
    return ret;
}

void solve(int cas){
    double l = 0.0, ret = 0.0;
    for (int i=0; i<n; i++){
        ret += run(b[id[i]] - l, 0);
//        ret += work(e[id[i]] - b[id[i]], w[id[i]]);
        l = e[id[i]];
    }
    ret += run(x-e[id[n-1]], 0);
    sort(id, id+n, cmp2);
    for (int i=0; i<n; i++){
        ret += run(e[id[i]]-b[id[i]], w[id[i]]);
    }
    printf("Case #%d: %.9lf\n", cas, ret);
}

int main(){
    int test; scanf("%d" ,&test);
    for (int cas=1; cas<=test; cas++){
        init();
        solve(cas);
    }
    return 0;
}
