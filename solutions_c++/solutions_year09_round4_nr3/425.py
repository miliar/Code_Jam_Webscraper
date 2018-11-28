#pragma comment(linker,"/STACK:100000000")  

#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;

int b[105][35];
int a[105][105];

int ans[1<<16];
int ans2[1<<16][16];

int get(int mask);

int get2(int mask, int x)
{
   if (ans2[mask][x]!=-1) return ans2[mask][x];
   int res=get(mask);
   for (int i=0; i<n; i++)
      if ((((mask>>i)&1)==1) && a[x][i])
      {
         int t=get2(mask^(1<<i), i);
         if (t<res) res=t;
      }
   return ans2[mask][x]=res;
}

int get(int mask)
{
   if (ans[mask]!=-1) return ans[mask];
   int res=1000;
   for (int i=0; i<n; i++)
      if ((mask>>i)&1)
      {
         int t=1+get2(mask^(1<<i), i);
         if (t<res) res=t;
      }
   return ans[mask]=res;
}

int main(void)
{
   int i, j, k, l;
   freopen("C-small-attempt0.in", "r", stdin);
   freopen("C-small-attempt0.out", "w", stdout);
   //freopen("C-large.in", "r", stdin);
   //freopen("C-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);
      ans[0]=0;
      memset(ans, -1, sizeof(ans));
      memset(ans2, -1, sizeof(ans2));
      scanf("%d%d", &n, &k);
      for (i=0; i<n; i++)
         for (j=0; j<k; j++)
            scanf("%d", &b[i][j]);
      
      for (i=0; i<n; i++)
         ans2[0][i]=0;

      for (i=0; i<n; i++)
         for (j=0; j<n; j++)
         {
            a[i][j]=1;
            for (l=0; l<k; l++)
               if (b[i][l]<=b[j][l])
                  a[i][j]=0;
         }

      printf("Case #%d: ", tn+1);
      printf("%d", get((1<<n)-1));
      printf("\n");
   }
   return 0;
}
