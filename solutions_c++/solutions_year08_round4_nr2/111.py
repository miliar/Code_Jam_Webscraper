#pragma comment(linker,"/STACK:100000000")  

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

int main(void)
{
   int i, j, k, l, m, f, a;
   freopen("B-small-attempt0.in", "r", stdin);
   freopen("B-small-attempt0.out", "w", stdout);
   //freopen("B-large.in", "r", stdin);
   //freopen("B-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d:\n", tn+1);
      scanf("%d%d%d", &n, &m, &a);

      printf("Case #%d: ", tn+1);
      f=0;
      for (i=0; i<=n && !f; i++)
         for (j=0; j<=m && !f; j++)
            for (k=0; k<=n && !f; k++)
               for (l=0; l<=m && !f; l++)
                  if (i*l-j*k==a)
                  {
                     printf("%d %d %d %d %d %d\n", 0, 0, i, j, k, l);
                     f=1;
                  }
      if (!f) printf("IMPOSSIBLE\n");
   }
   return 0;
}
