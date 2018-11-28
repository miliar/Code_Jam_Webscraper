/*#include <stdio.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#define eps 1e-8

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	double a,b;
	int T,n,L,P,C,i,j,x,k,t;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d%d%d",&L,&P,&C);
		i=1,j=0;		
		a = 1.0*P/L;	
		b = log(a)/log(C);	
		b++;
		if(b - (int)b <= eps)
		b--;
		i = b;	
		for(k=0;;k++)
		{
			if(1<<k>=i)
			break;
		}
		printf("Case #%d: %d\n",t,k);
	}
	return 0;
}*/

#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	long long T,n,L,P,C,i,j,x,k,t;
	scanf("%I64d",&T);
	for(t=1;t<=T;t++){
		scanf("%I64d%I64d%I64d",&L,&P,&C);
		i=1,j=0;
		int TT=L*C;
   	    while(TT<P)
    	{
           TT*=C;
           i++;
         }
         for(k=0;;k++)
        {
            if(1<<k>=i)
           break;
       }
       printf("Case #%I64d: %I64d\n",t,k);
	}
	return 0;
}

