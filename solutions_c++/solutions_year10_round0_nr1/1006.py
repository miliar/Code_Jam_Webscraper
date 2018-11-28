#include<stdio.h>

long cas,cas1,n,k,yes,i;

int main()
{

//   freopen("A-large.in","r",stdin);
//   freopen("A-large-out.out","w",stdout);

scanf("%ld",&cas);

for(cas1=1;cas1<=cas;cas1++)
{
scanf("%ld %ld",&n,&k);

yes = 1;

for(i=0;i<n;i++)
{
if(k%2!=1)
{
yes = 0;
break;
}
k=k/2;
}

if(yes==1)
printf("Case #%ld: ON\n",cas1);
else
printf("Case #%ld: OFF\n",cas1);
}
return 0;
}
