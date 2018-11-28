#include <stdio.h>
#include <cmath>

int main()
{
  int T;
  scanf("%d", &T);
  
  for (int t = 1; t <= T; t++)
  {
    int N, S, p, res = 0;
    scanf("%d %d %d", &N, &S, &p);
    for (int n = 0; n < N; n++)
    {
      int num;
      scanf("%d", &num);
      if ( (num+2) / 3 >= p )
        res++;
      else if (S > 0 && (num + 4) / 3 >= p && num > 0)
      {
        S--;
        res++;
      }
    }
    printf("Case #%d: %d\n", t, res);
  }

  return 0;
}