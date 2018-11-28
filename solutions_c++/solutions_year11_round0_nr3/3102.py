#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
    freopen("s.txt","w",stdout);
    int t,sum,n,i,j,c[20],max,a,b,b1,p,f;
    cin>>t;
    for(j=1;j<=t;j++)
    {
       cin>>n;
       for(i=0;i<n;i++)
         cin>>c[i];
       sum=1;
       for(i=1;i<=n;i++)
         sum=sum*2;
       f=0;
       max=0;
       for(i=1;i<sum-1;i++)
       {
         int tmp;
         tmp=i;
         a=b=b1=0;
         p=n-1;
         while(p>=0)
         {
           if(tmp&1==1)
             a+=c[p];
           else
           {
             b=b^c[p];
             b1+=c[p];
           }
           tmp=tmp>>1;
           p--;
          
           
         }
         if(a==b && (a>max||b1>max) )
         {  
           if(a>b1)
             max=a;
           else
             max=b1;
           f=1;

         }
       }
       if(f==0)
         cout<<"Case #"<<j<<": NO"<<endl;
       else
         cout<<"Case #"<<j<<": "<<max<<endl;
    }
    
    return 0;
}
