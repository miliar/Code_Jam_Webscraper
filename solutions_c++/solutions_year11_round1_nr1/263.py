#include <stdio.h>


int T;
long long int n;
int pd, pg;

int mdc(int a, int b){
	if(b == 0)return a;
	return mdc(b,a%b);
}

int main(){
	scanf(" %d",&T);
	for(int t=0; t<T;t++){
		scanf(" %lld %d %d",&n, &pd, &pg);
		printf("Case #%d: ",t+1);
		//printf("%d\n",100/mdc(100,pd));
		if( n >= 100/mdc(100,pd) ){
			if(pg == 0){
				if(pd != 0){
					printf("Broken\n");
					continue;
				}
			}
			if(pg == 100){
				if(pd != 100){
					printf("Broken\n");
					continue;
				}
			}
			printf("Possible\n");
		}
		else{
			printf("Broken\n");
			continue;
		}
	}
}
