#include <stdio.h>
int T;
int N;
int m;
int s;
int xs;

int main() {
  scanf("%d", &T);
  for (int TT=1;TT<=T;++TT) {
    scanf("%d", &N);
    m = 1<<30;
    s = xs = 0;
    int next;
    for (int i=0;i<N;++i) {
      scanf("%d", &next);
      xs ^= next;
      s += next;
      if (next < m)
	m = next;
    }
    if (xs) {
      printf("Case #%d: NO\n", TT);
    } else {
      printf("Case #%d: %d\n", TT, s-m);
    }
  }
  return 0;
}
