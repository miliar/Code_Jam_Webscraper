#include<stdio.h>

#define SIZE 100000

int main()
{
	int T,t;
	scanf("%d", &T);
	for(t = 1; t <= T; t++)
	{
		int a,b;
		scanf("%d %d", &a, &b);
		int i;
		double input[SIZE] = {0.0};
		double allright[SIZE] = {0.0};
		double allCorrect = 1.0;
		for(i = 0; i < a; i++)
		{
			allright[i] = allCorrect;
			scanf("%lf", &input[i]);
			allCorrect = allCorrect * input[i];
		}

		double case1 = allCorrect * (b - a + 1) + \
			(1.0 - allCorrect) * (b - a + 1 + b + 1);
	
		double min = case1;

		double case3 = (1 + b + 1) * 1.0;

		if(min > case3)
			min = case3;

		double case2 = 0;
		for(i = 0; i < a; i++)
		{
			case2 = 1.0 * ( 2.0*(a - i) + b - a + 1) * allright[i] + \
					1.0*(2.0*(a - i) + b - a + 1 + b + 1) * (1.0 - allright[i]);
			if(case2 < min)
				min = case2;
		}

		printf("Case #%d: %lf\n", t, min);
	}
}

