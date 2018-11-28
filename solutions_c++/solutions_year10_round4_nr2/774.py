#include<stdio.h>

long cas,cas1,p,i,j,k,cost,M;
long B[12][2000],A[20];

int main()
{

   freopen("B-small-attempt0.in","r",stdin);
   freopen("B-small-out.out","w",stdout);

A[0]=1;

for(i=1;i<=13;i++)
A[i]=A[i-1]*2;

scanf("%ld",&cas);

for(cas1=1;cas1<=cas;cas1++)
{
scanf("%ld",&p);

for(i=0;i<p;i++)
for(j=0;j<A[p];j++)
B[i][j]=0;

cost = 0;

for(i=0;i<A[p];i++)
{
scanf("%ld",&k);

M = i/2;

for(j=0;j<p;j++)
{
if(k==0)
{
if(B[j][M]==0)
{
cost++;
B[j][M]=1;
}
}
else
{
if(B[j][M]==0)
{
k--;
}
}
M = M / 2;
}
}

for(i=p-1;i>=0;i--)
{
for(j=0;j<A[i];j++)
scanf("%ld",&k);
}

printf("Case #%ld: %ld\n",cas1,cost);

}

return 0;
}
