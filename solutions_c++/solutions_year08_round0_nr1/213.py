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

map <string, int> a;

char s[105];
int res[1005][105];

int main(void)
{
   int i, j, k, l, m;
   //freopen("B-small-attempt0.in", "r", stdin);
   //freopen("B-small-attempt0.out", "w", stdout);
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);
   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      scanf("%d\n", &n);
      a.clear();
      for (i=0; i<n; )
      {
         gets(s);
         a[s]=++i;
      }

      scanf("%d\n", &k);
      for (i=0; i<k; i++)
      {
         gets(s);
         j=a[s]-1;
         for (l=0; l<n; l++)
            res[i+1][l]=res[i][l];
         m=res[i][j]+1;
         for (l=0; l<n; l++)
            if (res[i+1][l]>m) res[i+1][l]=m;
         res[i+1][j]=100000;
      }

      m=10000;
      for (l=0; l<n; l++)
         if (res[k][l]<m) m=res[k][l];

      printf("Case #%d: ", tn+1);
      printf("%d\n", m);
   }
   return 0;
}
