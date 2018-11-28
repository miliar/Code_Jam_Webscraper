#include <stdio.h>

struct Node{
	int score;
	int next;
	int lastTime;
	long long lastRet;
	Node(){
		lastTime = 0;
	}
};

int main(){
	int T;
	
	scanf("%d", &T);
	for (int ttt = 1; ttt <= T; ttt++){
		int R, K, N;
		int g[1000];
		Node node[1000];
		scanf("%d%d%d", &R, &K, &N);
		for (int i = 0; i < N; i++){
			scanf("%d", g + i);
		}
		long long ret = 0;
		for (int r = 1, p = 0; r <= R;){
			if (node[p].lastTime == 0){
				int sum = 0;
				int i;
				for (i = p; i < N && sum + g[i] <= K; i++){
					sum += g[i];
				}
				if (i == N){
					for (i = 0; i < p && sum + g[i] <= K; i++){
						sum += g[i];
					}
				}
				node[p].next = i;
				node[p].score = sum;
				node[p].lastTime = r;
				ret += sum;
				node[p].lastRet = ret;
				p = i;
				r++;
			}else{
				int cycle = r - node[p].lastTime;
				int time = (R - r) / cycle;
				r += time * cycle + 1;
				ret += node[p].score;
				ret += time * (ret - node[p].lastRet);
				p = node[p].next;
			}
		}
		printf("Case #%d: %lld\n", ttt, ret);
	}
	return 0;
}