#include <iostream>
using namespace std;

const int maxm = 10050;
const int impos = 20000;

int m,v;

bool g[maxm];
bool c[maxm];
bool a[maxm];

int d0[maxm];
int d1[maxm];

void dfs(int x) {
	if(x>m/2) {
		if(a[x]) {
			d1[x] = 0;
			d0[x] = impos;
		}else{
			d0[x] = 0;
			d1[x] = impos;
		}
		return;
	}
	d0[x] = d0[2*x]+d0[2*x+1];
	d1[x] = d1[2*x] + d1[2*x+1];
	if(g[x]) {
		if(c[x]) {
			d1[x] = min(d1[x], 1+min(d0[2*x]+d1[2*x+1], d1[2*x]+d0[2*x+1]) );
		}
		d0[x] = min(d0[x], min(d0[2*x]+d1[2*x+1], d1[2*x]+d0[2*x+1]) );
	} else {
		if(c[x]) {
			d0[x] = min(d0[x], 1+min(d0[2*x]+d1[2*x+1], d1[2*x]+d0[2*x+1]) );
		}
		d1[x] = min(d1[x], min(d0[2*x]+d1[2*x+1], d1[2*x]+d0[2*x+1]) );
	}
	/*
	0   d0[2*x] + d0[2*x+1];
	 or d0[2*x] + d1[2*x+1]
	 or d1[2*x] + d0[2*x+1]

	1   d1[2*x] + d1[2*x+1]
	*/
}

int main() {
	int N;
	scanf("%d",&N);
	for(int cs=1;cs<=N;cs++) {
		scanf("%d%d", &m,&v);
		for(int i=1;i<=m/2;i++) {
			int gg,cc;
			scanf("%d%d", &gg, &cc);
			g[i]=gg;
			c[i]=cc;
		}
		for(int i=m/2+1;i<=m;i++) {
			int aa;
			scanf("%d",&aa);
			a[i] = aa;
		}
		for(int i=m;i>0;i--) {
			dfs(i);
		}
		int res;
		if(v) {
			res = d1[1];
		} else {
			res = d0[1];
		}

		printf("Case #%d: ", cs);
		if(res>=impos) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n", res);
		}
	}
	return 0;
}

