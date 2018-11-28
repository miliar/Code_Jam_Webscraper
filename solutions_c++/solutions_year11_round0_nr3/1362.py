#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
       int tt,n,i,sun,ii,min,s,a;
       freopen("C2.in","r",stdin);
       freopen("C2.out","w",stdout);
       scanf("%d",&tt);
       for(i=1;i<=tt;i++)
       {
           scanf("%d",&n);
           scanf("%d",&min);
           s=min;
           sun=min;
           for(ii=1;ii<n;ii++)
           {
               scanf("%d",&a);
               s^=a;
               sun+=a;
               if(a<min)
               min=a;
           }
           if(s)
           printf("Case #%d: NO\n",i);
           else
           printf("Case #%d: %d\n",i,sun-min);
       }
       return 0;
}
