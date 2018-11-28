#include<iostream>
using namespace std;
int main(){
    int t,n,k,i;
    unsigned long long a,b;
    cin>>t;
    for(i=1;i<=t;i++)
    {
                     a=0;b=1;
                     cin>>n>>k;
                     a=b<<n;
                     b=a-1;
                     if(k<b)
                     cout<<"Case #"<<i<<": OFF"<<endl;
                     else if(k==b)
                     cout<<"Case #"<<i<<": ON"<<endl;
                     else
                     {
                         while(k>b)
                         b=b+a;
                         if(k==b)
                          cout<<"Case #"<<i<<": ON"<<endl;
                          else
                           cout<<"Case #"<<i<<": OFF"<<endl;
                           }
                           }
                           return 0;
                           }
                           
