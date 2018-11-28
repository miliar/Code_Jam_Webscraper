#include<stdio.h>
#include<math.h>

int main()
{
	int t, n, k, d, i, f, caseno=1;


	scanf("%d",&t);

	while(t--)
	{
		f = 1;

		scanf("%d%d",&n,&k);
		
		d =  floor(log10(k)/log10(2)) + 1;

		for(i=0; i<n; i++)
		{
			if((k&(1<<i))==0)
			{
				f = 0;
				break;
			}
		}

		if(f==1)
			printf("Case #%d: ON\n",caseno++);
		else
			printf("Case #%d: OFF\n",caseno++);
	}
	return 0;
}
