#include <stdio.h>

int i, j, tc, n, k;

int main ()
{
  scanf ("%d", &tc);
  for (int i = 1; i <= tc; i++)
  {
    scanf ("%d%d", &n, &k);
    bool can = true;
    for (int j = 0; j < n; j++)
    {
      if ((k & 1) == 0)
      {
        can = false;
        break;
      }
      k = k >> 1;
      //printf ("%d", k);
    }
    printf ("Case #%d: %s\n", i, can? "ON" : "OFF");
  }
}
