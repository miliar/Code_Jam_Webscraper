/* 
 * File:   newJam.cc
 * Author: Tanaeem
 *
 * Created on July 17, 2008, 8:48 AM
 */

#include <stdio.h>


#include <stdio.h>
#include <stdlib.h>
#include<string.h>
int acnt[2500];
int bcnt[2500];
char buf[20];

int main ()
{
//    freopen ("B.in","r",stdin);
//    freopen ("small.op","w",stdout);

    freopen ("B2.in","r",stdin);
    freopen ("large.op","w",stdout);
  int t, c = 0;
  scanf ("%d", &t);
  while (t--)
    {
      int opa, opb;
      int na, nb;
      for (int i = 0; i < 2400; i++)
        {
          acnt[i] = bcnt[i] = 0;
        }
      int dl;
      scanf ("%d", &dl);
      scanf ("%d%d", &na, &nb);


      for (int i = 0; i < na; i++)
        {
          int h, m;
          scanf ("%d:%d", &h, &m);
          if(h>24)
            h=h;
          acnt[h * 60 + m]--;
          scanf ("%d:%d", &h, &m);
          if(h * 60 + m + dl<2400)
          bcnt[h * 60 + m + dl]++;
        }

      for (int i = 0; i < nb; i++)
        {
          int h, m;
          scanf ("%d:%d", &h, &m);
          if(h*60+m <2400)
          bcnt[h * 60 + m]--;
          scanf ("%d:%d", &h, &m);
          if(h * 60 + m + dl<2400)
          acnt[h * 60 + m + dl]++;
        }
      opa = 0;
      int sum = 0;
      for (int i = 0; i < 2200; i++)
        {
          sum += acnt[i];
          if (sum < opa)
            opa = sum;
        }
      opb = 0;
      sum = 0;
      for (int i = 0; i < 2200; i++)
        {
          sum += bcnt[i];
          if (sum < opb)
            opb = sum;
        }
      opa=-opa;
      opb=-opb;

      printf ("Case #%d: %d %d\n", ++c, opa, opb);

    }


  return 0;
}

