#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output2.txt","w",stdout);
int n,t,i,j,a,p,r,q;
cin>>t;
for(j=1;j<=t;j++)
{
cin>>n;
p=q=0;
for(i=1;i<=n;i++)
{
cin>>a;
p+=a;
q^=a;
if(i==1) r=a;
else r=min(a,r);
}
cout<<"Case #"<<j<<": ";
if(q) cout<<"NO";
else cout<<p-r;
cout<<endl;
}
return 0;
}