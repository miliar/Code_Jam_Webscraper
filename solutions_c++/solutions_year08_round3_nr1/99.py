// c1.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <stdlib.h>

int freq[1000];
int P,K,L;

int cmp(const void *a, const void *b) {
	int aa = *(int *)a;
	int bb = *(int *)b;
	return bb-aa;
}
__int64 work() {
	qsort(freq,L,sizeof(int),cmp);
	__int64 sum = 0;
	int type = 1;
	int kused = 0;
	for(int i=0;i<L;i++) {
		sum += type * freq[i];
		kused ++;
		// printf("%d type %d\n",freq[i],type);
		if (kused == K) {
			kused = 0;
			type++;
		}
	}
	return sum;
}

int main() {
	int N; scanf("%d",&N);
	for(int i=1;i<=N;i++) {
		scanf("%d %d %d",&P,&K,&L);
		for(int j=0;j<L;j++) {
			scanf("%d",&freq[j]);
		}
		printf("Case #%d: ",i);

		if (P*K<L) printf("Impossible\n");
		else printf("%I64d\n",work());
	}
	int tmp;
	scanf("%d",&tmp);
}
