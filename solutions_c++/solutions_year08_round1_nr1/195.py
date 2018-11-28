#include <stdio.h>
#include <stdlib.h>

const int maxn = 800;

int n;
int x[maxn], y[maxn];

int
cmp_int(const void *a, const void *b)
{
  return *(const int *)a - *(const int *)b;
}

int
rcmp_int(const void *a, const void *b)
{
  return *(const int *)b - *(const int *)a;
}

void
run(int irun)
{
  scanf("%d", &n);
  for (int i = 0; i < n; i++)
    scanf("%d", &x[i]);
  for (int i = 0; i < n; i++)
    scanf("%d", &y[i]);

  qsort(x, n, sizeof(x[0]), cmp_int);
  qsort(y, n, sizeof(x[0]), rcmp_int);

  long long t = 0;
  for (int i = 0; i < n; i++)
    t += (long long)x[i] * (long long)y[i];

  printf("Case #%d: %lld\n", irun, t);
}

int
main()
{
  int N;
  scanf("%d", &N);
  for (int i = 1; i <= N; i++)
    run(i);
  return 0;
}
