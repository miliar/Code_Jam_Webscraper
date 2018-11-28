#include<iostream>
#include<cmath>

using namespace std;

int main()
{
     int t,n,k,a=0;
     cin>>t;
     for(int i=1;i<=t;i++)
     {
          cin>>n>>k;
          cout<<"Case #"<<i<<": ";
          a=(k+1)%(int)pow(2.0,n);
          if(a) cout<<"OFF\n";
          else cout<<"ON\n";
     }
     //system("pause");
     return 0;
}
