#include<iostream>
using namespace std;
int main()
{
    long num=0,i,j,k,t,l,p,c,a[1000][2];
    long long l1,l2;
    long ans;
    float d;
    cin>>t;
    while(t--)
    {
        cin>>l>>p>>c;
        l1=p/l+!!(p%l);
        l2=c;
        ans=0;
        while(l1>l2)
        {
            l2=l2*l2;
            ans++;
        }
        cout<<"Case #"<<++num<<": "<<ans<<endl;
    }
return 0;
}
