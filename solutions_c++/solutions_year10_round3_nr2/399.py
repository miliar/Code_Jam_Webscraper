#include<iostream>
using namespace std;
int main()
{
    long long t,n,p,c,ans,l1,l2,l,q;
    q=1;
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
cout<<"Case #"<<q++<<": "<<ans<<endl;
}
return 0;
}
