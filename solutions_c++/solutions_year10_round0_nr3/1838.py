#include <stdio.h>
#include <malloc.h>

int T,R,K,N;
int id;
int g[1009][2];
int group[1009];
__int64 ans;

void input() {
	int j;
	scanf("%d%d%d",&R,&K,&N);
	for(j = 0; j < N; j++) {
		scanf("%d",&group[j]);
	}
}

void solve() {
	int i,j,ti;
	int cur = 0;
	for(i = 0; i < N; i++) {
		cur = group[i];
		ti = 0;
		j = i;
		while(true) {
			if(ti < (N - 1) && cur + group[(j + 1) % N] <= K) {
				cur += group[(j + 1) % N];
				j = (j + 1) % N;
				ti++;
			} else break;
		}
		g[i][0] = cur;
		g[i][1] = (j + 1) % N;
	}
    ans = 0;
	int st = 0;
	for(i = 0; i < R; i++) {
		ans += g[st][0];
		st = g[st][1];
	}
	printf("Case #%d: %I64d\n",++id,ans);
}

int main() {
	int i;
		freopen("C-large.in","r",stdin);
		freopen("C-large.out","w",stdout);
	scanf("%d",&T);
	for(i = 0; i < T; i++) {
		input();
		solve();
	}
	return 0;
}

/*
10
4 6 2
4 2
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
*/