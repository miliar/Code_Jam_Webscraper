#include<stdio.h>
#include<stdlib.h>
int main(){
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		int N,K;
		scanf("%d %d",&N,&K);
		printf("Case #%d: ",t + 1);
		if(( K + 1 ) % ((1 << N)) == 0)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}
