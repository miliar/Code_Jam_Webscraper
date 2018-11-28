#include <cstdio>

#define REP(i,n) for(int i = 0,_n = (n);i < _n;++i)

const int NMAX = 50;

enum { EMPTY, RED, BLUE };
int T[NMAX][NMAX];

void find_series(int N,int K,int val,bool& ok) {
	REP(r,N) REP(c,N) {
		int cnt = 0, cur = c;
		while (cur < N && T[r][cur] == val) {
			++cnt, ++cur;
		}
		if (cnt >= K) { ok = true; return; }
	}
	REP(r,N) REP(c,N) {
		int cnt = 0, cur = r;
		while (cur < N && T[cur][c] == val) {
			++cnt,++cur;
		}
		if (cnt >= K) { ok = true; return; }
	}
	REP(r,N) REP(c,N) {
		int cnt = 0, curr = r, curc = c;
		while (curr < N && curc < N && T[curr][curc] == val) {
			++cnt,++curr,++curc;
		}
		if (cnt >= K) { ok = true; return; }
	}
	REP(r,N) REP(c,N) {
		int cnt = 0, curr = r, curc = c;
		while (curr < N && curc >= 0 && T[curr][curc] == val) {
			++cnt,++curr,--curc;
		}
		if (cnt >= K) { ok = true; return; }
	}
}

void testcase(int nr) {
	int N,K;
	scanf("%d%d",&N,&K);
	REP(r,N) {
		static char buf[NMAX+10];
		scanf("%s",buf);
		REP(c,N) switch (buf[c]) {
		case '.': T[c][N-1-r] = EMPTY; break;
		case 'R': T[c][N-1-r] = RED; break;
		case 'B': T[c][N-1-r] = BLUE; break;
		}
	}
	
	REP(c,N) {
		int a = N-1, b = N-1;
		for(;b >= 0;--b)
			if (T[b][c] != EMPTY) {
				T[a][c] = T[b][c];
				--a;
			}
		for(;a >= 0;--a)
			T[a][c] = EMPTY;
	}
	
	bool okR = false, okB = false;
	find_series(N,K,RED,okR);
	find_series(N,K,BLUE,okB);
	printf("Case #%d: ",nr);
	if (okR && okB) printf("Both");
	else if (okR) printf("Red");
	else if (okB) printf("Blue");
	else printf("Neither");
	putchar('\n');
}

int main() {
	int T;
	scanf("%d",&T);
	REP(i,T) testcase(i+1);
}
