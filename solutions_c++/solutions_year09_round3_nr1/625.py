#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;
int retval(char a)
{
if(a>='0' && a<='9')
return a-48;
else if (a>='a' && a<='z')
return a-87;
return -1;
}

int main()
{
long long int answer;
int nooftest,testcount;
char q[64];
cin>>nooftest;getchar();

for(testcount=1;testcount<=nooftest;testcount++)
{
cin>>q;
int n=strlen(q);
if(n==0){
cout<<"Case #"<<testcount<<": "<<"0"<<endl;continue;}
if(n==1){cout<<"Case #"<<testcount<<": "<<"1"<<endl;continue;}
int j;
int i;int flag;
answer=0;
int l=0;
for(i=0;i<n;i++)
{
flag=1;
for(j=0;j<i;j++)
{
	if(q[j]==q[i])	
	{flag=0;break;}
}
if(flag==1)
l++;
}
int cur=0;
int numarray[64];
numarray[0]=0;

for(i=0;i<n;i++)
{
flag=0;
for(j=0;j<i;j++)
if(q[i]==q[j])
{numarray[i]=numarray[j];flag=1;break;}
if(flag==0)
numarray[i]=cur++;
}
int k;

for(i=0;i<n;i++)
{
if(numarray[i]==0)
numarray[i]=99;
}

for(i=0;i<n;i++)
{
if(numarray[i]==1)
numarray[i]=0;
}


for(i=0;i<n;i++)
{
if(numarray[i]==99)
numarray[i]=1;
}

if(l==1)
l=2;
long long int base=1;

for(i=n-1;i>=0;i--)
{
answer+=(base*numarray[i]);
base*=l;
}

cout<<"Case #"<<testcount<<": "<<answer<<endl;



}



}
