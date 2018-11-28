#include <stdio.h>
#include <algorithm>

int a[10000];
int tot, sum, mi, tc, n;

int main()
{
  scanf("%d", &tc);
  for (int tt = 1; tt <= tc; tt++)
  {
    scanf("%d", &n);
    int tot = 0;
    int mi = 10000000;
    int sum = 0;
    for (int i = 0; i < n; i++) {
      scanf("%d", &a[i]);
      tot ^= a[i];
      sum += a[i];
      mi = std::min(mi, a[i]);
    }
    printf("Case #%d: ", tt);
    if (tot != 0) {
      printf ("NO\n");
    } else {
      printf ("%d\n", sum - mi);
    }
  }
  return 0;
}
