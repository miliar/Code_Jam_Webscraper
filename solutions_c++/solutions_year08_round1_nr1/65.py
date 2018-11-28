#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
long long x[820], y[820];

int main(){
  freopen("a.in", "r", stdin);
  freopen("a.out", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    scanf("%d", &n);
    int i;
    for (i=0; i<n; i++){
      scanf("%lld", &x[i]);
    }
    for (i=0; i<n; i++){
      scanf("%lld", &y[i]);
    }
    sort(x, x+n);
    sort(y, y+n);
    long long ans = 0;
    for (i=0; i<n; i++) ans += x[i] * y[n-1-i];
    printf("Case #%d: %lld\n", t, ans);
  }
  return 0;
}