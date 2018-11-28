#include <cstdio>
#include <algorithm>
using namespace std;
#define oo 1005

int a[oo];
int rank[oo];
int N;
int A,B;
int X[oo],Y[oo];

bool comp(int x, int y) {
	return a[x] < a[y];
}

inline void Readin() {
	scanf("%d%d%d", &N, &A, &B);
	for (int i=1; i<=N; ++i) {
		scanf("%d", a+i);
		rank[i] = i;
	}
	sort(rank+1, rank+1+N, comp);
	
	sort(a+1, a+N+1);
}

inline void Solve() {
	int y = 0;
	for (int i=N; i>0; ) {
		if (i!=N) y+=a[i];
		if (y > B) puts("___________________________");
		int j = i, x = 0;
		while (j>1 && x <= A - a[j] - a[j-1]) {
			x += a[j] + a[j-1];
			--j;
		}
		x = 0;
		for (int k = i; k >= j; --k) {
			if (k!=i) x += a[k] + a[k+1];
			//printf("%d %d ", x, y);
			X[rank[k]] = x;
			Y[rank[k]] = y;
		}
		y+=a[i];
		i=j-1;
	}
	for (int i=1; i<=N; ++i)
		printf("%d %d ", X[i], Y[i]);
	puts("");
}

int main() {
	int Test, Case = 0;
	scanf("%d", &Test);
	while (Test -- ) {
		printf("Case #%d: ", ++Case);
		Readin();
		Solve();
	}

	return 0;
}
