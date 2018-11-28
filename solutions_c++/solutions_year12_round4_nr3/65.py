#include <cstdio>
#include <algorithm>
using namespace std;
#define oo 2005
int N;
int a[oo];
int h[oo];

inline void Readin() {
	scanf("%d", &N);
	for (int i=1; i<=N-1; ++i) {
		scanf("%d", a+i);
		h[i] = 0;
	}
	h[N] = 0;
}

inline int GetHigh(int u, int v) {
	long long m = 1000000000;
	for (int i=v+1; i<=N; ++i)
		if (h[i]!=0)
		m = min(m, (((long long)h[v]*(i-v) - (long long)(h[i] - h[v])*(v-u)) / (i - v)) - 1);
	for (int i=1; i<u; ++i)
		if (h[i]!=0)
		m = min(m, (((long long)h[v]*(v-i) - (long long)(h[v] - h[i])*(v-u)) / (v - i)) - 1);
	return m;
}

bool Calc(int l, int r) {
	if (l == r) return true;
	
	for (int i = l; i<r; ++i)
		if (a[i] == r) {
			h[i] = GetHigh(i, r);
			if (!Calc(l, i)) return false;
			if (!Calc(i+1, r)) return false;
			return true;
		} else if (a[i] > r) return false;
	
	return false;
}

inline void Solve() {
	h[N] = 1000000000;
	if (Calc(1, N)) {
		for (int i=1; i<=N; ++i)
			printf("%d%c", h[i], i==N?'\n':' ');
	} else puts("Impossible");
}

int main() {
	int Test, Case = 0;
	for (scanf("%d", &Test); Test --; ){
		printf("Case #%d: ", ++Case);
		
		Readin();
		Solve();
	}

	return 0;
}