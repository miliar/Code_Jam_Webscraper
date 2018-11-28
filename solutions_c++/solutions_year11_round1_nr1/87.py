#include <stdio.h>
#include <stdlib.h>

__int64 gcd(__int64 a, __int64 b)
{
	if(b==0)
		return a;
	return gcd(b,a%b);
}

int main()
{
	__int64 n,pd,pg,a,b,c,d,g1,g2,i,no;
	int cas,asd;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%I64d %I64d %I64d",&n,&pd,&pg);

		g1 = gcd(pd,100);
		c = pd / g1;
		d = 100 / g1;

		g2 = gcd(pg,100);
		a = pg / g2;
		b = 100 / g2;

		printf("Case #%d: ",asd+1);

/*		no = 0;
		for(i=1;i<=n;i++)
		{
			if(n%d == 0)
			{
				tmp = c * n/d;

			}
			else
			{
				printf(" Broken\n");
				no = 1;
				break;
			}
		}*/


		if(n >= d)
		{
			if(pg!=0 && pg!=100)
			{
				printf(" Possible\n");
			}
			else if(pg==0 && pd==0)
				printf(" Possible\n");
			else if(pg==100 && pd==100)
				printf(" Possible\n");
			else
				printf(" Broken\n");
		}
		else
			printf(" Broken\n");



/*		if( ((a - b) >= 0 && (c - d) > 0) || ( (a-b)<= 0 && (c - d)<0 ) || (a==b && c==d) )
		{
			printf(" Possible\n");			
		}
		else
			printf(" Broken\n");*/


	}
	return 0;
}