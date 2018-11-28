#include<stdio.h>

int main() {
	int t,T,i,N,mn,sum,sum2,a;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d",&N);
		mn = 1000001;
		sum = sum2 = 0;
		for(i=0;i<N;i++){
			scanf("%d",&a);
			if(a<mn) mn = a;
			sum += a;
			sum2 ^= a;
		}
		if(sum2) {
			printf("Case #%d: NO\n",t);
		} else {
			printf("Case #%d: %d\n",t,sum-mn);
		}
	}
	return 0;
}
