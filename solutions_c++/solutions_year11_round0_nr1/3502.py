#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
main()
{
int te,n,r,i,t,t1;
char c;
cin>>te;
int cn=0;
while(te--)
{
cn++;
int time=0,timeO=0,timeB=0,flagO=1,flagB=1;
cin>>n;
for(i=1;i<=n;i++)
{
cin>>c>>r;
if(c=='O')
{
t=abs(r-flagO);
flagO=r;
t1=time-timeO;
if(t1>=t)
{
time=time+1;
timeO=time;
}
else
{
time=time+(t-t1)+1;
timeO=time;
}
}
else if(c=='B')
{
t=abs(r-flagB);
flagB=r;
t1=time-timeB;
if(t1>=t)
{
time=time+1;
timeB=time;
}
else
{
time=time+(t-t1)+1;
timeB=time;
}
}
}
cout<<"Case #"<<cn<<": "<<time<<"\n";
}
}
