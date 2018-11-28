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
int ans[20000][2], op[20000], c[20000];

int main(void)
{
   int i, j, k, l, v, res;
   //freopen("A-small-attempt0.in", "r", stdin);
   //freopen("A-small-attempt0.out", "w", stdout);
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d:\n", tn+1);
      scanf("%d%d", &n, &v);

      for (i=1; i<=(n-1)/2; i++)
         scanf("%d %d", &op[i], &c[i]);
      for (i=(n+1)/2; i<=n; i++)
      {
         scanf("%d", &l);
         ans[i][l]=0;
         ans[i][1-l]=100000;
      }

      for (i=(n-1)/2; i>=1; i--)
      {
         ans[i][0]=ans[i][1]=100000;
         for (j=0; j<=1; j++)
            for (k=0; k<=1; k++)
            {
               if (op[i]==0) res=j || k;
               else res=j && k;
               if (ans[i+i][j]+ans[i+i+1][k]<ans[i][res])
                  ans[i][res]=ans[i+i][j]+ans[i+i+1][k];
            }
         if (c[i]==1)
         for (j=0; j<=1; j++)
            for (k=0; k<=1; k++)
            {
               if (op[i]==0) res=j && k;
               else res=j || k;
               if (ans[i+i][j]+ans[i+i+1][k]+1<ans[i][res])
                  ans[i][res]=ans[i+i][j]+ans[i+i+1][k]+1;
            }
      }

      printf("Case #%d: ", tn+1);
      if (ans[1][v]>=100000) printf("IMPOSSIBLE\n");
      else printf("%d\n", ans[1][v]);
   }
   return 0;
}
