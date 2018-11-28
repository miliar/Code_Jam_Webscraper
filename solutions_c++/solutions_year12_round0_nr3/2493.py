#include<iostream>
#include<cmath>
using namespace std;
int t,a,b,n,j,dig[10],tmp[10];
long long int ans,y;
inline long long int f(int x)
{
y=0;
n=0;
j=x;
while(j!=0)
{
tmp[n]=j%10;
n++;
j/=10;
}
for(int i=0;i<n;i++)
{
dig[i]=tmp[n-1-i];
}

int last=0;
int first=x;
int num;
for(int i=n-1;i>0;i--)
{
last=last+dig[i]*pow(10,n-1-i);
first=(x-last)/pow(10,n-i);
num=pow(10,i)*last+first;
if(num==x)
break;
if(num>=a && num<=b)
y++;
}
return y;
}
int main()
{
cin>>t;
for(int i1=0;i1<t;i1++)
{
ans=0;
cin>>a>>b;
for(int i=a;i<=b;i++)
{
ans+=f(i);
}
cout<<"Case #"<<i1+1<<": "<<ans/2<<endl;
}
return 0;
}
