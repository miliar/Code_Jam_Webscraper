#include <iostream>
using namespace std;

int main()
{
    freopen("s.txt","w",stdout);
    int t,n,k,i,f,p1,p2;
    cin>>t;
    for(k=1;k<=t;k++)
    {
       cin>>n>>p1>>p2;
              
       if(p1<100&&p2==100 || p1>0&&p2==0)
       {
         cout<<"Case #"<<k<<": "<<"Broken"<<endl;
         continue;
       }
       
       f=0;

       for(i=1;i<=n;i++)
       {
          if((i*p1)%100==0)
          {
            cout<<"Case #"<<k<<": "<<"Possible"<<endl;
            f=1;
            break;
          }
       }
       if(f==0)
          cout<<"Case #"<<k<<": "<<"Broken"<<endl;
    }
    return 0;
}
