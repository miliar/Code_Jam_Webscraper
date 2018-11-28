#include<iostream>
using namespace std;
int main()
{
int t,n,s,p,x1,x2,ans;
int a[100];
cin>>t;
for(int i1=0;i1<t;i1++)
{
ans=0;
cin>>n>>s>>p;
for(int i=0;i<n;i++)
{
cin>>a[i];
if(a[i]<p)
continue;
a[i]-=p;
x1=a[i]/2;
x2=a[i]-x1;
if(x2>p)
ans++;
else
{
if(p-x2<2 && p-x1<2)
ans++;
else if(p-x2<=2 && p-x1<=2 && s>0)
{ans++;s--;}
}
}
cout<<"Case #"<<i1+1<<": "<<ans<<endl;
}
return 0;
}
