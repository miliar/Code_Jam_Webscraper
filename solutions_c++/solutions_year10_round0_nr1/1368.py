#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int data_n,n,k,limit;
	scanf("%d",&data_n);
	for (int i = 0; i< data_n; ++i){
		scanf("%d %d", &n, &k);
		limit = 1;
		for (int k = 0; k < n; ++k)
			limit *= 2;
		if ((k+1) % limit == 0)
			printf("Case #%d: ON\n",i+1);
		else
			printf("Case #%d: OFF\n", i+1);
	}
	return 0;
}