#include <stdio.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <queue>
#include <iostream>
using namespace std;

#define TRACE(x...) 
#define PRINT(x...) TRACE(fprintf(stderr, x))
#define WATCH(x) TRACE(cerr << #x << " = " << x << endl)

#define all(x) (x).begin(), (x).end()
#define _foreach(i, a, b) for (typeof(a) i = a; i != b; ++i)
#define foreach(x...) _foreach(x)
#define fu(i, n) foreach(i, 0, n)
#define forall(i, V) foreach(i, all(V))

#define MSET(V, x) memset(V, x, sizeof(V))

const int INF = 0x3f3f3f3f;
const int NINF = 0xc0c0c0c0;

const double EPS = 1.e-6;

inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

pair<long long, long long> V[10010];

long long d[10010], l[10010];

int main() {
	int _42;
	scanf("%d", &_42);
	fu (_, _42) {
		int N;
		scanf("%d", &N);
		int n = 0;
		for (int i = 0; i < N; i++)
			scanf("%lld %lld", &d[i], &l[i]);
		V[n++] = make_pair(2*d[0], d[0]);
		for (int i = 1; i < N; i++) {
			WATCH(i);
			WATCH(d[i]);
			WATCH(V[n-1].first);
			if (V[n-1].first < d[i]) continue; // Cannot Reach
			int pos = lower_bound(V, V+n, make_pair(d[i], 0ll)) - V;
			WATCH(pos);
			WATCH(V[pos].second);
			long long new_reach = d[i] + min(d[i] - V[pos].second, l[i]);
			WATCH(new_reach);
			if (new_reach <= V[n-1].first) continue;
			V[n++] = make_pair(new_reach, d[i]);
		}
		long long D;
		scanf("%lld", &D);
		bool ans = (V[n-1].first >= D);
		printf("Case #%d: %s\n", _+1, ans?"YES":"NO");
	}
	return 0;
}
