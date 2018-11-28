#include <stdio.h>

int main (void) {
 int cases, n, cur;
 scanf("%d", &cases);
 for (int caseX = 1; caseX <= cases; ++caseX) {
  int test = 0, sum = 0, min = 1000000;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
    scanf("%d", &cur);
    test = test ^ cur;
    sum += cur;
    if (cur < min)
      min = cur;
  }
  printf("Case #%d: ", caseX);
  if (test != 0)
    printf("NO\n");
  else
    printf("%d\n", sum - min);
 }
 return 0;
}
