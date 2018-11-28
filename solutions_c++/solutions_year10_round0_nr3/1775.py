#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define MAXN 1005

using namespace std;

typedef long long ll;

int R, k, N;
ll qnt[MAXN];
int prox[MAXN];
ll val[MAXN];
ll tot;

int main () {
	int T;
	scanf ("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf ("%d%d%d", &R, &k, &N);
		for (int i = 0; i < N; i++) {
			scanf ("%lld", &qnt[i]);
			prox[i] = val[i] = -1;
		}
		tot = 0;
		int at = 0, r = 0;
		for (; r < R; r++) {
			if (val[at] != -1) {
				tot += val[at];
				at = prox[at];
				continue;
			}
			val[at] = 0;
			int cur = (at+1)%N;
			ll tmp = qnt[at];
			for (; cur != at && tmp + qnt[cur] <= k; tmp+=qnt[cur], cur=(cur+1)%N);
			val[at] = tmp;
			prox[at] = cur;
			tot += tmp;
			at = prox[at];
		}
		printf ("Case #%d: %lld\n", t+1, tot);
	}
	return 0;
}
