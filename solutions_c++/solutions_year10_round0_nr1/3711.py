#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    long long t,n,k,l=1;
     cin>>t;
     while(t>0)
     {
            cin>>n>>k;
            cout<<"Case #"<<l<<": ";
            l++;
            long long a,b,c,d;
            a=pow(2,n);
            if((k+1)%a==0) cout<<"ON"<<endl;
            else cout<<"OFF"<<endl;
     t--;
     }
     return 9;
}
