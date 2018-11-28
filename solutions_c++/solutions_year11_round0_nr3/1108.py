#include<stdio.h>

int main(){
	int test, n;
	int min, sum, xor, candy;
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	scanf("%d", &test);

	for(int i=1; i<=test; i++){
		scanf("%d", &n);
		min = 2100000000;
		sum = 0;
		xor = 0;
		for(int j=0; j<n; j++){
			scanf("%d", &candy);
			if(candy < min)
				min = candy;
			sum += candy;
			xor ^= candy;
		}
		if(xor != 0)
			printf("Case #%d: NO\n", i);
		else
			printf("Case #%d: %d\n", i, sum-min);
	}
	return 0;
}
