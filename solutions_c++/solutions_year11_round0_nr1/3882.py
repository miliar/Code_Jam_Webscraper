#include<stdio.h>
long cas,cas1,n,k1,k2,max,i,st,count;
long A[109],C[109],D[109];
long st1,st2,kk1,kk2,n1,flag;
char u[109],B[109];
int main()
{

  //  freopen("A-large.in","r",stdin);
   // freopen("A-large.out","w",stdout);


scanf("%ld",&cas);

for(cas1=1;cas1<=cas;cas1++)
{
scanf("%ld",&n);

k1 = 0;
k2 = 0;

for(i=0;i<n;i++)
{
scanf("%s %ld",&u,&A[i]);
B[i]=u[0];
if(B[i]=='O')
{
C[k1]=A[i];
k1++;
}
else
{
D[k2]=A[i];
k2++;
}
}                            

max = 0;
st1 = 1;
st2 = 1;
kk1 = 0;
kk2 = 0;
n1 = 0;

while(n!=n1)
{

flag = 0;

if(B[n1]=='O' && st1==A[n1])
{
   flag = 1;
   n1++;
   kk1++;
}
else if(kk1<k1 && st1>C[kk1])
st1--;
else if(kk1<k1 && st1<C[kk1])
st1++;

if(B[n1]=='B' && st2==A[n1] && flag==0)
{
   n1++;
   kk2++;
}
else if(kk2<k2 && st2>D[kk2])
st2--;
else if(kk2<k2 && st2<D[kk2])
st2++;

max++;
}



printf("Case #%ld: %ld\n",cas1,max);
                            
}    

return 0;    
}
