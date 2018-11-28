/* 
 * File:   newJam.cc
 * Author: Tanaeem
 *
 * Created on July 17, 2008, 7:09 AM
 */

#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#include<assert.h>
#define INF 111000
int q, s;
char eng[110][110];
int srch[1100];
char buf[101];
int cache[110][1100];

int chc[110][1100];

void init ()
{
  for (int i = 0; i < s + 5; i++)
    {
      for (int j = 0; j < q + 5; j++)
        {
          cache[i][j] = -1;
        }
    }
}

void show (int cur, int pos)
{
  assert (cur != srch[pos]);
  printf ("%s\t%s\n", eng[srch[pos]], eng[cur]);
  if (pos < (q - 1))
    show (chc[cur][pos], pos + 1);
}

int mincost (int cur, int pos)
{
  if(cur==0 && pos==8)
    cur=0;
  assert (cur < s);
  assert (pos < q);
  assert (cur != srch[pos]);
  //  if(pos>=q)
  //    return 0;
  //  if(cur==srch[pos])
  //    return INF;
  if (pos == q - 1)
    return 0;
  if (cache[cur][pos] != -1)
    return cache[cur][pos];
  cache[cur][pos] = INF;
  for (int i = 0; i < s; i++)
    {
      if (srch[pos + 1] != i)
        {
          if (i != cur)
            {
              if (cache[cur][pos]>(mincost (i, pos + 1) + 1))
                {
                  cache[cur][pos] = (mincost (i, pos + 1) + 1);
                  chc[cur][pos] = i;
                }
            }
          else
            {
              if (cache[cur][pos]>(mincost (i, pos + 1)))
                {
                  cache[cur][pos] = (mincost (i, pos + 1));
                  chc[cur][pos] = i;
                }

            }
        }
    }
  assert(chc[cur][pos]!=srch[pos+1]);
  return cache[cur][pos];
}

int main ()
{
//  freopen ("A.in", "r", stdin);
//  freopen ("small.op","w",stdout);

    freopen ("A2.in","r",stdin);
    freopen ("large.op","w",stdout);
  int t, c = 0;
  scanf ("%d", &t);
  while (t--)
    {
      scanf ("%d", &s);
      gets (buf);
      //printf("%s",buf);
      for (int i = 0; i < s; i++)
        {
          gets (eng[i]);
        }
      scanf ("%d", &q);
      gets (buf);
      for (int i = 0; i < q; i++)
        {
          gets (buf);
          srch[i] = -1;
          for (int j = 0; j < s; j++)
            {
              if (strcmp (buf, eng[j]) == 0)
                {
                  srch[i] = j;
                  break;
                }
            }
          assert (srch[i] != -1);
        }
      init ();
      int op = q;
      int chc = 0;
      if (q != 0)
        for (int i = 0; i < s; i++)
          {
            if (srch[0] == i)
              continue;
            if (op > mincost (i, 0))
              {
                op = mincost (i, 0);
                chc = i;
              }
          }

     // show (chc, 0);
      printf ("Case #%d: %d\n", ++c, op);


    }


  return 0;
}

