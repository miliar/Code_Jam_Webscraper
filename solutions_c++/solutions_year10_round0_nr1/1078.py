#include<iostream>
using namespace std;

int n,k,t=0;

int main()
  {
   //freopen("snapper.in","r",stdin);
   //freopen("snapper.out","w",stdout);
   scanf("%d",&t);
   for (int i=1;i<=t;i++)
     {
      scanf("%d%d",&n,&k);
      k%=1<<n;
      if (k==(1<<n)-1) printf("Case #%d: ON\n",i); else printf("Case #%d: OFF\n",i);
     }
   return 0;
  }
