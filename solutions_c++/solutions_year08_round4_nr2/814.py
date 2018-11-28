#include <stdio.h>

const int maxprod = 1e8;

int a;
int n, m, maxp;
short x[maxprod+1];
short y[maxprod+1];

void
run(int irun)
{
  int i, j, p;
  int i2, j2;

  scanf("%d %d %d", &n, &m, &a);
  maxp = n*m;
  
  for (p = 0; p <= maxp; p++)
    x[p] = -1;

  x[0] = y[0] = 0;
  i2 = -1;
  for (i = 1; i <= n; i++)
    for (j = 1; j <= m; j++) {
      p = i*j;
      //printf("%d %d gives %d\n", i, j, p);
      x[p] = i;
      y[p] = j;
      if (p-a >= 0 && x[p-a] >= 0) {
        i2 = x[p-a];
        j2 = y[p-a];
        goto end;
      }
      if (p+a <= maxp && x[p+a] >= 0) {
        i2 = x[p+a];
        j2 = y[p+a];
        goto end;
      }
    }
 end:
  if (i2 == -1)
    printf("Case #%d: IMPOSSIBLE\n", irun);
  else
    printf("Case #%d: 0 0 %d %d %d %d\n", irun, i, j2, i2, j);
}

int
main()
{
  int nrun;
  scanf("%d", &nrun);
  for (int i = 1; i <= nrun; i++)
    run(i);
  return 0;
}
