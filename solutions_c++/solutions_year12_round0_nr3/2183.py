#include<stdio.h>
main()
{
	int t,a,b,c=1;
	scanf("%d",&t);
	while(t--)
	{
		int count = 0;
		int d,r,tr,p2 = 1;
		scanf("%d",&a);
		scanf("%d",&b);
		int n = a;
		n = n/10;
		while(n){p2*=10; n = n/10;}
		int p3 = p2;
			for(int j=10;j<=p2;j*=10)
			{		
				for(int i=a;i<b;i++)
				{	
					d = i/j;
					r = i%j;
					tr = (r*p3)+d;
					if(tr > i && tr <= b )
					{count++;}
						
				}
				p3/=10;
			}	
		printf("Case #%d: %d\n",c,count);
		c++;
		
	}
}
