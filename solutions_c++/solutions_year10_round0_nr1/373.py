#include<stdio.h>

//<A-large.in >aaa.out
int main(){
	int T,N,n,k;
	scanf("%d",&T);

	for(N=1;N<=T;N++){
		scanf("%d%d",&n,&k);
		if((k%(1<<n))==(1<<n)-1)
			printf("Case #%d: ON\n",N);
		else
			printf("Case #%d: OFF\n",N);
/*
		while(k){
			printf("%d",k%2);
			k/=2;
		}
		printf("\n");
*/
	}

	return 0;
}