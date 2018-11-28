#include <cstdio>

int main() {
  int t,n,k;
  scanf("%d",&t);
  for (int i=1; i<=t; ++i) {
    scanf("%d%d",&n,&k);
    bool on = true;
    for (int j=0; j<n; ++j) {
      if (!(k&1)) on = false;
      k >>= 1;
    }
    printf("Case #%d: %s\n",i,on?"ON":"OFF");
  }
  return 0;
}
