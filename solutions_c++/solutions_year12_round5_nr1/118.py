#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

long P[2005];
long L[2005];
long h[2005];

bool cmp(long x,long y)
{
 long long a,b,c,d;
 
 a=(100-P[x])*100*L[y]+L[x]*10000;
 b=(100-P[y])*(100-P[x]);
 
 c=(100-P[y])*100*L[x]+L[y]*10000;
 d=(100-P[x])*(100-P[y]);
 
 return a*d<c*b||a*d==c*b&&x<y;
}

void work(long x)
{
 long n;
 long i,j;
 
 printf("Case #%ld:",x);
 
 memset(P,0,sizeof(P));
 memset(L,0,sizeof(L));
 memset(h,0,sizeof(h));
 scanf("%ld",&n);
 
 for(i=1;i<=n;i++)
   scanf("%ld",&L[i]);
 for(i=1;i<=n;i++)
   {
    scanf("%ld",&P[i]);
    h[i]=i;
   }
 
 sort(h+1,h+n+1,cmp);
 
 for(i=1;i<=n;i++)
   printf(" %ld",h[i]-1);
 printf("\n");
}

int main()
{
 long t;
 
 freopen("1.in","r",stdin);
 freopen("1.out","w",stdout);
 
 scanf("%ld",&t);
 for(long i=1;i<=t;i++)
   work(i);
 
 return 0;
}
