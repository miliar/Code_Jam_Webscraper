#include <cstdio>
#include <algorithm>
using namespace std;
struct Node {
	int a, b;
	bool v, s;
	bool operator<(const Node &p) const {
		return a<p.a || a==p.a && b<p.b; }
	void out() {
		printf("%d %d: %d %d\n", a, b, v, s);
	}
};
int t, N;
Node A[200];
void find(int p, bool s) {
	for (int i = p+1; i < N; ++i) {
		if (A[i].v && A[i].s==!s && A[p].b+t <= A[i].a) {
			A[i].v = 0;
			find(i, !s);
			break;
		}
	}
}

int main() {
	int T, idx = 0; scanf("%d", &T);
	while (T--) {
		scanf("%d", &t);
		int na, nb; scanf("%d%d", &na, &nb);
		N = na + nb;
		for (int i = 0; i < N; ++i) {
			int x, y;
			scanf("%d:%d", &x, &y);
			A[i].a = x*60 + y;
			scanf("%d:%d", &x, &y);
			A[i].b = x*60 + y;
			A[i].v = 1;
			A[i].s = !(i<na);
		}
		sort(A, A+N);
		int count[2] = { 0, 0 }; 
		for (int i = 0; i < N; ++i) {
			if (!A[i].v) continue;
			find(i, A[i].s);
			++count[A[i].s];
		}
		printf("Case #%d: %d %d\n", ++idx, count[0], count[1]);
	}
	return 0;
}
