#include <cstdio>

int main(){
	int T;
	scanf("%d ", &T);
	for(int i = 1; i <= T; i++){
		int N, K;
		scanf("%d %d", &N, &K);
		int mask = (1 << N) - 1;
		printf("Case #%d: %s\n", i, (mask & K) == mask ? "ON" : "OFF");
	}
	return 0;
}
