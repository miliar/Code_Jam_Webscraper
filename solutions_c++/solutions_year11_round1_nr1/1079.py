#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<memory.h>
#include<algorithm>
#include<string.h>
#define inf 999999999
#define eps 1e-8
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)>(b)?(b):(a))
typedef __int64 LL;
using namespace std;
FILE *f=fopen("A.out","w");
LL gcd(LL a,LL b)
{
	if(b==0) return a;
	else return gcd(b,a%b);
}

int main()
{
  int ca,test=0;
  LL n,p,q,y,d,m,i;
  scanf("%d",&ca);
  while(ca--)
  {
  fprintf(f,"Case #%d: ",++test);
  scanf("%I64d%I64d%I64d",&n,&p,&q);
   
  if((p>0 && q==0)  || (p<100 && q==100)) fprintf(f,"Broken\n");
  else 
  {
	  for(i=1;i<=n;i++)
	  if(i*p%100==0) break;
	  if(i<=n) fprintf(f,"Possible\n");
	  else fprintf(f,"Broken\n");
  }

  }

  system("pause");
return 0;
}