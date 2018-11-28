#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

#define maxn 1000007

int n, s, r, t, m;
int a[maxn];
int ll, rr, ww;
int cases;
double ans;
double w, z;
bool f;

int main()
{
    freopen("A1.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&cases);
    for (int k = 1;k <= cases; ++k) {
      printf("Case #%d: ",k);
      scanf("%d",&n);
      scanf("%d%d%d%d",&s,&r,&t,&m);
      for (int i = 1; i <= n; ++i)
        a[i] = s;
      for (int i = 1; i <= m; ++i) {
        scanf("%d%d%d",&ll,&rr,&ww);
        for (int j = ll+1; j <= rr; ++j) 
          a[j] += ww;
      }
      sort(a+1,a+(1+n));
      ans = 0; f = true;
      for (int i = 1; i <= n; ++i){
        if (f) {
          w = a[i]+(r-s);
          z = a[i];
          ans += 1.00/w;
          if (ans > t) {
            f = false;
            ans = t+(ans-t)*w/z;
          }
        }
        else {
           w = a[i];
           ans += 1.00/w;
        }
      } 
      printf("%.6lf",ans);
      printf("\n");
    }
}
