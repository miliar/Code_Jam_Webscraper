#include <stdio.h>

int T;
int N;

int main() {
  scanf("%d", &T);

  for (int TT=1;TT<=T;++TT) {
    int cur;
    scanf("%d", &N);
    int ans = N;
    for (int i=1;i<=N;++i) {
      scanf("%d", &cur);
      if (cur == i) --ans;
    }
    printf("Case #%d: %lf\n", TT, (double)ans);
  }
  return 0;
}
