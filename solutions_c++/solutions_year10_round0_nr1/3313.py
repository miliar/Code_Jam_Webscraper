#include<stdio.h>

int main() {
	int T, t, N, K;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d %d",&N,&K);
		printf("Case #%d: ",t);
		printf(((K+1)&((1<<N)-1))?"OFF\n":"ON\n");
	}
	return 0;
}
