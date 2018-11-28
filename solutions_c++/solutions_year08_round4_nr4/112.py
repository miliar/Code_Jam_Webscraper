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

int n, tn, nt, p[20], mark[20], ans;
char s[10000], t[10000];

void run(int x)
{
   int i, j, k;
   if (x==n)
   {
      for (i=0; s[i]!=0; i+=n)
         for (j=0; j<n; j++)
            t[j+i]=s[p[j]+i];
      k=0;
      for (j=0; j<i; j++)
         if (j==0 || t[j]!=t[j-1])
            k++;
      if (k<ans) ans=k;
   }
   else
   {
      for (i=0; i<n; i++)
         if (!mark[i])
         {
            mark[i]=1;
            p[x]=i;
            run(x+1);
            mark[i]=0;
         }
   }

}

int main(void)
{
   int i, j, k, l, m, f, a;
   freopen("D-small-attempt0.in", "r", stdin);
   freopen("D-small-attempt0.out", "w", stdout);
   //freopen("D-large.in", "r", stdin);
   //freopen("D-large.out", "w", stdout);

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d:\n", tn+1);
      scanf("%d\n", &n);
      memset(mark, 0, sizeof(mark));
      ans=1000000;
      
      gets(s);
      
      run(0);      

      printf("Case #%d: ", tn+1);
      printf("%d\n", ans);
   }
   return 0;
}
