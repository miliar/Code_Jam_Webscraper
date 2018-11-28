#include <stdio.h>

int min (int a, int b)
{
  return (a < b) ? a : b;
}

int num, sup;

void calc(int N, int p)
{
  if (p == 0)
  {
    num++;
    return;
  }
  if (p == 1 || N == 0)
  {
    if (N != 0)
      num++;
    return;
  }
  if (N / (p - 1) >= 3)
  {
    if (N % 3 != 0 || N / p >= 3)
    {
      num++;
    }
    else
      sup++;
    return;
  }
  if (N % 3 == 2 && (p <= 2 || N / (p - 2) >= 3))
      sup++;
}

int main()
{
  int i, t, N, S, P, j, val;
  scanf("%d", &t);
  for (i = 0; i < t; i++)
  {
    scanf("%d %d %d", &N, &S, &P);
    num = 0;
    sup = 0;
    for (j = 0; j < N; j++)
    {
      scanf("%d", &val);
      calc(val, P);
    }
    printf("Case #%d: %d\n", i + 1, num + min(sup, S));
  }

  return 0;
}

