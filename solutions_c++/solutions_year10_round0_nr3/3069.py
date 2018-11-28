#include<stdio.h>

int main(void)
{
	int i, T, R, N, K, C=1; 
	double sum, total, person=0.0;
	int queue[1000];

	scanf("%d", &T);

	while(T--)
	{
		scanf("%d %d %d", &R, &K, &N);

		person=0.0;

		for(i=0;i<N;i++)
		{
			scanf("%d", &queue[i]);
			person+=queue[i];
		}
		i=0;
		
		total=0.0;

		while(R--)
		{
			sum=0.0;

			for(;;i++)
			{
				if(sum+queue[i%N]>K || sum+0.5>person)
				{
					total+=sum;
					break;
				}
				sum+=queue[i%N];
			}
		}
		printf("Case #%d: %.0lf\n",C++,total);
	}

	return 0;
}