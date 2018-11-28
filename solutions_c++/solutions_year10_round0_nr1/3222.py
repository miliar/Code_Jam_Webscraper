#include<stdio.h>
bool solve(int N, int K){
	int i=0;
	while(K>0){
		if(K%2==1){
			K/=2;
			++i;
		}else
			return false;
		if(i==N)
			return true;
	}
	return false;
}
int main(){
	int T,N,K;
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;++i){
		scanf("%d%d",&N,&K);
		printf("Case #%d: ",i);
		if(solve(N,K))
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}