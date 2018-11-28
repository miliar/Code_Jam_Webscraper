#include <cstdio>
#include <cmath>

int main()
{
	int C, N, K, N2;
	scanf("%d", &C);
	for (int c=1; c <= C; c++) {
		scanf("%d", &N);
		scanf("%d", &K);
		N2 = (int)pow(2.0, N);
		if((K+1)%N2)
			printf("Case #%d: OFF\n");
		else
			printf("Case #%d: ON\n");
	}
}