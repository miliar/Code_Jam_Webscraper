#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int T; cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		int N, W, L; cin >> N >> W >> L;
		printf("Case #%d:", ti);
		int cur = 0, cur2 = 0;
		int r[1011];
		int maxr = 0;
		for (int i = 0; i < N; i++) cin >> r[i], maxr = max(maxr, r[i]);
		for (int i = 0; i < N; i++) {
			if (i) cur += r[i];
			if (cur > max(W, L)) {
				cur2 += maxr*2;
				cur = 0;
			}
			if (W > L) {
				printf(" %d %d", cur, cur2);
			} else {
				printf(" %d %d", cur2, cur);
			}
			if (cur > max(W, L)) throw;
			if (cur2 > min(W, L)) throw;
			cur += r[i];
		}
		puts("");
	}
}
