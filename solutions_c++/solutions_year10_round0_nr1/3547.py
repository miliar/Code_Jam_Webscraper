#include <stdio.h>

int main()
{
  int T, N, K, M;
  scanf("%d", &T);
  for (int i = 1; i <= T; ++i)
  {
    scanf("%d%d", &N, &K);
    M = 1 << N;
    if ((K%M) == (M-1))
      printf("Case #%d: ON\n", i);
    else
      printf("Case #%d: OFF\n", i);
  }
  return 0;
}
