#include <stdio.h>

int gcd(int a, int b) {
  while (a != b && a && b) {
    if (a > b)
      a %= b;
    else
      b %= a;
  }
  if (!a)
    return b;
  return a;
}

int main() {
  int T;
  scanf("%d", &T);
  int pa, pb;
  long long n;
  for (int TT=1;TT<=T;++TT) {
    scanf("%lld %d %d", &n, &pa, &pb);
    int g = gcd(pa, 100);
    int d = 100/g;
    if (n < d || (pa > 0 && pb == 0) || (pa < 100 && pb == 100))
      printf("Case #%d: Broken\n", TT);
    else
      printf("Case #%d: Possible\n", TT);
  }
  return 0;
}
