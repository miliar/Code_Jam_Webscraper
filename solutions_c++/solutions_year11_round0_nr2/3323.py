#include<iostream>
#include<vector>
#include<string>
using namespace std;
main()
{
int te,c,d,n,a,b,t,i,j,k;
string s;
cin>>te;
int cn=0;
while(te--)
{
cn++;
int co1[26][26]={0};
char co[26][26];
int op1[26]={0};
int op[26][26]={0};
cin>>c;
while(c--)
{
cin>>s;
a=int(s[0]-65);
b=int(s[1]-65);
co[a][b]=s[2];
co[b][a]=s[2];
co1[a][b]=1;
co1[b][a]=1;
}
cin>>d;
while(d--)
{
cin>>s;
a=int(s[0]-65);
b=int(s[1]-65);
op[a][b]=1;
op[b][a]=1;
op1[a]=1;
op1[b]=1;
}
cin>>n;
vector<int>flag(n,1);
cin>>s;
int flaga;
for(i=1;i<n;i++)
{
flaga=0;
a=int(s[i]-65);
//b=int(s[i-1]-65);
for(k=i-1;k>=0;k--)
{
if(flag[k]==1)
{
flaga=1;
b=int(s[k]-65);
break;
}
}
if(flaga==1 && co1[a][b]==1)
{
s[i]=co[a][b];
flag[k]=0;
}
else if(flaga==1 && op1[a]==1)
{
for(j=k;j>=0;j--)
{
if(flag[j]==0)
continue;
t=int(s[j]-65);
if(op[a][t]==1)
{
fill(flag.begin(),flag.begin()+(i+1),0);
break;
}
}
}
}
int flagb=0;
string s1="";
int cnt=0;
for(i=0;i<n;i++)
{
if(flag[i]==1)
cnt++;
}
if(cnt==0)
cout<<"Case #"<<cn<<": []"<<"\n";
else
{
s1+="[";
for(i=0;i<n;i++)
{
if(flag[i] && flagb==0)
{
flagb=1;
s1+=s[i];
}
else if(flag[i] && flagb==1)
{
s1+=", ";
s1+=s[i];
}
}
s1+=']';
cout<<"Case #"<<cn<<": "<<s1<<"\n";
}
}
}
