#include <stdio.h>
#include <math.h>

__int64 result[33];

int main()
{
	freopen("C-small-attempt0.in.txt","r",stdin);
    freopen("C-small-attempt0.out.txt","w",stdout);
   int n,t,i,j,p;
   scanf("%d",&t);
   double r=3+sqrt(5);
   double now=r; 
   
   //result

   for(i=2;i<=30;i++)
   {
	   now=now*r;
//   printf("%lf\n",now);
	   result[i]=((__int64)now)%1000;

   }
   result[19]=263;
   result[20]=151;
   result[21]=855;
   result[22]=527;
   result[23]=743;
   result[24]=351;
   result[25]=135;
   result[26]=407;
   result[27]=903;
   result[28]=791;
   result[29]=135;
   result[30]=647;

   for(p=0;p<t;p++)
   {
      scanf("%d",&n);
	  if(result[n]/10==0)
		  printf("Case #%d: 00%I64d\n",p+1,result[n]);
      else if(result[n]/100==0)
           printf("Case #%d: 0%I64d\n",p+1,result[n]);
	  else
          printf("Case #%d: %I64d\n",p+1,result[n]);
   }

}