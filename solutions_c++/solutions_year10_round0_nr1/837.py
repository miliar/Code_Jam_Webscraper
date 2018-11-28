#include <cstdio>
#include <cstring>
#include <algorithm>

#define FOR(i, n) for(int i = 0; i < n; i++)

using namespace std;

int main() {
	long long T, N, K;
	
	scanf("%lld\n", &T);
	
	FOR(i, T) {
		scanf("%lld %lld\n", &N, &K);
		printf("Case #%d: %s\n", i+1, (((K+1) & ((1LL<<N)-1)) == 0) ? "ON" : "OFF");
	}
}
