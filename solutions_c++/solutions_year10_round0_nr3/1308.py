#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#define MAXN 11

int R, K, N;
int g[MAXN];

int solve(){
	if (N == 1) return R*g[0];
	int res = 0, head, tail;
	head = tail = 0;
	for (int attempt = 1; attempt <= R; attempt++){
		int capacity = g[head];		
		tail = head;
		while (true){
			tail = (tail + 1) % N;
			if (tail == head) break;
			capacity += g[tail];			
			if(capacity > K){				
				capacity -= g[tail];
				tail = (tail - 1 + N) % N;
				break;
			}
		}
		head = (tail + 1) % N;
		res += capacity;
	}
	return res;
}

int main(){
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
	int cases, t = 0;
	scanf("%d", &cases);
	while (t < cases){
		int i, res;
		memset(g, 0, sizeof g);
		scanf("%d %d %d", &R, &K, &N);
		for (i = 0; i < N; i++)
			scanf("%d", g + i);
		res = solve();
		printf("Case #%d: %d\n", ++t, res);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}