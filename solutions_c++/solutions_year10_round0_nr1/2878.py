#include<stdio.h>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
   long t,n;
   long k;
   int i;
    int ii;
	int sum;
   scanf("%ld",&t);
  
   if(t>=1&&t<=10000)
   {
	   for(i=0;i<t;i++){
	       scanf("%ld%ld",&n,&k);
		   if(n>=1&&n<=30&&k>=0&&k<=100000000)
		   {
			   sum=1;
			   for(ii=0;ii<n;ii++)
			   {
				   sum*=2;
			   }
			
          
			 if(k%sum==sum-1)
			  {
				  printf("Case #");
				  printf("%d",1+i);
				  printf(": ON\n");
			  }
			 
			  else 
			  {
				  printf("Case #"); 
				  printf("%d",1+i);
				  printf(": OFF\n");
			  }

		   }
	       
	   }
   }
   return 0; 
}
