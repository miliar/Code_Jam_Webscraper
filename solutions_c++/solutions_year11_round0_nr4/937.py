#include <stdio.h>

int main() {

  int T;
  scanf("%d", &T);
  for(int i = 0; i < T; ++i) {
    int n;
    scanf("%d", &n);
    int ans = n;
    for(int j = 0; j < n; ++j) {
      int v;
      scanf("%d", &v);
      if(v == 1+j) --ans;
    }
    printf("Case #%d: %d.000000\n", 1+i, ans);
  }

  return(0);
}
