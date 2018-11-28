#include <iostream>
#include <string>
#include <sstream>
using namespace std;
string s[2000];
string st;
int i,n,it,t;
bool metia(string a,string b)
{
return (a.size()>b.size() || (a.size()==b.size()&&a>b) );
}
string sxvaoba(string a,string b)
{
if(metia(b,a)) swap(a,b);
while(a.size()!=b.size())
   b="0"+b;
int i=a.size();
for(i--;i>=0;i--)
   if(a[i]>=b[i])
      a[i]=a[i]-b[i]+'0';
   else
      {
      a[i-1]--;
      a[i]= a[i]-b[i]+'0'+10;
      }
while(!a.empty() && a[0]=='0') a.erase(0,1);
if(a.empty()) a="0";
return a;
}
string nashti(string a,string b)
{
if(metia(b,a)) return a;
if(a==b) return "0";
string c=b;
while(a.size()>c.size()+1)
   c=c+"0";
while(metia(a,c))
   a=sxvaoba(a,c);
if(a==b) return "0";
if(metia(b,a)) return a;
return nashti(sxvaoba(a,b),b);
}
string usg(string a,string b)
{
while( a!="0" && b!="0" )
   if(metia(a,b))
      a=nashti(a,b);
   else
      b=nashti(b,a);
if(a=="0") return b;
else return a;
}
int USG(int a,int b)
{
while(a&&b)
   if(a>b)
      a%=b;
   else
      b%=a;
return a+b;
}
int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
cin>>t;
for(it=1;it<=t;it++)
   {
   cout<<"Case #"<<it<<": ";
   cin>>n;
   for(i=0;i<n;i++)
      cin>>s[i];
   st="0";
   for(i=1;i<n;i++)
      st = usg ( st, sxvaoba (s[i],s[i-1]) );
   cout<<nashti(sxvaoba(st,nashti(s[0],st)),st)<<endl;
   }
return 0;
}
