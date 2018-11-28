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
int G[55][55];

char s[55];

int main(void)
{
   int i, j, k, l;
   //freopen("A-small-attempt0.in", "r", stdin);
   //freopen("A-small-attempt0.out", "w", stdout);
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: ", tn+1);
      scanf("%d\n", &n);
      memset(G, 0, sizeof(G));
      for (i=0; i<n; i++)
      {
         gets(s);
         int ma=0;
         for (j=0; j<n; j++)
            if (s[j]=='1') ma=j;
         for (j=0; j<ma; j++)
            G[i][j]=-1;
         for (j=ma; j<n; j++)
            G[i][j]=1;
      }

      int ans=0;
      for (i=0; i<n; i++)
      {
         for (j=i; j<n; j++)
            if (G[j][i]==1)
            {
               for (l=j; l>i; l--) 
               {
                 for (k=0; k<n; k++)
                   swap(G[l][k], G[l-1][k]);
                 ans++;
               }
               break;
            }
      }

      printf("Case #%d: ", tn+1);
      printf("%d", ans);
      printf("\n");
   }
   return 0;
}
