#include<stdio.h>

double solve() {
	int N;
	scanf("%d", &N);
	double r=0;
	for(int i=1;i<=N;i++) {
		int v;
		scanf("%d", &v);
		if(v!=i) r++;
	}
	return r;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int cas=1;cas<=T;cas++) {
		printf("Case #%d: %lf\n", cas, solve());
	}
}