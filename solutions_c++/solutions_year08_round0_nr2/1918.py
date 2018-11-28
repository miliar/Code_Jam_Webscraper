#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;

int ntest = 0;
void solve() {
	int arrive[2][3600];
	int leave[2][3600];
	memset(leave, 0, sizeof(leave));
	memset(arrive, 0, sizeof(arrive));

	int T, NA, NB;
	scanf("%d %d %d",&T,&NA,&NB);

	int add[2]; memset(add, 0, sizeof(add));
	int cur[2]; memset(cur, 0, sizeof(cur));

	// A - 0, B - 1
	for (int i = 0; i < NA; i++) {
		int h, m;
		scanf("%d:%d ", &h, &m);
		leave[0][h * 60 + m]++;
		scanf("%d:%d ", &h, &m);
		if (h * 60 + m + T < 3600)
			arrive[1][h * 60 + m + T]++;
	}

	for (int i = 0; i < NB; i++) {
		int h, m;
		scanf("%d:%d ", &h, &m);
		leave[1][h * 60 + m]++;
		scanf("%d:%d ", &h, &m);
		if (h * 60 + m + T < 3600)
			arrive[0][h * 60 + m + T]++;
	}

	for (int i = 0; i < 3600; i++) {
		for (int j = 0; j < 2; j++) {
			cur[j] += arrive[j][i];
		}

		for (int j = 0; j < 2; j++) {
			if (leave[j][i] > 0) {
				if (leave[j][i] > cur[j]) {
					add[j] += leave[j][i] - cur[j];
					cur[j] = 0;
				}
				else {
					cur[j] -= leave[j][i];
				}
			}
		}
	}

	printf("Case #%d: %d %d\n", ++ntest, add[0], add[1]);
}

int main() {
	
	freopen("test_large.in", "rt", stdin);
	freopen("test_large.out", "wt", stdout);
	int N; scanf("%d ",&N);
	for (int i = 0; i < N; i++)
		solve();
	
	return 0;
}