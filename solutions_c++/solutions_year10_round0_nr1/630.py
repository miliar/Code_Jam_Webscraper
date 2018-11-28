#include <cstdio>

using namespace std;

int T;

int main() {
	scanf("%d", &T);
	for(int i=0; i<T; i++) {
		long long int N, K, r, p;
		scanf("%lld%lld", &N, &K);
		r = (1 << N);
		p = r - 1;
		bool f = (K % r)==p;
		printf("Case #%d: %s\n", (i+1), (f ? "ON" : "OFF"));
	}
	return 0;
}
