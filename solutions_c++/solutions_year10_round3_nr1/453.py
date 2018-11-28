#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;
#define MAX 1008

struct Point
{
   int x, y;
}pp[MAX];

int main()
{
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);
   int i, j, n, t, iCas = 1, ans;
   scanf("%d", &t);
   while (t--)
   {
      scanf("%d", &n);
      for (i = 0; i < n; ++i)
         scanf("%d%d", &pp[i].x, &pp[i].y);
      ans = 0;
      for (i = 0; i < n; ++i)
         for (j = i + 1; j < n; ++j)
            if ((pp[i].x - pp[j].x) * (pp[i].y - pp[j].y) < 0)
               ans++;
      printf("Case #%d: %d\n", iCas++, ans);
   }
 //  system("pause");
}



