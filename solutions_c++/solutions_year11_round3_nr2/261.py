#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long huge;

#define MAX 1000100
huge d[MAX], menor[MAX];

int main(void)
{
  int caso, T;

  for(scanf("%d", &T), caso = 1; caso <= T; caso++)
  {
    huge r, L, t, N, C;

    scanf("%lld %lld %lld %lld", &L, &t, &N, &C);
    for(int i = 0; i < C; i++)
      scanf("%lld", d+i);
    t *= 2;

    menor[0] = 4*d[0];
    for(int i = 1; i < N; i++)
      menor[i] = menor[i-1] + 4*d[i%C];
    int mb = -1;
    for(int i = 0; i < N; i++)
      if (t >= menor[i])
        mb = i;
    mb++;
    vector<huge> v;
    for(int i = mb+1; i < N; i++)
      v.push_back(d[i%C]);
    sort(v.rbegin(), v.rend());

    r = menor[N-1];

    for(int i = 0; i < L-1 && i < (int)v.size(); i++)
      r -= 2*v[i];

    if (L > 0)
    {
      if ((int)v.size() < L)
      {
        if (mb < N)
          r -= (menor[mb]-t)/2;
      }
      else
        r -= max((menor[mb]-t)/2, 2*v[L-1]);
    }

    printf("Case #%d: %lld\n", caso, r/2);
  }

  return(0);
}

