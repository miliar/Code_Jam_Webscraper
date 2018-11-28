#include<stdio.h>
#include<algorithm>
#include<functional>

int r[1000], W, L;
void forward(int &x, int &y, int &p, int d) {
	if(p==0) {
		x+=d;
		if(x>W) {
			p=1;
			x=W;
			y=0;
		}
	}
	if(p==1) {
		y+=d;
		if(y>L) {
			p=2;
			y=L;
			x=W;
		}
	}
	if(p==2) {
		x-=d;
		if(x<0) {
			x=0;
			y=L-d;
		}
	}
	if(p==3) {
		y-=d;
	}
}

long long inline sqr(long long v) { return v*v; }

int cor[1000][2];
int idx[1000];
bool inline cmp(int a, int b) {
	return r[a]<r[b];
}
void solve() {
	int N;
	scanf("%d%d%d", &N, &W, &L);
	for(int i=0;i<N;i++) {
		scanf("%d", &r[i]);
	}
	r[N]=0;
	for(int i=0;i<N;i++) {
		idx[i]=i;
	}
	std::sort(idx, idx+N, cmp);
	int x=0, y=0, p=0;
	for(int i=0;i<N;i++) {
		cor[idx[i]][0]=x;
		cor[idx[i]][1]=y;
		if(x<0||x>W||y<0||y>L) {
			puts("Error!");
		}
		for(int j=0;j<i;j++) {
			if(sqr(cor[idx[i]][0]-cor[idx[j]][0])+sqr(cor[idx[i]][1]-cor[idx[j]][1])<sqr(r[idx[i]]+r[idx[j]])) {
				puts("Error!");
			}
		}
		forward(x, y, p, r[idx[i]]+r[idx[i+1]]);
	}
	for(int i=0;i<N;i++) {
		printf(" %d %d", cor[i][0], cor[i][1]);
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++) {
		printf("Case #%d:", c);
		solve();
		putchar('\n');
	}
}