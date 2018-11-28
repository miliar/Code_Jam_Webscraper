#include <stdio.h>

int main(){
	int T,N,K;
	scanf("%d",&T);
	for (int TC=1; TC<=T; TC++){
		scanf("%d %d",&N,&K);
		int M = (1<<N) - 1;
		printf("Case #%d: %s\n",TC,((K&M)==M)?"ON":"OFF");
	}
}
