#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define ll long long

int tn, nt, n;

int a[105][105], b[105][105];

int main(void)
{
   freopen("C-small-attempt0.in", "r", stdin);
   freopen("C-small-attempt0.out", "w", stdout);
   //freopen("C-large.in", "r", stdin);
   //freopen("C-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      //fprintf(stderr, "Case #%d: \n", tn+1);

      scanf("%d", &n);
      memset(a, 0, sizeof(a));
      for (int i=0; i<n; i++)
      {
        int x1, x2, y1, y2;
        scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
        for (int j=x1; j<=x2; j++)
          for (int k=y1; k<=y2; k++)
            a[j][k]=1;
      }

      int ans=0;
      while (1)
      {
        int good = 0;
        for (int i=0; i<=101; i++)
          for (int j=0; j<=101; j++)
            if (a[i][j]) good = 1;
        if (!good) break;
        ans++;
        memset(b, 0, sizeof(b));
        for (int i=1; i<=101; i++)
          for (int j=1; j<=101; j++)
          {
            b[i][j]=a[i][j];
            if (a[i][j] && !a[i-1][j] && !a[i][j-1])
              b[i][j]=0;
            if (!a[i][j] && a[i-1][j] && a[i][j-1])
              b[i][j]=1;
          }

        memcpy(a, b, sizeof(a));
      }

      printf("Case #%d: ", tn+1);

      printf("%d\n", ans);
   }
   return 0;
}
