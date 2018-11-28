#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long huge;

int main(void)
{
  int caso, T;

  for(scanf("%d", &T), caso = 1; caso <= T; caso++)
  {
    bool ok = true;
    huge N, Pd, Pg;

    scanf("%lld %lld %lld", &N, &Pd, &Pg);

    if (Pd > 0 && Pg == 0) ok = false;
    else if (Pd < 100 && Pg == 100) ok = false;
    else if (N < 100)
    {
      ok = false;
      for(huge i = 1; i <= N; i++)
        if ((i*Pd) % 100 == 0)
          ok = true;
    }

    printf("Case #%d: %s\n", caso, (ok ? "Possible" : "Broken"));
  }

  return(0);
}

