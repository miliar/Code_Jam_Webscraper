
#include <cstdio>

int solve () {
  int n;
  int min = -1;
  int sum = 0;
  int sum_a = 0;

  scanf ("%d", &n);

  for (int i = 0; i < n; i++) {
    int tmp;
    scanf ("%d", &tmp);

    if (min < 0 || tmp < min)
      min = tmp;

    sum += tmp;
    sum_a ^= tmp;
  }

  if (sum_a == 0)
    printf ("%d\n", sum - min);
  else 
    printf ("NO\n");

  return 0;
}

int main() {

  int TC;
  scanf ("%d", &TC);

  for (int tc = 1; tc <= TC; tc++) {
    printf ("Case #%d: ", tc);
    solve ();
  }

  return 0;
}
