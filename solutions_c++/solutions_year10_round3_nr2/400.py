#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;
#define MAX 108

typedef long long LL;


int main()
{
   freopen("B-large.in", "r", stdin);
   freopen("B-large.out", "w", stdout);
   int i, j, t, iCas = 1,  cnt, tp, ans, f;
   LL L, P, C;
   scanf("%d", &t);
   while (t--)
   {
      scanf("%lld%lld%lld", &L, &P, &C);
      for (i = 0; L < P; ++i)
         L *= C;
      cnt = i - 1;
   //   printf("%d\n", cnt);
      if (i == 1)
         ans = 0;
      else
      {
      //   cnt = i;
         for (i = 1; 1 <= (cnt >> i); ++i);
            ans = i;
      }
      
      printf("Case #%d: %d\n", iCas++, ans); 
   }
   
  //system("pause");
}
