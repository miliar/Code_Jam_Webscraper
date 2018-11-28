#include<iostream>
using namespace std;

int is_next(long long int,long long int);
int is_neg(int *,int);

main()
{
FILE *ifp,*ofp;
int T,t;
ifp=fopen("small.in","r");
ofp=fopen("small.out","w");
long long int n,i;
//cin>>n;
fscanf(ifp,"%d\n",&T);
for(t=0;t<T;t++)
{
fscanf(ifp,"%lld",&n);
i=n+1;
while(!is_next(i,n))
i++;
fprintf(ofp,"Case #%d: %lld\n",t+1,i);
}
}

int is_next(long long int a,long long int n)
{
int n_dig[16],i=0,a_dig[16],j=0,r,l,m;
while(n!=0)
{
r=n%10;
if(r!=0)
n_dig[i++]=r;
n=(n-r)/10;
}
while(a!=0)
{
r=a%10;
if(r!=0)
a_dig[j++]=r;
a=(a-r)/10;
}

if(i!=j) return(0);

for(l=0;l<j;l++)
{
for(m=0;m<i;m++)
{
if(a_dig[l]==n_dig[m])
{
a_dig[l]=-1;n_dig[m]=-1;
break;
}
}
}

if((is_neg(a_dig,j))&&(is_neg(n_dig,i))) return(1);
else return(0);
}

int is_neg(int a[],int n)
{
int i;
for(i=0;i<n;i++)
{
if(a[i]>=0) 
return(0);
}
return(1);
}
