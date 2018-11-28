#include <cstdio>
#define FOR(i,a,b) for(int i=int(a); i<int(b); ++i)
#define NX 1003
using namespace std;

typedef long long LG;

int R, k, N, head, tail, cst;
int G[NX], First[NX], Next[NX];
LG vh, vt;
LG Val[NX];

inline void succ(int &x) {
	if(++x > N) x -= N;
}

int main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,0,Z) {
		scanf("%d%d%d", &R, &k, &N);
		FOR(i,1,N+1) scanf("%d", G + i), First[i] = 0;
		int start = 1;
		FOR(i,1,N+2) {
			if(First[start]) { tail = i; break; }
			First[start] = i;
			int j = start; LG sum = 0;
			while(sum + G[j] <= k) {
				sum += G[j], succ(j);
				if(j == start) break;
			}
			Val[start] = sum, Next[start] = j, start = j;
		}
		head = First[start], cst = start, start = 1, vh = vt = 0;
		FOR(i,1,head) vh += Val[start], start = Next[start];
		FOR(i,head,tail) vt += Val[start], start = Next[start];
		//printf("head=%d  tail=%d  cst=%d\n", head, tail, cst);
		//printf("vh=%lld  vt=%lld\n", vh, vt);
		LG res = 0;
		if(R < head) {
			start = 1;
			FOR(i,1,R) res += Val[start], start = Next[start];
		} else {
			int R2 = (R + 1 - head) % (tail - head);
			start = cst;
			FOR(i,0,R2) res += Val[start], start = Next[start];
			res += vh + (R + 1 - head) / (tail - head) * vt;
		}
		printf("Case #%d: %lld\n", z + 1, res);
	}
	return 0;
}
