#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

#define MAX 128
int v[MAX];

int main(void)
{
  int caso, T;

  for(scanf("%d", &T), caso = 1; caso <= T; caso++)
  {
    int r, N, L, H;

    scanf("%d %d %d", &N, &L, &H);
    for(int i = 0; i < N; i++)
      scanf("%d", v+i);

    r = -1;
    for(int i = L; i <= H && r < 0; i++)
    {
      bool ok = true;
      for(int j = 0; j < N && ok; j++)
        if (i < v[j] && (v[j] % i) != 0)
          ok = false;
        else if (i > v[j] && (i % v[j]) != 0)
          ok = false;
      if (ok)
        r = i;
    }

    printf("Case #%d: ", caso);
    if (r < 0) printf("NO\n");
    else printf("%d\n", r);
  }

  return(0);
}

