#include<iostream>
using namespace std;
 
 
 
 
 
 
 
 
 
int main()
{
 
int t;
cin>>t;
int a[1000];
int n,s,p;
int i,j,k,m,l;
for(j=1;j<=t;j++)
{
 
cin>>n>>s>>p;
 
k=n;
m=p;
l=p;
for(i=0;i<n;i++)
{
cin>>a[i];
}
if(3*p-4<=0)
{
m=-1;
}
if(3*p-4<=0)
{
l=-1;
}
 
for(i=0;i<n;i++)
{
if(a[i]<(p*3))
{
if(a[i]!=(3*p-2) && a[i]!=(3*p-1))
{
if(s==0)
{
k--;
}
else if(s!=0)
{
 
 
if(a[i]!=(3*m-4) && a[i]!=(3*l-3))
{
k--;
}
else
{
s--;
}
}
}
}
}
cout<<"Case #"<<j<<": "<<k<<"\n";
}
}