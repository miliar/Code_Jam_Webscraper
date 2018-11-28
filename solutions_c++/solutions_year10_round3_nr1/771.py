#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


int main() {
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int N;
		scanf("%d", &N);

		int st[N], end[N];
		int count = 0;

		for (int i = 0; i < N; i++) {
			scanf("%d %d", &st[i], &end[i]);

			for (int j = 0; j < i; j++) {
				if ((st[i] < st[j] && end[i] > end[j]) || (st[i] > st[j] && end[i] < end[j]))
					count++;
			}
		}

		printf("Case #%d: %d\n", t, count);
	}

	return 0;
}
