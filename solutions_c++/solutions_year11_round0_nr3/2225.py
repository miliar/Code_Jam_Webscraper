#include<iostream>
#include<cstring>
using namespace std;

int n,m,x,a,tt,sum;

int main()
  {
   freopen("C.in","r",stdin);
   freopen("C.out","w",stdout);
   scanf("%d",&tt);
   for (int t=1;t<=tt;t++)
     {
      scanf("%d",&n);m=1<<30;x=sum=0;
      for (int i=0;i<n;i++) {scanf("%d",&a);sum+=a;m=min(m,a);x^=a;}
      printf("Case #%d: ",t);
      if (x) printf("NO\n"); else printf("%d\n",sum-m);
     }
   return 0;
  }
