#include<stdio.h>
#include<algorithm>

int dist[10000], len[10000];
int mx[10000];

bool solve() {
	int N, D;
	scanf("%d", &N);
	for(int i=0;i<N;i++) {
		scanf("%d%d", &dist[i], &len[i]);
	}
	scanf("%d", &D);
	memset(mx, 0, sizeof(mx));
	mx[0]=dist[0];
	int end=0;
	for(int i=0;i<N;i++) {
		if(end<=i) end=i+1;
		while(end<N&&dist[end]<=dist[i]+mx[i]) {
			mx[end]=std::min(len[end], dist[end]-dist[i]);
			end++;
		}
		if(dist[i]+mx[i]>=D) return true;
	}
	return false;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++) {
		printf("Case #%d: %s\n", c, solve()?"YES":"NO");
	}
}