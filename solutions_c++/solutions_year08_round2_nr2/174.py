/* 
 * File:   newJam.cc
 * Author: Tanaeem
 *
 * Created on July 26, 2008, 11:09 PM
 */

#include <stdio.h>


#include <stdlib.h>
#include<string.h>
bool isnp[1100];

void seive ()
{
  for (int i = 2; i < 1100; i++)
    {
      if (!isnp[i])
        for (int j = i * i; j < 1100; j += i)
          {
            isnp[j] = true;
          }
    }

}
int par[1100];
int rank[1100];

void init ()
{
  for (int i = 0; i < 1100; i++)
    {
      par[i] = i;
      rank[i] = 0;
    }
}

int get (int i)
{
  if (i != par[i])
    par[i] = get (par[i]);
  return par[i];
}

bool uni (int i, int j)
{
  i = get (i);
  j = get (j);
  if (i == j)
    return false;
  if (rank[i] > rank[j])
    par[j] = i;
  else if (rank[j] > rank[j])
    par[i] = j;
  else
    {
      par[i] = j;
      rank[i]++;
    }
  return true;
}

int main ()
{
    freopen ("B.in","r",stdin);
    freopen ("small.op","w",stdout);

  //  freopen ("C-large.in.enc.txt","r",stdin);
  //  freopen ("large.op","w",stdout);
  int t, c = 0;
  scanf ("%d", &t);
  seive ();
  int a, b, p;
  while (t--)
    {
      scanf ("%d%d%d", &a, &b, &p);
      init ();
      int res = b - a + 1;
      for (int i = p; i <= b; i++)
        {
          if (isnp[i])
            continue;
          int j = (a / i) * i;
          if (j < a)
            j += i;

          {
            int k = j + i;
            for (; k <= b; k += i)
              if (uni (j, k))
                res--;
          }
        }




      printf ("Case #%d: %d\n", ++c, res);


    }


  return 0;
}

