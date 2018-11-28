#include <cstdio>
#include <cmath>

int main(){
	int tc; scanf("%d",&tc);
	for(int i=1;i<=tc;i++){
		int N,K; scanf("%d%d",&N,&K);
		int P=1<<N;
		K%=P;
		printf("Case #%d: ",i);
		if(K==P-1) printf("ON\n");
		else printf("OFF\n");
	}
}
