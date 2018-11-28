#include<iostream>
using namespace std;
int main()
{
   int i,j,k;
   int n,t;
   int cnt;
   int ans;
   int a[35];
   freopen("A-large.in","r",stdin);
   freopen("out.txt","w",stdout);
   a[1]=2;
   for(i=2;i<=33;i++)
     a[i]=2*a[i-1];
  // for(i=1;i<=33;i++)
      //cout<<a[i]<<endl;
   scanf("%d",&t);
   for(i=1;i<=t;i++)
   {
      ans=0;

      scanf("%d%d",&n,&k);
      if(n==1)
      {
        if(k%2==0) ans=0;
        else ans=1; 
      }
      else 
      {
         k%=a[n];
         if(k==a[n]-1) ans=1;
         else ans=0;
      }
      printf("Case #%d: ",i);
      if(ans==0) printf("OFF\n");
      else printf("ON\n");
   }
  // while(1);
   return 0;
}
