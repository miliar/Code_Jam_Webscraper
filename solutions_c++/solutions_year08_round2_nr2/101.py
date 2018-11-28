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

int n, tn, nt, ans;
int p[1000005];
//int r=0;

int pr(int x)
{
   //if (r==1) fprintf(stderr, "%d\n", x);
   if (p[x]==x) return x;
   return p[x]=pr(p[x]);
}

void un(int u, int v)
{
   //fprintf(stderr, "%d %d ", u, v);
   //if (u==20 && v==6) r=1;
   u=pr(u);
   v=pr(v);
   //fprintf(stderr, "%d %d\n", u, v);
   if (u!=v)
   {
      ans--;
      if (rand()&1) p[u]=v;
      else p[v]=u;
   }
}

char a[2000005];

int main(void)
{
   long long i, j, k, A, B, M;
   //freopen("B-small-attempt0.in", "r", stdin);
   //freopen("B-small-attempt0.out", "w", stdout);
   freopen("B-large.in", "r", stdin);
   freopen("B-large.out", "w", stdout);
   a[0]=a[1]=1;
   for (i=2; i<=1000; i++)
      if (!a[i])
         for (j=i*i; j<=1000000; j+=i)
            a[j]=1;

   scanf("%d\n", &nt);
   for (tn=0; tn<nt; tn++)
   {
      scanf("%I64d%I64d%I64d\n", &A, &B, &M);
      ans=n=B-A+1;

      for (i=0; i<=n; i++)
         p[i]=i;

      for (i=M; i<n; i++)
         if (!a[i])
         {
            for (j=k=((A-1)/i+1)*i; j<=B-i; )
            {
               j+=i; 
               un(j-A, k-A);
            }
         }

      printf("Case #%d: ", tn+1);
      printf("%d\n", ans);
   }
   return 0;
}
