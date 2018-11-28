#include<stdio.h>
#include<math.h>

int main()
{
	freopen("a.in","r", stdin);
	freopen("a.out","w+", stdout);
	long int a, b,tCase, c, d, i, j, k, l, count;

	scanf("%ld", &tCase);

	for(i=1; i<=tCase; i++)
	{
		scanf("%ld %ld", &a, &b);
	d=log10(a);
	count=0;
		for(j=a; j<=b; j++)
		{	
			
			for(k=10, l=d; k<=pow(10, d) && l>0; k=k*10, l--)
			{
		
				c=(j%k)*pow(10,l)+(j/k);

				if(c!=j && c<=b && c>=a)
	
					count++;

			}
					

			
		}
		if(d>2)
			count=count-1;

		printf("Case #%ld: %ld\n",i, count/2);
	}



	

	return 0;
}