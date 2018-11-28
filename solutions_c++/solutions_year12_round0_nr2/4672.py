#include<stdio.h>
int main()
{int t,i;
scanf("%d",&t);
for(i=1;i<=t;i++)
{
int n,s,a[103],p,count=0,j,u;
scanf("%d %d %d",&n,&s,&p);
for(j=0;j<n;j++)
scanf("%d",&a[j]);
for(j=0;j<n;j++)
{
u=(a[j]-p);
if(u>=0)
{  u=u/2;
if(u>=(p-1))
count++;
else if(u>=(p-2)&&u<(p-1))
{
if(s)
{ count++;
s--;
}
}
}}

printf("Case #%d: %d\n",t,count);
}
}
