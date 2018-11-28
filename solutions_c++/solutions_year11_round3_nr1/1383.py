#include<iostream>
#include<string>
#include<vector>
using namespace std;
main()
{
int te,n,m,i,j,flag,cn=0;
cin>>te;
vector<string>s(51);
while(te--)
{
cn++;
flag=0;
cin>>n>>m;
for(i=0;i<n;i++)
cin>>s[i];
for(i=0;i<n;i++)
{
for(j=0;j<m;j++)
{
if(s[i][j]=='#')
{
if((i+1)<n && (j+1)<m)
{
if(s[i+1][j]==s[i][j+1] && s[i+1][j+1]==s[i][j] && s[i+1][j]=='#')
{
s[i][j]=s[i+1][j+1]='/';
s[i+1][j]=s[i][j+1]='\\';
}
else
flag=1;
}
else
flag=1;
}
}
}

if(flag==1)
cout<<"Case #"<<cn<<":"<<"\n"<<"Impossible"<<"\n";
else
{
cout<<"Case #"<<cn<<":"<<"\n";
for(i=0;i<n;i++)
{
cout<<s[i]<<"\n";
}
}
}
}
