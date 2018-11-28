#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>
using namespace std;

#define maxn 1007

int n;
int a[maxn];
int times;
int m, x, y;
double ans;
double f[maxn], p[maxn], e[maxn];

void prepare()
{
    f[1] = p[1] = 0;
    f[2] = p[2] = 2;
    e[2] = 0.5; e[1] = 0; e[0] = 0.5;
    for (int i = 3; i <= 1000; ++i) {
      e[i] = 1/double(i);
      for (int j = i-1; j >= 0; --j)
        e[j] /= i-j;
      p[i] = e[i];
      for (int j = i-1; j >= 0; --j)
        p[i] += e[j]*(p[j]+1);
      p[i] *=  double(i)/double(i-1);
      f[i] = p[i];
      for (int j = i-1; j >= 2; --j)
        if (p[j]+f[i-j+1] < f[i]) 
          f[i] = p[j]+f[i-j+1];
    }
}

int main()
{
    freopen("D1.in","r",stdin);
    freopen("D.out","w",stdout);
    
   // prepare();
    
    scanf("%d",&times);
    for (int k = 1; k <= times; ++k) {
      printf("Case #%d: ",k);
      ans = 0;
      scanf("%d",&n);
      for (int i = 1; i <= n; ++i) 
        scanf("%d",&a[i]);
      for (int i = 1; i <= n; ++i) if (a[i]){
        m = 0; x = i;
        while (a[x]) {
          y = a[x]; a[x] = 0; x = y;
          ++m;
        }
        if (m > 1) ans += m;
      }
      printf("%.6lf",ans);
      printf("\n");
    }
    return 0;
}
