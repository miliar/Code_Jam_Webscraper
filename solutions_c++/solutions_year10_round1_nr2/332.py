#include<stdio.h>

long Dif(long x,long y)
{
if(x>=y)     
return x-y;     
else
return y-x;     
}

long cas,cas1,D,I,M,N,i,j,k,l,a,min;
long A[109],B[109][260];

int main()
{

// freopen("B-large.in","r",stdin);
// freopen("B-large-out.out","w",stdout);
 
scanf("%ld",&cas);    
    
for(cas1=1;cas1<=cas;cas1++)
{    
 scanf("%ld %ld %ld %ld",&D,&I,&M,&N);
 
 for(i=0;i<N;i++)
 {
 scanf("%ld",&A[i]);
 for(j=0;j<=255;j++)
 B[i][j]= D * (i+1);
 }
 
 for(j=0;j<=255;j++)
 if(Dif(A[0],j)<B[0][j])
 B[0][j]=Dif(A[0],j);
 
 if(M!=0)
 for(j=0;j<=255;j++)
 {
 
 for(k=0;k<=255;k++) 
 {
   l = Dif(k,j);
   a = l / M;
   if(l%M!=0)
   a++;
   if(B[0][j]+a*I<B[0][k])
   B[0][k] = B[0][j]+a*I;
 }             
 }
 
 for(i=1;i<N;i++)
 for(j=0;j<=255;j++)
 {
 if(B[i-1][j]+D<B[i][j])
    B[i][j]=B[i-1][j]+D;
    
 for(k=0;k<=255;k++)
 if(Dif(j,k)<=M)
 {
    if(B[i-1][k]+Dif(j,A[i])<B[i][j])
    B[i][j]=B[i-1][k]+Dif(j,A[i]);
 }
 
 if(M!=0)
 for(k=0;k<=255;k++) 
 {
   l = Dif(k,j);
   a = l / M;
   if(l%M!=0)
   a++;
   if(B[i][j]+a*I<B[i][k])
   B[i][k] = B[i][j]+a*I;
 }
 
 }
 
 min = N * D;
 
 for(j=0;j<=255;j++)
 if(B[N-1][j]<min)
 min = B[N-1][j];
 
 printf("Case #%ld: %ld\n",cas1,min);   
    
}    
return 0;    
}
