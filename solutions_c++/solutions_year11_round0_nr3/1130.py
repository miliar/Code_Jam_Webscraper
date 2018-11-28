#include <stdio.h>
int v[1005];
int main() {
  int casn;
  scanf("%d", &casn);
  for(int cas=1; cas<=casn; ++cas) {
    int n, sum_t=0, mi=1000000000;
    scanf("%d", &n);
    for(int i=0; i<n; ++i) {
      scanf("%d", v+i);
      sum_t+=v[i];
      if(mi>v[i]) mi=v[i];
    }
    
    for(int k=0; k<=30; ++k) {
      int cnt=0;
      for(int i=0; i<n; ++i) cnt += (v[i]&(1<<k))>0;
      if(cnt&1) goto fail;
    }
    
    printf("Case #%d: %d\n", cas, sum_t-mi);
    continue;
    fail:;
    printf("Case #%d: NO\n", cas);
  }
  return 0;
}

