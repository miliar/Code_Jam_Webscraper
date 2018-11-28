#include <stdio.h>
#include <string.h>
typedef long long llong;
#define MAXN 1024
int R;
int Cap;
int N;
int g[MAXN];
int next[MAXN];
int cost[MAXN];
int lis[MAXN];
bool visit[MAXN];
int list_length;
int loop_length;
long long ans;
void input() {
	scanf("%d%d%d", &R, &Cap, &N);
	for (int i=1; i<=N; ++i) {
		scanf("%d", &g[i]);
	}
}
void init() {
	for (int i=1; i<=N; ++i) {
		cost[i] = 0;
		next[i] = i;
		do {
			cost[i] += g[next[i]];
			next[i]++;
			if (next[i] == N+1) {
				next[i] = 1;
			}
			if (next[i] == i) {
				break;
			}
		} while (cost[i] + g[next[i]] <= Cap);
	}
	
	// test
	/*for (int i=1; i<=N; ++i) {
		printf("%d %d %d\n", i, next[i], cost[i]);
	}*/
}
void solve() {
	list_length = 0;
	loop_length = 0;
	ans = 0;
	memset(visit, false, sizeof(visit));
	int now = 1;
	while (!visit[now]) {
		visit[now] = true;
		lis[list_length++] = now;
		now = next[now];
	}
	for (int i=0; i<list_length; ++i) {
		if (lis[i] == now) {
			loop_length = list_length - i;
			break;
		}
	}
	// test
	/*printf("%d %d\n", list_length, loop_length);
	for (int i=0; i<list_length; ++i) {
		printf("%d ", lis[i]);
	}
	printf("\n");*/
	if (R <= list_length - loop_length) {
		for (int i=0; i<R; ++i) {
			int j = lis[i];
			ans += cost[j];
		}
	} else {
		for (int i=0; i<list_length-loop_length; ++i) {
			int j = lis[i];
			ans += cost[j];
		}
		R -= list_length-loop_length;
		int p = R/loop_length;
		int q = R%loop_length;
		for (int i=0; i<q; ++i) {
			int j = lis[list_length-loop_length+i];
			ans += cost[j];
		}
		long long tmp = 0;
		for (int i=list_length-loop_length; i<list_length; ++i) {
			int j = lis[i];
			tmp += cost[j];
		}
		ans += tmp * p;
	}
}
int main(int argc, char* argv) {
	int T;
	scanf("%d", &T);
	for (int kth=1; kth<=T; ++kth) {
		input();
		init();
		solve();
		printf("Case #%d: %I64d\n", kth, ans);
	}
	return 0;
}