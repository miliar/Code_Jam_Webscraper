#include<iostream>
using namespace std;
int a[1001];
int main()
{
 freopen("C-large.in","r",stdin);
 freopen("C-large.out","w",stdout);
 int i,j,t,n,m=0,min,s,tot;
 scanf("%d",&t);
 while(t--)
      {
       scanf("%d",&n);
       scanf("%d",a);
       s=tot=a[0];
       for(i=1;i<n;i++)
          {
           scanf("%d",a+i);
           tot+=a[i];
           s=s^a[i];
          }
       if(s) printf("Case #%d: NO\n",++m);
       else
         {
          min=a[0];
          for(j=0;j<n;j++) 
              if(min>a[j])
                 min=a[j];
          printf("Case #%d: %d\n",++m,tot-min);
         } 
      }
 return 0;
}
