/* 
 * File:   newJam.cc
 * Author: Tanaeem
 *
 * Created on August 2, 2008, 10:05 PM
 */

#include <stdio.h>


#include <stdio.h>


#include <stdlib.h>
#include<string.h>

#define  INF 10000000
int m, inp[11000][2];
int cache[11000][3];

int mincost (int i, int tar)
{
  if (i > (m - 1) / 2)
    {
      return (inp[i][0] != tar) * INF;
    }
  if (cache[i][tar] != -1)
    return cache[i][tar];
  cache[i][tar] = INF;
  if (inp[i][0] == tar)
    {
      cache[i][tar] = mincost (2 * i, tar) + mincost (2 * i + 1, tar);
      if (cache[i][tar] > INF)
        cache[i][tar] = INF;

    }
  else
    {
      cache[i][tar] = mincost (2 * i, tar) + mincost (2 * i + 1, tar);
      int t = mincost (2 * i, tar) + mincost (2 * i + 1, 1 - tar);
      if (t < cache[i][tar])
        cache[i][tar] = t;
      t = mincost (2 * i, 1 - tar) + mincost (2 * i + 1, tar);
      if (t < cache[i][tar])
        cache[i][tar] = t;
      if (cache[i][tar] > INF)
        cache[i][tar] = INF;
    }
  if (inp[i][1] == 0)
    return cache[i][tar];
  inp[i][0] = 1 - inp[i][0];

  if (inp[i][0] == tar)
    {
      int t;
      t = mincost (2 * i, tar) + mincost (2 * i + 1, tar)+1;
      if (t < cache[i][tar])
        cache[i][tar] = t;
      if (cache[i][tar] > INF)
        cache[i][tar] = INF;

    }
  else
    {
      int t = mincost (2 * i, tar) + mincost (2 * i + 1, tar)+1;
      if (t < cache[i][tar])
        cache[i][tar] = t;
      t = mincost (2 * i, tar) + mincost (2 * i + 1, 1 - tar)+1;
      if (t < cache[i][tar])
        cache[i][tar] = t;
      t = mincost (2 * i, 1 - tar) + mincost (2 * i + 1, tar)+1;
      if (t < cache[i][tar])
        cache[i][tar] = t;
      if (cache[i][tar] > INF)
        cache[i][tar] = INF;
    }

  inp[i][0] = 1 - inp[i][0];
  return cache[i][tar];

}

void init ()
{
  for (int i = 0; i < m + 20; i++)
    {
      cache[i][0] = cache[i][1] = -1;
    }

}

int main ()
{
    freopen ("A2.in","r",stdin);
//    freopen ("small.op","w",stdout);

  //  freopen ("C-large.in.enc.txt","r",stdin);
    freopen ("large.op","w",stdout);
  int t, c = 0, i;
  scanf ("%d", &t);
  while (t--)
    {
      int tar;
      scanf ("%d%d", &m, &tar);
      for (i = 1; i <= (m - 1) / 2; i++)
        {
          scanf ("%d%d", &inp[i][0], &inp[i][1]);
        }
      for (; i <= m; i++)
        {
          scanf ("%d", &inp[i][0]);
        }

      init ();
      int op = mincost (1, tar);


      if (op < INF)
        printf ("Case #%d: %d\n", ++c, op);
      else
        printf ("Case #%d: IMPOSSIBLE\n", ++c);


    }


  return 0;
}

