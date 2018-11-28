#include<iostream>
#include<string>
#include<math.h>
#include<algorithm>
#include<string>
using namespace std;
long long po(long long x, long long y)
{   if(y!=0)
    {
        x=1;
    while(y>0)
    {
  x=x*2;
  y--;
    }
    return x;
    }
    else
    return 1;
}
int main()
{  long long a,ans,i,x1,h;
   long long t,m,n,k,p;
   freopen("A2.in","r",stdin);
   freopen("out.txt","w",stdout);
  long long po(long long,long long);
   cin>>t;
   i=1;
for(a=1;a<=t;a++)
  {
      x1=0;
  ans=0;
   cin>>n>>k;
   for(i=1;i<=n;i++)
   {
   x1=po(2,(i-1));
   ans+=x1;
   }
 m=k+1;
 ans=ans+1;
 h=m%ans;
if(h==0)
{
cout<<"Case #"<<a<<": ON"<<endl;
}
else
{
cout<<"Case #"<<a<<": OFF"<<endl;
}

  }
}

