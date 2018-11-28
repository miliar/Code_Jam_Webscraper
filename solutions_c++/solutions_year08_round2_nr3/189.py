// swarnaprakash

// modified MY accepted code for problem CTRICK in Spoj

#include<stdio.h>

#define M 20005

struct card{
int index;
int next;
}c[M];

int main()
{
int t,n,i,j,o[M],p,x;
int tc;
int k,a[M];

scanf("%d",&tc);

for(t=1;t<=tc;++t)
{
scanf("%d",&n);
scanf("%d",&k);
for(i=0;i<k;++i)
	scanf("%d",&a[i]);
	
for(i=0;i<n;++i)
{
c[i].index=i;
c[i].next=i+1;
}
c[n-1].next=0;


p=n-1;

for(i=0;i<n;++i)
{
 for(j=0;j<i;++j)
   p=c[p].next;

 x=c[p].next;
 o[c[x].index]=i+1;
 c[p].next=c[x].next;
 
}

printf("Case #%d:",t);
for(i=0;i<k;++i)
 printf(" %d",o[a[i]-1]);
printf("\n");


}
return 0;
}
