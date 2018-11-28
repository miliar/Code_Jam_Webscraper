#include<iostream>
using namespace std;
int main()
{
    int test_case,i,n,k;
    long long int x;
    cin>>test_case;
    for(i=0;i<test_case;i++) 
    {
               cin>>n>>k;
               x = 1<<n;
               cout<<"Case #"<<(i+1)<<": ";
               if(k%x==(x-1))
               {
                         cout<<"ON\n";
               }                  
               else
               {
                         cout<<"OFF\n";
               }   
    }
    return 0;
}
