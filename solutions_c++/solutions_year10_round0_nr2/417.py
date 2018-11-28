#include<stdio.h>

__int64 cas,cas1,n,A[1009],min,low,result,i;

__int64 GCD(__int64 x, __int64 y)
{
__int64 z;

while(y!=0)
{
z = x % y;
x = y;
y = z;
}
return x;
}


int main()
{

//   freopen("B-small-attempt0.in","r",stdin);
//   freopen("B-small-out.out","w",stdout);

scanf("%I64d",&cas);    
    
for(cas1=1;cas1<=cas;cas1++)
{
scanf("%I64d",&n);

for(i=0;i<n;i++)
scanf("%I64d",&A[i]);

min = A[0];

for(i=0;i<n;i++)
if(A[i]<min)
{
min = A[i];
}

low = -1;

for(i=0;i<n;i++)
if(A[i]!=min)
{
if(low==-1)
low=(A[i]-min);
else
low = GCD(A[i]-min,low);
}

if(low == -1)
low = min;

result = 0;

if(min%low!=0)
{
result = ((min/low) + 1 ) * low - min;
}

printf("Case #%I64d: %I64d\n",cas1,result);

}    
       
return 0;    
}
