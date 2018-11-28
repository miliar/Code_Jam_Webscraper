#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;



int no(char chk[],int chks,int chke,string s,int ss)
{
int i,m;
if(chks>chke)
return 1;
else
{
for(i=ss;(s[i]!=chk[chks])&&(s[i]!='\n');i++);
if(s[i]=='\n')
return 0;
else
m=(no(chk,chks+1,chke,s,i+1)+no(chk,chks,chke,s,i+1))%10000;
return m;
}
}

int main()
{
char *chk="welcome to code jam";
int n,i,m=0,j;
char s[501];
cin>>n;
for(i=0;i<n+1;i++)
{
s[0]=getchar();
for(j=1;s[j-1]!='\n';j++)
s[j]=getchar();
if(i!=0)
{
m=no(chk,0,18,s,0);
cout<<"Case #"<<i<<": ";
if(m<10)
cout<<"000";
else 
{
if(m<100)
cout<<"00";
else 
{
if(m<1000);
cout<<"0";
}
}
cout<<m<<endl;

}
}
return 0;
}
