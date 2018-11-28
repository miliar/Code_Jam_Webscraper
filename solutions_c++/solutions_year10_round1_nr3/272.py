#include <stdio.h>
#include <cstring>

int a1, a2, b1, b2;

int ganha(int a, int b)
{
	if (a > b)
	{
		return ganha(b, a);
	}

	if (a == b)
	{
		return 0;
	}

	if (b%a == 0)
	{
		return 1;
	}
	
	if (2*a >= b)
	{
		return 1-ganha(b-a, a);
	}

	return (1-ganha(b%a, a))|(1-ganha(b%a+a, a));

}

int main()
{
	int cas, t;

	scanf("%d", &t);

	for (cas=1; cas<=t; cas++)
	{
		int i, j, r;

		scanf("%d %d %d %d", &a1,&a2,&b1,&b2);
		r = 0;
		for (i=a1; i<=a2; i++)
		{
			for (j=b1; j<=b2; j++)
			{
//				printf("%d %d --> %d\n",i,j, ganha(i,j));
				if (ganha(i,j))
				{
					r++;
				}	
			}
		}
		printf("Case #%d: %d\n",cas,r);
	}

	return 0;
}
