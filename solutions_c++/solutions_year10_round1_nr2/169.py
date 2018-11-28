#pragma comment(linker,"/STACK:100000000")  

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

int tn, nt;

int a[260][105];
int b[105];

int main(void)
{
   //freopen("B-small-attempt0.in", "r", stdin);
   //freopen("B-small-attempt0.out", "w", stdout);
   freopen("B-large.in", "r", stdin);
   freopen("B-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);

      printf("Case #%d: ", tn+1);

      int D, I, m, n;
      scanf("%d%d%d%d\n", &D, &I, &m, &n);
      for (int i=1; i<=n; i++)
        scanf("%d", &b[i]);

      memset(a, 63, sizeof(a));
      int inf=a[0][0];
      int res=inf;

      for (int i=0; i<=255; i++)
        a[i][0]=0;
      for (int j=0; j<=n; j++)
        for (int i=0; i<=255; i++)
        {
          for (int k=0; k<=255; k++)
            for (int l=j+1; l<=n; l++)
            {
              int add;
              if (k==i) add = 0;
              else if (m==0) add = inf;
              else add = ((abs(k-i) - 1) / m) * I;

              int t = a[i][j] + (l-j-1)*D + abs(b[l]-k) + add;
              if (t<a[k][l])
                a[k][l]=t;
            }
//          printf("%d %d:%d\n", i, j, a[i][j]);
          res=min(res, (n-j)*D+a[i][j]);
        }

      printf("%d\n", res);
   }
   return 0;
}
