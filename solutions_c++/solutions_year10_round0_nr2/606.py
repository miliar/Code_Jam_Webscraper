#include<iostream>
#include<algorithm>
using namespace std;

int a[4],b[3];
int main()
{
     freopen("B-small-attempt0.in","r",stdin);
     freopen("BB-small-attempt0.out","w",stdout);
     int n,i,j,k,t,cas=1,gd,r;
     cin>>t;
     while(t--)
     {
           cin>>n;
        for(i=0;i<n;i++)
           cin>>a[i];

        sort(&a[0],&a[n]);

        for(i=1;i<n;i++)
        b[i]=a[i]-a[i-1] ;

           gd=b[1];
           for(i=2;i<n;i++)
           gd =__gcd(gd,b[i]);
           r=a[0]%gd;
          if(!r)
          printf("Case #%d: 0\n",cas++);
          else
          printf("Case #%d: %d\n",cas++,gd-r);

     }

     return 0;
}
