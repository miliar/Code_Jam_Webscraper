#include<stdio.h>

long test,test1,i,j,k,n,m,in,a,b;
long X[109],Y[109],Z[109],A[109],A1[109];
long B[109],B1[109],Count_A,Count_B,time;
char te[109],c;

int main()
{
    
////freopen("B-small-attempt1.in","r",stdin);
/////freopen("B_small1_out.in","w",stdout);    
scanf("%ld",&test);

for(test1=1;test1<=test;test1++) 
{
in=0;
scanf("%ld",&time);
scanf("%ld %ld",&n,&m);

for(i=1;i<=n;i++)
{
scanf("%s",te);
sscanf(te,"%ld%c%ld",&j,&c,&k);
Y[in]=j*60+k;
scanf("%s",te);
sscanf(te,"%ld%c%ld",&j,&c,&k);
Z[in]=j*60+k;
X[in]=0;
in++;                
}

for(i=1;i<=m;i++)
{
scanf("%s",te);
sscanf(te,"%ld%c%ld",&j,&k);
Y[in]=j*60+k;
scanf("%s",te);
sscanf(te,"%ld%c%ld",&j,&k);
Z[in]=j*60+k;
X[in]=1;
in++;                
}


for(i=0;i<in-1;i++)
for(j=0;j<in-i-1;j++)
if(Y[j]>Y[j+1])
{
k=X[j];
X[j]=X[j+1];
X[j+1]=k;
k=Y[j];
Y[j]=Y[j+1];
Y[j+1]=k;
k=Z[j];
Z[j]=Z[j+1];
Z[j+1]=k;               
}
a=0;
b=0;    
Count_A=0;
Count_B=0;
for(i=0;i<in;i++)
{
if(X[i]==0)
{
k=-1;           
for(j=0;j<a;j++)
if(A[j]<=Y[i]&&A1[j]==1)
{k=1;A1[j]=0;break;}
if(k==-1)
Count_A++;
if(Y[i]<=Z[i])
{B[b]=Z[i]+time;B1[b]=1;b++;}
}                 
else                 
{                 
k=-1;           
for(j=0;j<b;j++)
if(B[j]<=Y[i]&&B1[j]==1)
{k=1;B1[j]=0;break;}
if(k==-1)
Count_B++;
if(Y[i]<=Z[i])
{A[a]=Z[i]+time;A1[a]=1;a++;}
}                 
}
  
printf("Case #%ld: %ld %ld\n",test1,Count_A,Count_B);    
    
}   
return 0;    
}
