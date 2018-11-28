#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 3000;

struct Tinteval {
	int begin, end, v, len;
}ints[MAXN];
bool operator < (const Tinteval x, const Tinteval y) {
	return x.v < y.v;
}

int X, S, R, T, N;

double delta;

void init() {
	scanf("%d%d%d%d%d", &X, &S, &R, &T, &N);
	int len = X;
	for (int i=0;i<N;i++) {
		scanf("%d%d%d", &ints[i].begin, &ints[i].end, &ints[i].v);
		ints[i].v += S;
		ints[i].len = ints[i].end - ints[i].begin;
		len -= ints[i].len;
	}
	if (len > 0) {
		ints[N].len = len;
		ints[N].v = S;
		N ++;
	}
	sort(ints, ints + N);
	//for (int i=0;i<N;i++) 
	//	printf("%d %d\n", ints[i].v, ints[i].len);
	delta = (double)(R - S);
}

void work() {
	double ans = 0.0, rT = (double)T;
	for (int i=0;i<N;i++) {
		double L = (double)ints[i].len;
		double x = (double)ints[i].v;
		if (L / (x + delta) <= rT) {
			rT -= L / (x + delta);
			ans += L / (x + delta);
		} else {
			double L1 = rT * (x + delta);
			double L2 = L - L1;
			ans += rT + L2 / x;
			rT = 0.0;
		}
	}
	printf("%.6lf\n", ans);
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int ti=1;ti<=T;ti++) {
		init();
		printf("Case #%d: ", ti);
		work();
	}	
	return 0;
}

