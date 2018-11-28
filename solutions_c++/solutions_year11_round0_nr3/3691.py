#include<stdio.h>
long cas,cas1,n,sum,i,j,output;
long A[1009];
long p1,p2,min;

int main()
{

//    freopen("C-large.in","r",stdin);
//   freopen("C-large.out","w",stdout);


scanf("%ld",&cas);

for(cas1=1;cas1<=cas;cas1++)
{
scanf("%ld",&n);

min = 0;

for(i=0;i<n;i++)
{
scanf("%ld",&A[i]);
if(i==0)
min = A[i];
else if(A[i]<min)
min = A[i];
}           

p1 = A[0];
sum = A[0];

for(i=1;i<n;i++)
{
p1 = p1 ^ A[i];
sum+=A[i];
}

sum -= min;

if(p1!=0)
printf("Case #%ld: NO\n",cas1);
else
{
printf("Case #%ld: %ld\n",cas1,sum);
}                           
}    
    
return 0;    
}
