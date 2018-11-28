#include<stdio.h>

int main() {
	int T, t, N, K;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		
		scanf("%d %d",&N,&K);
		
		printf("Case #%d: ",t);
		K &= (1<<N)-1;
		if(K==(1<<N)-1) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
