#include <stdio.h>

using namespace std;

int count(int n)
{
	int c = 0;

	while(n>0)
	{
		c++;
		n = n/10;
	}
	return c;
}

int main()
{
	int cases,small,big;
	int c=1;
	int res,i,tmp,j;
	int digits,multiplier;

	for(scanf("%d",&cases);cases>0;cases--,c++)
	{
		scanf("%d%d",&small,&big);
		res = 0;

		digits = count(small);
		for(multiplier=1,i=1;i<digits;multiplier*=10,i++);

		for(i=small;i<big;i++)
		{
			j = i;
			tmp = j%10;
			j = tmp*multiplier + (j/10);
			while(j!=i)
			{
				if(j>i && j<=big)
					res++;

				tmp = j%10;
				j = tmp*multiplier + (j/10);
			}
		}

		printf("Case #%d: %d\n",c,res);
	}
	
	return 0;
}
