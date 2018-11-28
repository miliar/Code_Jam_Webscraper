#include <cstdio>

int main() {
	int T,N,K;
	scanf("%d", &T);
	for(int t=0;t<T;++t) {
		scanf("%d%d",&N,&K);
		int mask = 0;
		for(int n=0;n<N;++n) mask |= (1<<n);
		printf("Case #%d: %s\n",t+1, (K&mask)==mask ? "ON" : "OFF");
	}
}
