#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


int main() {
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int R, k, N;
		scanf("%d %d %d", &R, &k, &N);

		int Q[N];
		for (int i = 0; i < N; i++)
			scanf("%d", &Q[i]);

		int euros = 0, total = 0;
		int st = 0, end;

		for (int i = 0; i < R; i++) {
			end = st;
			euros = 0;

			do {
				euros += Q[st];
				st = (st+1) % N;
			} while (st != end && euros + Q[st] <= k);

			total += euros;
		}

		printf("Case #%d: %d\n", t, total);
	}

	return 0;
}
