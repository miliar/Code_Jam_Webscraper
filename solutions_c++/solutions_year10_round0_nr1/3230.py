#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
long long a[35];
int n,x,y,i;
cin>>n;
a[0]=1;
for(i=1;i<=30;i++)
{
a[i]=a[i-1]*2;
}
for(i=1;i<=n;i++)
{
cin>>x>>y;
cout<<"Case #"<<i<<": ";
if((y+1)%a[x]==0)
{
cout<<"ON"<<endl;
}
else
{
cout<<"OFF"<<endl;
}
}
return 0;
}