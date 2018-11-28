#include<iostream>
#include<cstdio>
using namespace std;

const int maxn(1001);

double f[maxn] , tmps[maxn] , h[maxn];

double g(int i,int j)
{
   return h[j] * tmps[i-j];
}

int main()
{
   freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   /*
   tmps[0] = 1;
   for (int i(1);i<maxn;i++)
      tmps[i] = tmps[i-1] /  i;
   h[0] = 1;
   for (int i(1);i<maxn;i++)
      if (i % 2 == 1)
         h[i] = h[i-1] - tmps[i];
      else
         h[i] = h[i-1] + tmps[i];
   for (int i(2);i<maxn;i++)
   {
      double sum(1);
      for (int j(2);j<i;j++)
         sum = sum + g(i,j) * f[j];
      f[i] = sum / (1 - g(i,i)) ;
   }
   */
   int task;
   scanf("%d",&task);
   for (int cases(1);cases<=task;cases++)
   {
      int n;
      scanf("%d",&n);
      int m = 0;
      for (int i(1);i<=n;i++)
      {
         int x;
         scanf("%d",&x);
         if (x != i) m++;
      }
      printf("Case #%d: %.6lf\n",cases,1.0*m);
   }
   
   return 0;
}
