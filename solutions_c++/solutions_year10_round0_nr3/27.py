/*
 * File:   main.cpp
 * Author: tanaeem
 *
 * Created on May 8, 2010, 6:38 AM
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef long long ll;
ll r, k;
int n;
ll inp[1100];
ll cst[1100];
int pr[1100];

int main()
{
  freopen("C1.in", "r", stdin);
  freopen("C1.op", "w", stdout);

  int t;
  scanf("%d", &t);
  int cs=0;
  while (t--)
  {
    scanf("%lld%lld%d", &r, &k, &n);
    for (int i=0; i < n; i++)
    {
      scanf("%lld", &inp[i]);
    }
    memset(pr, -1, sizeof (pr));
    int st=0;
    ll prt=0;
    int i=0;
    for (; i < r; i++)
    {
      if (pr[st] >= 0)
      {
        int cyc=i - pr[st];
        ll cyl=prt - cst[st];
        int cc=(r - i) / cyc;
        i+=cc*cyc;
        prt+=cc*cyl;
        break;
      }
      pr[st]=i;
      cst[st]=prt;

      int prv=(st + n - 1) % n;
      ll tt=0;
      while (tt + inp[st] <= k)
      {
        tt+=inp[st];
        if (st == prv)
        {
          st++;
          st%=n;
          break;
        }
        st++;
        st%=n;
      }
      prt+=tt;
    }

    for (; i < r; i++)
    {
      int prv=(st + n - 1) % n;
      ll tt=0;
      while (tt + inp[st] <= k)
      {
        tt+=inp[st];
        if (st == prv)
        {
          st++;
          st%=n;
          break;
        }
        st++;
        st%=n;
      }
      prt+=tt;
    }

    printf("Case #%d: %lld\n", ++cs, prt);
  }
  return 0;
}

