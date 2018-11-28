#include <cstdlib>
#include <cstdio>

int main(){
	int T,N;
	long long K;
	scanf("%d\n",&T);
	for(int t=1;t<=T;++t){
		scanf("%d %lld\n",&N,&K);
		long long mod = 1LL << N;
		//printf("\tK=%lld mod=%lld N=%d K'=%lld\n",K,mod,N,K%mod);
		K = K%mod;
		printf("Case #%d: %s\n",t,(K==mod-1)?"ON":"OFF");
	}
}
