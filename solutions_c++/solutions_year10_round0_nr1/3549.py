#include <cstdio>

#define rep(i,n) for (int i = 0; i < n; i++)

using namespace std;

long long doit(long long c) {
	if (c == 1) return 1;
	else return 2*doit(c-1) + 1;
}

int main() {
	int T;
	scanf("%d", &T);
	
	rep(t,T) {
		long long N, K;
		scanf("%lld %lld", &N, &K);
		
		long long quant = doit(N);
		K %= quant+1;

		printf("Case #%d: ", t+1);
		if (K == quant) printf("ON\n");
		else printf("OFF\n");
	}
	
	return 0;
}

