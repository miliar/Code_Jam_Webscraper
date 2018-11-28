/* 
 * File:   newJam.cc
 * Author: Tanaeem
 *
 * Created on August 2, 2008, 10:49 PM
 */

#include <stdio.h>


#include <stdlib.h>
#include<string.h>

int main ()
{
  freopen ("B.in", "r", stdin);
  freopen ("small.op", "w", stdout);

  //  freopen ("C-large.in.enc.txt","r",stdin);
  //  freopen ("large.op","w",stdout);
  int t, c = 0;
  scanf ("%d", &t);
  while (t--)
    {
      int n, m, a;
      scanf ("%d%d%d", &n, &m, &a);
      int x[3], y[3];
      bool done = false;
      int x0 = 0, y0 = 0;
      for (int x1 = 0; x1 <= n; x1++)
        {
          for (int x2 = 0; x2 <= n; x2++)
            {
              for (int y2 = 0; y2 <= m; y2++)
                {
                  for (int y1 = 0; y1 <= m; y1++)
                    {
                      int ar = x1 * y2 - y1 *x2;
                      if (ar == a)
                        {
                          x[0] = x0;
                          x[1] = x1;
                          x[2] = x2;
                          y[0] = y0;
                          y[1] = y1;
                          y[2] = y2;
                          done = true;
                          ////;
                        }


                      if (done)
                        break;
                    }
                  if (done)
                    break;

                }
              if (done)
                break;

            }
          if (done)
            break;

        }
      

  if (done)
    printf ("Case #%d: %d %d %d %d %d %d\n", ++c, x[0], y[0], x[1], y[1], x[2], y[2]);
  else
    printf ("Case #%d: IMPOSSIBLE\n", ++c);


}


return 0;
}

