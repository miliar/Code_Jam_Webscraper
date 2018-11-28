#include<iostream>
#include<cmath>
using namespace std;
int main()
{
int tc;
cin>>tc;
for(int u=0;u<tc;u++)
{
int n,l,h;
cin>>n>>l>>h;
int a[n];
for(int i=0;i<n;i++)
{
cin>>a[i];
}
int bit=0;
for(int i=l;i<=h;i++)
{
int q=0;
for(int j=0;j<n;j++)
{
if(a[j]%i==0 || i%a[j]==0)
{
q++;
if(q==n)
{
cout<<"Case #"<<u+1<<": "<<i<<endl;
bit=1;
break;
}
}
}
if(bit==1)
break;
}
if(bit==0)
cout<<"Case #"<<u+1<<": NO"<<endl;
}
return 0;
}
