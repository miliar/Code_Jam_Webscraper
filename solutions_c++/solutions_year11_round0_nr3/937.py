#include <cstdio>
#include <vector>

using namespace std;

int main () {
  int T, N;
  scanf("%d", &T);
  
  for (int t = 1; t <= T; t++) {
    int x = 0, s = 0, m = 10000000, n;
    scanf ("%d", &N);
    for (int i = 0; i < N; i++) {
      scanf("%d", &n);
      x ^= n;
      s += n;
      if (n < m)
        m = n;
    }
    printf ("Case #%d: ", t);
    if (x != 0)
      printf ("NO\n");
    else
      printf ("%d\n", s-m);
  }
  return 0;
}
