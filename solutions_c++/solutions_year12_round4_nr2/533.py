#include<assert.h>
#include<stdio.h>
#include<algorithm>
using namespace std;

typedef struct Node {
	int id, r, used;
	int x, y;
	bool operator<(const struct Node &a) const {
		return r > a.r;
	}
}Node;

int nCase;
int W, L, N;
Node C[1024];
int X[1024], Y[1024];

inline int greedyRow(int bh, int *_hi) {
	int m = 0;
	for(; m < N && C[m].used; ++m);
	C[m].x = 0;
	C[m].y = bh + C[m].r;
	*_hi = 2*C[m].r;
	int wd = C[m].r;
	fprintf(stderr, "bh %d hi %d L %d\n", bh, *_hi, L);
	if(bh + *_hi > L) return 0;
	int n = 1;
	for(int i = m+1; i < N; ++i) {
		if(C[i].used) continue;
		if(wd+2*C[i].r > W) continue;
		C[i].x = wd + C[i].r;
		C[i].y = bh + C[i].r;
		C[i].used = 1;
		wd += 2*C[i].r;
		++n;
		/*for(int j = i+1; j < N; ++j)
			if(!C[j].used && 2*C[i].r+2*C[j].r <= *_hi) {
				C[j].x = C[i].x;
				C[j].y = C[i].y + C[i].r+C[j].r;
				C[j].used = 1;
				++n;
				break;
			}*/
	}
	return n;
}

inline int greedyRow1(int *_hi) {
	C[0].x = C[0].y = 0;
	int hi = C[0].r, wd = C[0].r;
	int n = 1;
	for(int i = 1; i < N; ++i) {
		if(C[i].used) continue;
		if(wd+2*C[i].r > W) continue;
		C[i].x = wd + C[i].r;
		C[i].y = C[0].y;
		C[i].used = 1;
		wd += 2*C[i].r;
		++n;
		/*for(int j = i+1; j < N; ++j)
			if(!C[j].used && C[i].r+2*C[j].r <= hi) {
				C[j].x = C[i].x;
				C[j].y = C[i].r + C[j].r;
				C[j].used = 1;
				++n;
				break;
			}*/
	}
	*_hi = hi;
	return n;
}

int main() {
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		scanf("%d %d %d", &N, &W, &L);
		char tr = 0;
		if(W < L) { int t = L; L = W; W = t; tr = 1; }
		for(int i = 0; i < N; ++i) {
			scanf("%d", &C[i].r);
			C[i].id = i;
			C[i].x = C[i].y = -1;
			C[i].used = 0;
		}
		sort(C, C+N);
		int by;
		int n = greedyRow1(&by);
		while(n < N) {
			int h;
			int n2 = greedyRow(by, &h);
			by += h;
			assert(n2 > 0);
			n += n2;
		}

		for(int i = 0; i < N; ++i) {
			X[C[i].id] = tr ? C[i].y : C[i].x;
			Y[C[i].id] = tr ? C[i].x : C[i].y;
		}
		printf("Case #%d:", cs);
		for(int i = 0; i < N; ++i)
			printf(" %d %d", X[i], Y[i]);
		printf("\n");
		fflush(stdout);
	}
}

