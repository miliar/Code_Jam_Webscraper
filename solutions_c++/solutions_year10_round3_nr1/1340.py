#include<cstdio>
#define MAX 1005

int A[MAX],B[MAX],t,n,i,j,k,res;

int main()
{
scanf("%d",&t);
for(i=0;i<t;++i)
   {
   scanf("%d",&n);
   res=0;
   for(j=0;j<n;++j) scanf("%d%d",&A[j],&B[j]);
   for(j=0;j<n;++j)
      for(k=j+1;k<n;++k)
         if(((A[j]<A[k])&&(B[j]>B[k]))||((A[j]>A[k])&&(B[j]<B[k]))) ++res;
   printf("Case #%d: %d\n",i+1,res);
   }
return 0;
}
