# include<iostream>
#include<math.h>
using namespace std;
int count (int x)
{
int c=0;
while(x!=0)
{
x=x/10;
c++;
}
return c;
}
int main()
{
int ctr=0,rem,m,n,i,j,l,y,t,k,a[50];
cin>>t;
for(k=0;k<t;k++)
{ 
    ctr=0;
cin>>m>>n;
for(i=m;i<n;i++)
{
for(j=i+1;j<=n;j++)
{
if (count(i)==count(j))
{
l=count(j);
y=j;
while(l!=0)
{
rem=y%10;
y=y/10;
y=rem*pow(10,count(j)-1)+y;
if(i==y)
{

ctr++;
break;
}
l--;
}
}}}
a[k]=ctr;}
for(i=0;i<t;i++)
cout<<"case #"<<i+1<<": "<<a[i]<<endl;
return 0;
}

