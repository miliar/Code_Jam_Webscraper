#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int r,c,d,n,i,j,l,k,a[105];
string cs[40],ds[40],s,t;
cin>>r;
for(l=1;l<=r;l++)
{
cin>>c;
for(i=1;i<=c;i++) cin>>cs[i];
cin>>d;
for(i=1;i<=d;i++) cin>>ds[i];
cin>>n>>s;
t="";
for(i=0;i<s.length();i++)
{
for(j=1;j<=c;j++) if(t[t.length()-1]==cs[j][0] && s[i]==cs[j][1] || t[t.length()-1]==cs[j][1] && s[i]==cs[j][0]) {t[t.length()-1]=cs[j][2]; break;}
if(j>c)
{
t+=s[i];
for(j=0;j<t.length();j++)
{
for(k=1;k<=d;k++)
{
if(t[j]==ds[k][0] && s[i]==ds[k][1] || t[j]==ds[k][1] && s[i]==ds[k][0]) {t=""; break;}
}
}
}
}
cout<<"Case #"<<l<<": [";
if(t.length()>0)
{
cout<<t[0];
for(i=1;i<t.length();i++)
{
cout<<", "<<t[i];
}
}
cout<<"]"<<endl;
}
return 0;
}