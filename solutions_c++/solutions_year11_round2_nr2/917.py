#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX 256

int C,D,P[MAX],V[MAX],t;

int pode(double r)
{
  double p;
  for(int i = 0; i < C; i++)
  {
    if (i > 0 && p > (double)P[i]+r)
      return(0);

    if (i == 0 || (double)P[i]-r >= p+(double)D)
      p = (double)P[i]-r+(double)(D*(V[i]-1));
    else
      p += (double)D*(double)V[i];
    if (p > (double)P[i]+r)
      return(0);
  }

  return(1);
}

int main(void)
{
  int caso, T;

  for(scanf("%d", &T), caso = 1; caso <= T; caso++)
  {
    double r;

    scanf("%d %d", &C, &D);
    t = 0;
    for(int i = 0; i < C; i++)
    {
      scanf("%d %d", P+i, V+i);
      t += V[i];
    }

    double left = 0.0;
    double right = 1e9;
    while(1)
    {
      r = (left+right)/2;
      if (right-left < 1e-10) break;

      if (pode(r)) right = r;
      else left = r;
    }
    printf("Case #%d: %.10lf\n", caso, r);
  }

  return(0);
}

