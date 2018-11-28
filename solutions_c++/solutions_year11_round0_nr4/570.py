#include <stdio.h>
int main() {
	int N, K, a, i, j, sum;
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	scanf("%d", &N);
	for(i=0;i<N;i++) {
		sum = 0;
		scanf("%d", &K);
		for(j=0;j<K;j++) {
			scanf("%d", &a);
			if(a-1==j)sum++;
		}
		printf("Case #%d: %lf\n", i+1,(double)K-sum);
	}
	return 0;	
}
