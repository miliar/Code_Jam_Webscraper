#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

using namespace std;

#define MAX 1024
int C[MAX];

int main(void)
{
  int T,caso;

  for(scanf("%d",&T), caso = 1; caso <= T; caso++)
  {
    int N,t,x;

    scanf("%d", &N);
    t = 0;
    for(int i = 0; i < N; i++)
    {
      scanf("%d", C+i);
      t += C[i];
      if (i == 0 || C[i] < x)
        x = C[i];
    }

    int ok = 1;
    for(int i = 0; i < 32 && ok; i++)
    {
      int p = 0;
      for(int j = 0; j < N; j++)
        if ((C[j] & (1 << i)) != 0)
          p++;
      if (p%2)
        ok = 0;
    }

    char s[256];
    sprintf(s, "%d", t-x);
    printf("Case #%d: %s\n", caso, (ok) ? s : "NO");
  }

  return(0);
}

