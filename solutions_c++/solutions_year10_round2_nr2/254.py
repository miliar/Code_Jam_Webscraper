#include <iostream>
using namespace std;

int p[60], v[60];

int main() {
	freopen("b-large.in", "r", stdin);
	freopen("b-large.out", "w", stdout);
	int tt, ttt, i, N, K, B, T, cnt, possible, impossible;
	scanf("%d", &tt);
	for(ttt = 1; ttt <= tt; ttt++) {
		scanf("%d%d%d%d", &N, &K, &B, &T);
		cnt = 0;
		impossible = 0;
		possible = 0;
		for(i = 0; i < N; i++)
			scanf("%d", &p[i]);
		for(i = 0; i < N; i++)
			scanf("%d", &v[i]);
		for(i = N - 1; i >= 0 && possible < K; i--) {
			if (B - p[i] <= v[i] * T) { // possible
				cnt += impossible;
				possible++;
			} else
				impossible++;
		}
		if (possible == K)
			printf("Case #%d: %d\n", ttt, cnt);
		else
			printf("Case #%d: IMPOSSIBLE\n", ttt);
	}
//	system("pause");
	return 0;
}
