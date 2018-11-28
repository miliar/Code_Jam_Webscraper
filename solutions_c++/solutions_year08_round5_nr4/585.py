#pragma comment(linker,"/STACK:100000000")  

#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;
int a[105][105], b[105][105];

int main(void)
{
   int i, j, k, m, x, y;
   freopen("D-small-attempt0.in", "r", stdin);
   freopen("D-small-attempt0.out", "w", stdout);
   //freopen("A-large.in", "r", stdin);
   //freopen("A-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d:\n", tn+1);
      memset(a, 0, sizeof(a));
      memset(b, 0, sizeof(b));
      scanf("%d%d%d", &x, &y, &m);
      for (i=0; i<m; i++)
      {
         scanf("%d%d", &j, &k);
         b[j-1][k-1]=1;
      }
      a[0][0]=1;
      a[1][2]=1;
      a[2][1]=1;
      if (b[1][2]) a[1][2]=0;
      if (b[2][1]) a[2][1]=0;
      for (i=2; i<x; i++)
         for (j=2; j<y; j++)
         {
            a[i][j]=(a[i-1][j-2]+a[i-2][j-1])%10007;
            if (b[i][j]) a[i][j]=0;
         }
            
      printf("Case #%d: %d\n", tn+1, a[x-1][y-1]);
   }
   return 0;
}
