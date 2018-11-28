#include<iostream>

using namespace std;

int main()
    {
          long long k,t,n,i,val,sum,min;
          cin>>t;
          for(k=1;k<=t;k++)
          {
                           cin>>n;
                           long long a[n];
                           cin>>a[0];
                           val=a[0];
                           min=a[0];
                           sum=a[0];
                           for(i=1;i<n;i++)
                           {
                                           cin>>a[i];
                                           val^=a[i];
                                           sum+=a[i];
                                           if(a[i]<min)
                                                       min=a[i];
                           }
                           if(val!=0)
                                     cout<<"Case #"<<k<<": NO"<<endl;
                           else
                                     cout<<"Case #"<<k<<": "<<(sum-min)<<endl;
          }
          return 0;
    }
