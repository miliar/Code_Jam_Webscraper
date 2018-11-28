#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int t,tt,i,a[105],n,s,p,x,y,z,k;
cin>>tt;
for(t=1;t<=tt;t++)
{
cin>>n>>s>>p;
k=0;
for(i=1;i<=n;i++)
{
cin>>a[i];
}
sort(a+1,a+n+1);
for(i=1;i<=n;i++)
{
x=a[i]/3;
a[i]-=x;
y=a[i]/2;
a[i]-=y;
z=a[i];
if(z>=p) k++;
else if(x==y && x==z && s>0 && z+1>=p && x>0) k++,s--;
else if(x==y-1 && x==z-1 && s>0 && z+1>=p) k++,s--;
}
cout<<"Case #"<<t<<": "<<k<<endl;
}
return 0;
}