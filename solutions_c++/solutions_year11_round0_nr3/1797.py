#include<stdio.h>

int main()
{
	int test, T, tmp, sum, bsum, N, min;
	scanf("%d", &T);
	for(test = 1; test <= T; test ++)
	{
		bsum = 0; sum = 0; min = 2000000;
		scanf("%d", &N);
		while(N --)
		{
			scanf("%d", &tmp);
			sum = sum + tmp;
			bsum = (bsum ^ tmp);
			if(tmp < min)
				min = tmp;
		}
		
		if(bsum == 0)
			printf("Case #%d: %d\n", test, sum - min);
		else
			printf("Case #%d: NO\n", test);
	}
	
	return 0;
}
