#include <cstdio>

int main(){
	int T,N,K;
	scanf("%d",&T);
	for (int i=0;i<T;i++){
		scanf("%d%d",&N,&K);
		printf(((K+1)%(1<<N))==0 ? "Case #%d: ON\n" : "Case #%d: OFF\n",i+1);
	}
	return 0;
}
