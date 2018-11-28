#include<iostream>
#include<cstdio>
#include<string>
#include<sstream>
#include<cctype>
#include<cstdlib>
#include<utility>
#include<set>

using namespace std;

set< pair<int,int> >myset;
int digitc(int a)
{
int c=0;
while(a!=0)
{
c++;
a/=10;
}
return c;
}
int recycled(int a,int b)
{
string s,st;int count=0,i,j;
stringstream s2;
s2<<a;
s=s2.str();
s=s+s;
int d=digitc(a);
for(i=1;i<s.length()-d;i++)
{                           long long int num=0;
for(j=i;j<i+d;j++)
{
num=num*10+(s[j]-'0');
}
if(num>a&&num<=b)
{
myset.insert(make_pair(a,num));
}
}
return 0;
}
int main()
{
int a,b,i;
int t,ch=0;
cin>>t;
while(t--)
{
          ch++;
scanf("%d%d",&a,&b);
 int res=0;
for(i=a;i<b;i++)
res=res+recycled(i,b);
printf("Case #%d: %d\n",ch,myset.size());
myset.clear();
}
return 0;
}



