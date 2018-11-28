#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    long long t,n,k,i,num,div;
    cin>>t;
    num=1;
    while(t--)
    {
              int flag=0;
              cin>>n>>k;
              for(i=n;i>=1;i--)
              {
                  div=1<<(i-1);
                  if((k/div)%2==0)
                  {
                     flag=1;
                     break;
                  }
              }
              if(flag==0)
                 cout<<"Case #"<<num++<<": ON"<<endl;
              else
                 cout<<"Case #"<<num++<<": OFF"<<endl;
    }
    return 0;
}   
