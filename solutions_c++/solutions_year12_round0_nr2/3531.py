#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
int n,s,p,t,x,ans,a[33];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for (int j=1;j<=t;j++){
        cin>>n>>s>>p;ans=0;
        for (int i=0;i<=30;i++)a[i]=0;
        for (int i=1;i<=n;i++){
            cin>>x;a[x]++;}
        if (p==0)ans=n;
        else if (p==1)ans=n-a[0];
        else {
             for (int i=p*3-2;i<=30;i++)ans+=a[i];
             ans+=min(a[p*3-3],s);s-=min(a[p*3-3],s);
             ans+=min(a[p*3-4],s);s-=min(a[p*3-4],s);}
        cout<<"Case #"<<j<<": "<<ans<<endl;}
    return 0;
}
        
