#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int task;
   scanf("%d",&task);
   for (int cases(1);cases<=task;cases++)
   {
      int n;
      scanf("%d",&n);
      int sum(0),mi = 1000000000 , t(0);
      for (int i(1);i<=n;i++)
      {
         int x ;
         scanf("%d",&x);
         sum = sum ^ x;
         t = t + x;
         if (x < mi) mi = x;
      }
      if (sum != 0) printf("Case #%d: NO\n",cases);
         else
            printf("Case #%d: %d\n",cases,t - mi);
   }
   return 0;
}
