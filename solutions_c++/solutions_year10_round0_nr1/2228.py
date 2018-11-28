#include<iostream>
using namespace std;
int main()
{
    int t,i,n,k;
    long long int x;
    cin>>t;
    for(i=0;i<t;i++) 
    {
               cin>>n>>k;
               x = 1<<n;
               if(k%x==(x-1))
               {
                         cout<<"Case #"<<(i+1)<<": ON\n";
               }                  
               else
               {
                         cout<<"Case #"<<(i+1)<<": OFF\n";
               }   
    }
  
    return 0;
}
