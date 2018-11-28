#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
int main()
{
int l,d,n,testcaseno;
int i,j,k,answer,temp,dscount;
int queue[500],tempqueue[500];

string ds[5000];
string ns[500];
bool dsb[5000],dsb1[5000];
string tempns;
int tempnslen;

while(scanf("%d",&l)!=EOF)
{
testcaseno=0;

scanf("%d%d",&d,&n);
getline(cin,ds[0],'\n');

for(i=0;i<d;i++)
getline(cin,ds[i],'\n');

for(i=0;i<n;i++)
getline(cin,ns[i],'\n');


for(i=0;i<n;i++)
{
testcaseno++;
tempns=ns[i];
tempnslen=tempns.length();
for(j=0;j<d;j++)
dsb[j]=true;
dscount=0;
for(j=0;j<tempnslen;j++)
{
if(tempns.at(j)!='(')
{
for(k=0;k<d;k++)
if(dsb[k]==true&&tempns.at(j)!=ds[k].at(dscount))
dsb[k]=false;
}
else
{
for(k=0;k<d;k++)
dsb1[k]=false;
while(tempns.at(j)!=')')
{
for(k=0;k<d;k++)
if(dsb1[k]==false&&tempns.at(j)==ds[k].at(dscount))
dsb1[k]=true;
j++;
}
for(k=0;k<d;k++)
dsb[k]=dsb[k]&&dsb1[k];

}
dscount++;
}

answer=0;
for(j=0;j<d;j++)
if(dsb[j]==true)
answer++;
printf("Case #%d: %d\n",testcaseno,answer);
}

}



return 0;
}
