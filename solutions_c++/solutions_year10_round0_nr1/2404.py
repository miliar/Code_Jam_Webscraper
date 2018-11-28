#include <stdio.h>

int main(){
	int T,t;
	scanf("%d",&T);
	t=T;
	while(T--){
		int N,K;
		scanf("%d %d",&N,&K);
		int f=2;
		for(int i=0;i<N-1;i++)
			f*=2;
		f--;
		printf("Case #%d: %s\n",t-T,((K&f)==f ?  "ON" : "OFF"));
	}
};
