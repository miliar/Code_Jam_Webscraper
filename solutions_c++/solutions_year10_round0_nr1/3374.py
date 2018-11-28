#include <stdio.h>
#include <cmath>

int main(){
	int T,i;
	long long N,K;
	long long zus; //Zustaende
	scanf("%i\n",&T);
	for(i=1;i<=T;i++){
		scanf("%lli %lli\n",&N,&K);
		zus=pow(2,N);
		if(N==1){
			if(K%2==0)printf("Case #%i: OFF\n",i);
			else printf("Case #%i: ON\n",i);
		}
		else{
			if((K!=0) && ((K+1)%zus==0))printf("Case #%i: ON\n",i);
			else printf("Case #%i: OFF\n",i);
		}
	}
	return 0;
}
