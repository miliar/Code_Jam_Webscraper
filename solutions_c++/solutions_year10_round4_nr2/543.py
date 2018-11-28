#include <stdio.h>
const long long INF =1000000000000000LL;
int i,j,n,it,t,p;
int mas[10000],m[10000];
long long pr[10000];
long long chasvla(int k, int a,int b)
{
if(a==b-1)
   {
   if(m[a]>1||m[b]>1)
      return INF;
   if(m[a]==1||m[b]==1)
      {
      return pr[k];
      }
   return 0;
   }
int i;
long long k1=chasvla((k<<1)+1,a,(a+b)>>1) + chasvla ( (k<<1)+2, ((a+b)>>1) +1, b);
if(k1>INF) k1=INF;
for(i=a;i<=b;i++)
   m[i]--;
long long k2=pr[k]+chasvla((k<<1)+1,a,(a+b)>>1) + chasvla ( (k<<1)+2, ((a+b)>>1) +1, b);
for(i=a;i<=b;i++)
   m[i]++;
if(k1>k2)
   k1=k2;
return k1;
}
int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
scanf("%d",&t);
for(it=1;it<=t;it++)
   {
   scanf("%d",&p);
   n=(1<<p);
   for(i=0;i<(n<<1);i++)
      mas[i]=0;
   for(i=0;i<n;i++)
      {
      scanf("%d",&m[i]);
      m[i]=p-m[i];
      }
   for(i=p-1;i>=0;i--)
      {
      for(j=0;j<(1<<i);j++)
         scanf("%I64d",&pr[(1<<i)-1+j]);
      }
   printf("Case #%d: %I64d\n",it,chasvla ( 0, 0,n-1 ) );
   }
return 0;
}
