#include<iostream>
using namespace std;
int main()
{
    long long i,t,n,min,p,xo,sum,k=1;
    cin>>t;
    while(t--)
    {
           xo=0;sum=0;
           p=0;
           min=10000000;
           cin>>n;
           for(i=0;i<n;i++)
             {
              cin>>p;
              sum+=p;
              if(p<min)
              min=p;
              xo=xo^p;
              }
              if(xo)cout<<"Case #"<<k++<<": NO\n";
              else
              cout<<"Case #"<<k++<<": "<<sum-min<<endl;
           }
           // system("pause");  
            return 0;
    }
