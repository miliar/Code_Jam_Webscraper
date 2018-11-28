#include <stdio.h>
#include <math.h>
int main()
{
	int c,ci;
	freopen("A-large.in", "r", stdin);
	freopen("2.txt", "w", stdout);
	scanf("%d", &c);
	for(ci=1;ci<=c;ci++){
		int N,K;
		scanf("%d%d", &N, &K);
		double base = pow((double)2, N);
		long basen = (long)base;
		long rst = K%basen;
		if(rst == basen-1)
			printf("Case #%d: ON\n", ci);
		else
			printf("Case #%d: OFF\n", ci);
	}
}