#include<stdio.h>

void solve() {
	int N, mn=100000000, xx=0, sm=0;
	scanf("%d", &N);
	for(int i=0;i<N;i++) {
		int c;
		scanf("%d", &c);
		xx^=c;
		if(c<mn) mn=c;
		sm+=c;
	}
	if(xx!=0) puts("NO");
	else printf("%d\n", sm-mn);
}

int main() {
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++) {
		printf("Case #%d: ", cas);
		solve();
	}
}