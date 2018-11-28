#include<iostream>
#include<math.h>
using namespace std;
int main()
{
   long long k,n,mod;
   long t;
   cin>>t;
   for(long i=1;i<=t;i++)
   {
      cin>>n;
      cin>>k;
      n = pow(2,n);   
      mod = (k+1)&(n-1);
      if(mod==0)
         cout<<"Case #"<<i<<": ON\n";
      else
         cout<<"Case #"<<i<<": OFF\n";
   }
   return 0;
}
