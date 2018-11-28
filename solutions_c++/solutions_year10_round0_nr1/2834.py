#include<iostream>
using namespace std;
int main()
{
    int t,c=0;
    cin>>t;
    while(t--)
    {
        int i,n,n1=0;
        c++;
        long long k=0;
        cin>>n>>k;
        for(i=0;i<n;i++) n1=n1|(k&1<<i);
        n1=n1+1;
        if(n1 & (1<<n)) cout<<"Case #"<<c<<": ON"<<endl;
        else  cout<<"Case #"<<c<<": OFF"<<endl;
    }
   return 0;
}
