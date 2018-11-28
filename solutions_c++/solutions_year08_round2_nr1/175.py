/* 
 * File:   newJam.cc
 * Author: Tanaeem
 *
 * Created on July 26, 2008, 10:18 PM
 */

#include <stdio.h>


#include <stdlib.h>
#include<string.h>

long long cnt[5][5];

long long b3 (long long a)
{
  long long res = a * (a - 1)*(a - 2);
  res /= 6;
  return res;

}

long long b2 (long long a)
{
  long long res = a * (a - 1);
  res /= 2;
  return res;
}

int main ()
{
  freopen ("A2.in", "r", stdin);
//  freopen ("small.op", "w", stdout);

  //  freopen ("C-large.in.enc.txt","r",stdin);
    freopen ("large.op","w",stdout);
  int t, C = 0;
  scanf ("%d", &t);
  while (t--)
    {
      int n;
      long long a, b, c, d, x, y, m;
      scanf ("%d%lld%lld%lld%lld%lld%lld%lld", &n, &a, &b, &c, &d, &x, &y, &m);
      for (int i = 0; i < 3; i++)
        {
          for (int j = 0; j < 3; j++)
            {
              cnt[i][j] = 0;
            }

        }

      for (int i = 0; i < n; i++)
        {
        
          cnt[x % 3][y % 3]++;
          x = (a * x + b) % m;
          y = (c * y + d) % m;
        }
      long long res = 0;
      for (int i = 0; i < 3; i++)
        {
          for (int j = 0; j < 3; j++)
            {

              for (int ii = i; ii < 3; ii++)
                {
                  int jj = 0;
                  if (i == ii)
                    jj = j;
                  for (; jj < 3; jj++)
                    {

                      for (int iii = ii; iii < 3; iii++)
                        {

                          if ((i + ii + iii) % 3 != 0)
                            continue;
                          int jjj = 0;
                          if (ii == iii)
                            jjj = jj;
                          for (; jjj < 3; jjj++)
                            {

                              if ((j + jj + jjj) % 3 != 0)
                                continue;
                              if (i == ii && j == jj)
                                {
                                  if (ii == iii && jj == jjj)
                                    {
                                      res += b3 (cnt[i][j]);
                                    }
                                  else
                                    res += b2 (cnt[i][j]) * cnt[iii][jjj];
                                }
                              else if (ii == iii && jj == jjj)
                                res += b2 (cnt[ii][jj]) * cnt[i][j];
                              else res += cnt[i][j] * cnt[ii][jj] * cnt[iii][jjj];
                            }
                        }
                    }
                }
            }
        }

      printf ("Case #%d: %lld\n", ++C, res);


    }


  return 0;
}

