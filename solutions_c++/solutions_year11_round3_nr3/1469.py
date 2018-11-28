#include<iostream>
using namespace std;
long long int gcd(long long int a,long long int b)
{
if(b==0)return a;
else
return gcd(b,a%b);
}
main()
{
long long int g,i,t,x,n,l,h,pr,j,fl,fl1;
cin>>t;fl=0;
for(x=1;x<=t;x++)
{
cin>>n>>l>>h;fl=0;
long long int a[n],a1[n];
pr=1;
for(i=0;i<n;i++)
{cin>>a[i];}
for(i=l;i<=h;i++)
{fl=0;
for(j=0;j<n;j++)
{if((a[j]%i!=0)&&(i%a[j]!=0)){fl=1;break;}}
if(!fl)break;
}
//cout<<i<<"\n";
if(fl)cout<<"Case #"<<x<<": "<<"NO\n";
else cout<<"Case #"<<x<<": "<<i<<"\n";
}
return 0;
}
