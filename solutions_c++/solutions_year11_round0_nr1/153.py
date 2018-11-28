#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>

using namespace std;

const int maxn(205);

int a[maxn],b[maxn],n;

int next(int i,int k,int pos)
{
   for (int j(i);j<=n;j++)
      if (a[j] == k) return b[j];
   return pos;
}

int main()
{
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int task;
   scanf("%d",&task);
   for (int cases(1);cases<=task;cases++)
   {
      int pos0(1) , pos1(1) , ans(0);
      scanf("%d",&n);
      for (int i(1);i<=n;i++)
      {
         char s[5];
         scanf("%s %d",s,&b[i]);
         if (s[0] == 'O') a[i] = 0;
            else a[i] = 1;
      }
      // 2(0) 1(1) 2(1) 4(0) 
      int i = 1;
      while (i<=n)
      {
         int next_0 = next(i,0,pos0);
         int next_1 = next(i,1,pos1);
         int dist0 = abs(next_0 - pos0);
         int dist1 = abs(next_1 - pos1);
            
         if (a[i] == 0)
         {
            ans = ans + dist0 + 1;
            pos0 = next_0;
            int delta;
            if (dist1 <= dist0+1) delta = dist1;
               else delta = dist0+1;
            if (pos1 < next_1) pos1+=delta;
               else pos1-=delta;
         } else
         {
            ans = ans + dist1 + 1;
            pos1 = next_1;
            int delta;
            if (dist0 <= dist1+1) delta = dist0;
               else delta = dist1+1;
            if (pos0 < next_0) pos0+=delta;
               else pos0-=delta;
         }
         i++;   
      }
      printf("Case #%d: %d\n",cases,ans);
   }
   return 0;
}
