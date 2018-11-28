#include<iostream>
using namespace std;
long long x[107700];
int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
    int n;
    cin>>n;
    long long s=0;
    long long c=0;
    long long min=-1;
    for(int i=1;i<=n;i++)
    {
    cin>>x[i];
    s+=x[i];
    c=(c^x[i]);
    if(x[i]<min||min<0)min=x[i];
    }
    if(c==0)
    {
         cout<<"Case #"<<i<<": "<<s-min<<endl;
    }
    else
    {
         cout<<"Case #"<<i<<": NO"<<endl;
    }
}
return 0;
}
