#include <stdio.h>
#include <algorithm>
using namespace std;

struct node{
       int b, e, w;
}p[2000];

int cmp(node a,node b) {
    return a.w < b.w;
}

int main () {
    int kase, i, len, sv, rv, n;
    double ti;
    int h = 1;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          int sum = 0;
          scanf("%d %d %d %lf %d", &len, &sv, &rv, &ti, &n);
          for (i = 0; i < n; i++) {
              scanf("%d %d %d", &p[i].b, &p[i].e, &p[i].w);
              sum += p[i].e-p[i].b;
          }
          p[i].b = 0;
          p[i].e = len-sum;
          p[i].w = 0;
          n++;
          double ans = 0;
          sort(p,p+n,cmp);
          for (i = 0; i < n; i++) {
              int sum = p[i].e-p[i].b;
              if (sum >= ti*(rv+p[i].w)) {
                 ans += ti+(sum-ti*(rv+p[i].w))/(sv+p[i].w);
                 ti = 0;
              }
              else{
                 ans += sum*1.0/(rv+p[i].w);
                 ti -= sum*1.0/(rv+p[i].w);
              }
          
          }
          printf("Case #%d: %.8f\n",h++, ans);
    }
    return 0;
}
