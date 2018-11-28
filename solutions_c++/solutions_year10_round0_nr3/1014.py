#include<stdio.h>

__int64 cas,cas1,R,K,N,h1,h2,h3,h4,h5,h6,limit,sum,i,j,start;
__int64 A[1009],B[1009],C[1009];

int main()
{

//   freopen("C-large.in","r",stdin);
//   freopen("C-large-out.out","w",stdout);

scanf("%I64d",&cas);    
    
for(cas1=1;cas1<=cas;cas1++)
{    
scanf("%I64d %I64d %I64d",&R,&K,&N);

for(i=0;i<N;i++)
{
scanf("%I64d",&A[i]);    
B[i]=-1;
C[i]=0;
}

sum=0;
start = 0;
for(i=0;i<R;i++)
{

if(B[start]!=-1)
break;

limit = 0;
j = start;

while(limit+A[start]<=K)
{
limit+=A[start];
start++;
start %=N;
if(start==j)
break; 
}

B[j]=i;
C[i]=limit;
sum+=limit;

}

if(i!=R)
{
h1 = R - i;
h2 = i - B[start];
h3 = h1/h2;
h4 = h1%h2;
h5=0;
h6=0;
for(j=B[start];j<i;j++)
{
h5+=C[j];
if(h6<h4)
sum+=C[j];
h6++;
}
sum+=(h5*h3);
}
 
 printf("Case #%I64d: %I64d\n",cas1,sum);
    
}    
return 0;    
}
