#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;

long long a[3][3];

int main(void)
{
   int i, j, k, l, m, A, B, C, D, x0, y0, M;
   long long X, Y;
   //freopen("A-small-attempt2.in", "r", stdin);
   //freopen("A-small-attempt2.out", "w", stdout);
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);
   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      scanf("%d%d%d%d%d%d%d%d\n", &n, &A, &B, &C, &D, &x0, &y0, &M);
      memset(a, 0, sizeof(a));
      X = x0, Y = y0;
      for (i = 0; i<n; i++)
      {
         a[X%3][Y%3]++;
         X = (A * X + B) % M;
         Y = (C * Y + D) % M;
      }

      long long ans=0;

      for (i=0; i<3; i++)
         for (j=0; j<3; j++)
            for (k=0; k<3; k++)
               for (l=0; l<3; l++)
               {
                  m=(6-i-k)%3;
                  n=(6-j-l)%3;
                  if (i==k && k==m && j==l && l==n) ans+=(a[i][j]*(a[i][j]-1)*(a[i][j]-2))/*/6*/;
                  else if (i==k && j==l) ans+=(a[i][j]*(a[i][j]-1)*a[m][n])/*/2*/;
                  else if (i==m && j==n) ans+=(a[i][j]*(a[i][j]-1)*a[k][l])/*/2*/;
                  else if (k==m && l==n) ans+=(a[k][l]*(a[k][l]-1)*a[i][j])/*/2*/;
                  else ans+=a[i][j]*a[k][l]*a[m][n];
               }

      printf("Case #%d: ", tn+1);
      printf("%I64d\n", ans/6);
   }
   return 0;
}
