#include<iostream>
#include<string>
#include<vector>
#define pb push_back
using namespace std;

int main()
{
int l,d,n;
cin>>l>>d>>n;
vector<string>v;


for(int i=0;i<d;i++)
{
string s="";
cin>>s;
v.pb(s);
}
int ans=0;
for(int i=0;i<n;i++)
{ string s="";
cin>>s;
vector<string>vs;
for(int j=0;j<s.size();j++)
{
if(s[j]=='(')
{
string p="";
while(1)
{

j++;
if(s[j]==')')break;
p+=s[j];
}

if(p.size()==0)vs.pb("");
else vs.pb(p);
}
else
{
string p="";
p+=s[j];
vs.pb(p);
}
}

int ct=0;
for(int j=0;j<d;j++)
{
//cout<<v[j]<<endl;
string ss[l];
for(int k=0;k<l;k++)
{
ss[k]+=v[j][k];
}

int cc=0;
for(int k=0;k<l;k++)
{
//cout<<vs[k]<<" "<<ss[k]<<endl;
if(vs[k].find(ss[k])!=string::npos)cc++;
}
if(cc==l)ct++;
}
cout<<"Case #"<<i+1<<": "<<ct<<endl;
}


return 0;
}
