#include <stdio.h>

int main(){ 
	long r, k, a[1000];
	int t, n, i, j;
	scanf("%d", &t);
	for(i = 1; i <= t; i++){
		scanf("%ld%ld%d", &r, &k, &n);
		long total = 0;
		for(j = 0; j < n; j++){
			scanf("%ld", &a[j]);
			total += a[j];
		}
		if(total <= k){
			total *= r;
		} else{
			total = 0;
			long sum = 0;
			int x = 0;
			while(r){
				if((sum + a[x]) <= k){
					sum += a[x];
				} else {
					total += sum;
					r--;
					sum = a[x];
				}
				x++;
				x %= n;
			}
		}
		printf("Case #%d: %ld\n", i, total);
	}
}