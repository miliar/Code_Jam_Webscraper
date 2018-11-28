#include <stdio.h>
#include <math.h>

int main()
{
	unsigned int N, T, K;
	scanf("%u", &T);
	for(int i=0;i<T;i++)
	{
		scanf("%u %u", &N, &K);
		int iLight = 0;
		
		int a = pow(2, N);
		if (K%a == a-1)
			iLight = 1;

		if (iLight)
			printf("Case #%d: ON\n", i+1);
		else
			printf("Case #%d: OFF\n", i+1);
	}
}
