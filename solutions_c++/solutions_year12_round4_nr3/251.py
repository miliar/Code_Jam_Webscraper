#include<stdio.h>

int nCase;
int N, W[2048], H[2048];

inline int max(int a, int b) { return a>b ? a : b; }

inline char go(int s, int e, int dx, int dy) {
	fprintf(stderr, "go s %d e %d dx %d dy %d\n", s, e, dx, dy);
	if(s >= e) return 1;
	if(s+1 == e) {
		if(W[s] > e) return 0;
		H[s] = H[e] - max(1, (dy+dx-1)/dx);
	//	fprintf(stderr, "\t H[%d] = %d\n", s, hs);
		return 1;
	}
	int now = s;
	for(; now < e && W[now] != e; ++now) ;
	//fprintf(stderr, "\tnow %d wnow %d\n", now, W[now]);
	if(W[now] > e) return 0;
	H[now] = H[e] - max(1, (dy*((long long)e-now)+dx-1)/dx);
	char ok = go(s, now, e-now, H[e]-H[now]);
	for(int i = now+1; i < e; ++i)
		if(W[i] == e) {
			H[i] = H[now];
			ok &= go(now+1, i, e-i, H[e]-H[i]);
			now = i;
		}
	ok &= go(now+1, e, dx, dy);
	return ok;
	//fprintf(stderr, "\t H[%d] = %d\n", now, he-1);
	//return go(s, now, e-now, H[e]-H[now]) && go(now+1, e, dx, dy);
}

int main() {
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		scanf("%d", &N);
		for(int i = 1; i < N; ++i)
			scanf("%d", &W[i]);
		W[N] = N+1;
		H[N] = 1000000000;
		char ok = go(1, N, 1, 0);
		printf("Case #%d:", cs);
		if(!ok) puts(" Impossible");
		else {
			for(int i = 1; i <= N; ++i)
				printf(" %d", H[i]);
			printf("\n");
		}
	}
}


