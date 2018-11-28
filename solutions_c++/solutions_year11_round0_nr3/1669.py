#include <stdio.h>
#include <stdlib.h>
int compare (const void *a, const void *b) {
	return ( *(int*)a - *(int*)b );
}
int main() {
	unsigned long T, N, i, j, C[1001], sum, xorSum,test=1,found, partialTopDownXorSum[1001], partialDownTopXorSum[1001], partialSum[1001];
	scanf("%lu",&T);
	while(T--) {
		scanf("%lu", &N);
		xorSum=sum=0;
		for(i=0;i<N;i++) {
			scanf("%lu", &C[i]);
			xorSum ^= C[i];
			sum += C[i];
		}
		printf("Case #%lu: ",	test++);
		if (xorSum != 0) {
			printf("NO\n");
		} else {
			qsort(C, N, sizeof(unsigned long), compare);
			for(i=0,j=N-1;i<N;i++,j--) {
				partialSum[i] = i==0?C[i]:partialSum[i-1]+C[i];
				partialTopDownXorSum[i] = i==0?C[i]:partialTopDownXorSum[i]^C[i];
				partialDownTopXorSum[j] = i==0?C[j]:partialDownTopXorSum[j+1]^C[j];
			}
			found=0;
			for(i=0;i<N-1;i++) {
				if (partialTopDownXorSum[i] == partialDownTopXorSum[i+1]) {
					printf("%lu\n", sum-partialSum[i]);
					found=1;
					break;
				}
			}
			if (found==0) { // not possible
				printf("NO\n");
			}
		}
	}
}