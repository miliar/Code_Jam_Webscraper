#include<iostream>
#include<vector>
using namespace std;
main()
{
int te,n,p,q,i,j,flag,flag1,cn=0;
cin>>te;
vector<int>v(10001);
while(te--)
{
cn++;
flag1=0;
cin>>n>>p>>q;
for(i=0;i<n;i++)
cin>>v[i];
for(i=p;i<=q && flag1==0;i++)
{
flag=0;
for(j=0;j<n && flag==0;j++)
{
if(v[j]%i==0 || i%v[j]==0)
continue;
else
flag=1;
}
if(flag==0)
{
cout<<"Case #"<<cn<<": "<<i<<"\n";
flag1=1;
}
}
if(flag1==0)
cout<<"Case #"<<cn<<": "<<"NO"<<"\n";
}
}
