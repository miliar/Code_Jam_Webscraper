#include<cstdio>
typedef long long LL;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);
	int ntc;
	scanf("%d", &ntc);
	for(int TC=1; TC<=ntc; TC++) {
		LL N, K;
		scanf("%I64d %I64d", &N, &K);
		printf("Case #%d: %s\n", TC, ( (K % (1LL<<N)) == ((1LL << N) - 1) ) ? "ON" : "OFF" );
	}
	return 0;
}
