#include<stdio.h>

char map[64][64];
int N, K;

bool valid(int x, int y) {
	return x>=0 && x<N && y>=0 && y<N;
}

int mxr, mxb;
void tomax(char c, int v) {
	if(c=='R' && v>mxr) mxr=v;
	if(c=='B' && v>mxb) mxb=v;
}

void test(int x, int y, int dx, int dy) {
	char lc=0;
	int cnt=1;
	while(valid(x, y)) {
		if(map[x][y]==lc) cnt++;
		else {
			tomax(lc, cnt);
			cnt=1;
			lc=map[x][y];
		}
		x+=dx;
		y+=dy;
	}
	tomax(lc, cnt);
}

void solve() {
	mxr=mxb=0;
	scanf("%d%d", &N, &K);
	for(int i=0;i<N;i++) {
		scanf("%s", map[i]);
		int t=N-1;
		for(int j=N-1;j>=0;j--) {
			if(map[i][j]!='.')
				map[i][t--]=map[i][j];
		}
		while(t>=0) map[i][t--]='.';
	}
	for(int i=0;i<N;i++) {
		test(0, i, 1, 0);
		test(i, 0, 0, 1);
		test(i, 0, 1, 1);
		test(0, i, 1, 1);
		test(i, 0, -1, 1);
		test(N-1, i, -1, 1);
	}
	if(mxr>=K) {
		if(mxb>=K) puts("Both");
		else puts("Red");
	} else {
		if(mxb>=K) puts("Blue");
		else puts("Neither");
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for(int i=1;i<=t;i++) {
		printf("Case #%d: ", i);
		solve();
	}
}