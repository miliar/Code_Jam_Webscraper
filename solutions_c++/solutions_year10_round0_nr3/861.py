#include <cstdio>
const int N = 1001;
long long v[N];
int w[N];
int g[N];
int main() {
  int t,r,k,n;
  scanf("%d",&t);
  for (int i=1; i<=t; ++i) {
    scanf("%d%d%d",&r,&k,&n); 
    for (int j=0; j<n; ++j) {
      scanf("%d",g+j);
      v[j] = 0;
      w[j] = -1;
    }
    long long ret = 0;
    int d = 0;
    v[0] = 0;
    w[0] = 0;
    bool ok = true;
    for (int j=1; j<=r; ++j) {
      int dr = 0;
      for (int l=0;l<n;++l) {
        dr += g[d];
        if (dr > k) {
          dr -= g[d];
          break;
        }
        if (++d == n) {
          d = 0;
        }
      }
      ret += dr;
      if (ok && w[d] >= 0) {
        long long dv = ret - v[d];
        int dw = j - w[d];
        ret += ((r-j)/dw)*dv;
        j += dw*((r-j)/dw);
        ok = false;
      } else {
        w[d] = j;
        v[d] = ret;
      }
    }
    printf("Case #%d: %lld\n",i,ret);
  }
  return 0;
}
