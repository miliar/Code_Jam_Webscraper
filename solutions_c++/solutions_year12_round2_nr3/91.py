#include<stdio.h>
#include<algorithm>
using namespace std;

typedef struct Node {
	long long s;
	int m;
	bool operator<(const struct Node &a) const {
		if(s != a.s) return s < a.s;
		else return m < a.m;
	}
}Node;

int nCase;
int N, A[512];
Node X[1048580];

inline void print(int m) {
	char first = 1;
	for(int i = 0; i < N; ++i)
		if(m & (1<<i)) {
			if(first) first = 0;
			else printf(" ");
			printf("%d", A[i]);
		}
	printf("\n");
}

int main() {
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		scanf("%d", &N);
		for(int i = 0; i < N; ++i) {
			scanf("%d", &A[i]);
		}
		sort(A, A+N);
		for(int i = 1; i < (1<<N); ++i) {
			long long s = 0;
			for(int j = 0; j < N; ++j)
				if(i & (1<<j)) s += A[j];
			X[i-1].s = s;
			X[i-1].m = i;
		}
		sort(X, X+(1<<N)-1);
		int i1 = -1, i2 = -1, mx = (1<<N)-1;
		for(int i = 0; i < mx && i1 < 0; ) {
			int n = 0;
			for(++n; i+n < mx && X[i].s == X[i+n].s; ++n) ;
			for(int j = i; j < i+n && i1 < 0; ++j)
				for(int k = j+1; k < i+n && i1 < 0; ++k) {
					if((X[j].m&X[k].m) == 0) i1 = j, i2 = k;
				}
			i += n;
		}
		printf("Case #%d:\n", cs);
		if(i1 < 0) puts("Impossible");
		else {
			print(X[i1].m);
			print(X[i2].m);
		}
	}
}

