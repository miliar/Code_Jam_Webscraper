#include<iostream>
#include<stdio.h>
using namespace std;
void get(int op,int bp,int k,int &ans,int o[],int b[],int ob[][2],int opk,int bpk,int n)
{
if(k==n)
return;
if(ob[k][0]==0)
{
ans++;
if(op<ob[k][1])
op++;
else if(op==ob[k][1])
{
opk++;
k++;
}
else
op--;
if(bpk!=-1)
{
if(bp<b[bpk])
bp++;
else if(bp>b[bpk])
bp--;
}
}
else
{
ans++;
if(bp<ob[k][1])
bp++;
else if(bp==ob[k][1])
{
bpk++;
k++;
}
else
bp--;
if(opk!=-1)
{
if(op<o[opk])
op++;
else if(op>o[opk])
op--;
}
}
get(op,bp,k,ans,o,b,ob,opk,bpk,n);
}
int main()
{
int tc;
scanf("%d",&tc);
for(int i=0;i<tc;i++)
{
int n,p;
char r;
scanf("%d",&n);
int ind1=0,ind2=0;
int o[n],b[n],ob[n][2];
for(int j=0;j<n;j++)
{
cin>>r;
scanf("%d",&p);
if(r=='O')
{
ob[j][0]=0;
ob[j][1]=p;
o[ind1]=p;
ind1++;
}
else
{
ob[j][0]=1;
ob[j][1]=p;
b[ind2]=p;
ind2++;
}
}
int op=1,bp=1;
int k=0;
int ans=0;
int opk=0,bpk=0;
if(ind1==0)
opk=-1;
if(ind2==0)
bpk=-1;
get(op,bp,k,ans,o,b,ob,opk,bpk,n);
cout<<"Case #"<<i+1<<": "<<ans<<endl;
}
return 0;
}
