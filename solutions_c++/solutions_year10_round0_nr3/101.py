#include <cstdio>

int main(){
	int T, R, K, N, g[1000], cache[1000][2];
	scanf("%d ", &T);
	for(int i = 1; i <= T; i++){
		scanf("%d %d %d ", &R, &K, &N);
		for(int j = 0; j < N; j++){
			scanf("%d ", g + j);
			cache[j][0] = cache[j][1] = -1;
		}
		long long cost = 0;
		for(int j = 0, next = 0; j < R; j++){
			if(cache[next][0] >= 0){
				cost += cache[next][0];
				next  = cache[next][1];
			}else{
				int prev = next;
				long long now = 0;
				for(int c = 0; c < N && now + g[next] <= K; c++){
					now += g[next];
					next = (next + 1) % N;
				}
				cost += (cache[prev][0] = now);
				cache[prev][1] = next;
			}
		}
		printf("Case #%d: %lld\n", i, cost);
	}
	return 0;
}
