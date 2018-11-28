#include <stdio.h>
#include <string.h>
#include <math.h>

int C, N, M, i,j,A;
float dist(int i, int j)
{
  int ix = i/M;
  int iy = i%M;
  int jx = j/M;
  int jy = j%M;

  float dx = jx-ix;
  float dy = jy-iy;
  dx *= dx;
  dy *= dy;

  return sqrt(dx+dy);
};

int main()
{

  scanf("%d", &C);

  for (int cs=1 ; cs<=C; cs++)
  {
    scanf("%d %d %d", &N, &M, &A);
    N++;
    M++;
    int ttl = N*M;
    if (N*M < A)
    {
      printf("Case #%d: IMPOSSIBLE\n", cs);
      continue;
    }

    for (i=0;i<ttl;i++)
    {
      for (j=0; j<ttl; j++)
      {
        double a = dist(0, i);
        double b = dist(0, j);
        double c = dist(i, j);
        double s = (a+b+c)/2.0;

        double area = sqrt(s*(s-a)*(s-b)*(s-c));
        //int bob = (area*2.0 + 0.0001);
        if (((int)(area*2.0+0.50)) == A)
          break;
      }
      if (j != ttl) break;
    }

    if (i == ttl)
      printf("Case #%d: IMPOSSIBLE\n", cs);
    else
      printf("Case #%d: 0 0 %d %d %d %d\n", cs, (i/M), (i%M), (j/M), (j%M));
  }

  return 0;
}
