#include<iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
for(int i=1;i<=t;i++)
{
        long long n,k;
        cin>>n>>k;

    long long c=2;
    if(n==1)c=1;
    else if(n==2)
    {
    if(k%4==3)cout<<"Case #"<<i<<": ON"<<endl;
    else cout<<"Case #"<<i<<": OFF"<<endl;
    continue;
    }
    else
    {
        for(int i=1;i<=n-2;i++)
        {
        c=2*c;
        //cout<<i<<" "<<c<<endl;
        }
    }
   // cout<<c<<endl;
    if(k%(2*c)==2*c-1)cout<<"Case #"<<i<<": ON"<<endl;
    else cout<<"Case #"<<i<<": OFF"<<endl;
    
}
    //system("pause");
    return 0;
}
