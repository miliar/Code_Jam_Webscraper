#include<stdio.h>
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
	int t;
	long r,k;
	int n;
	int i,j;
	int g[1000];
	int ii;
	int sum;
	int eums;
	int m=0;
	scanf("%d",&t);
	if(t>=1&&t<=50)
	{
		for(i=0;i<t;i++)
		{
			eums=0;
		     ii=0;
	   scanf("%d%d%d",&r,&k,&n);//100 10 1
	    if(r>=1&&r<=100000000&&k>=1&&k<=1000000000&&n>=1&&n<=100)
		{
             for(j=0;j<n;j++)
                scanf("%d",&g[j]);
			   g[++j]=0;
			   for(j=0;j<r;j++){
				   sum=0;
				
			   while(g[ii]!='\0')
			   {
                
				 if(sum+g[ii]<=k)
				 {
				 
			      sum+=g[ii];
				  ii++;
				  m++;
				  if(ii==n)
					  ii=0;
				  if(m>=n)
				  {
				      m=0;
					  eums+=sum;
					  break;
				  }
				 }
				 else 
				 {
                  eums+=sum;
				  m=0;
                  break;
				 }

			   }
		

			 }
			   	   printf("Case #%d: %d\n",i+1,eums);
             
		}

		}
	}

  return 0;
}
