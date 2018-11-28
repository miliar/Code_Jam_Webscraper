#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp (int x, int y) {
	return x > y;
}

int main() {
	int T; scanf("%d", &T);
	vector<int> scores;
	scores.resize(100);
	for (int t = 0; t < T; t++) {
		scores.clear();
		int N, S, P; scanf("%d%d%d", &N, &S, &P);
		for (int n = 0; n < N; n++)
			scanf("%d", &scores[n]);
		sort(scores.begin(), scores.begin() + N, cmp);
		int total = 0;

		int minNoS = max(0, 3 * P - 2);
		int minS = P == 1 ? 1 : max(0, 3 * P - 4);

		while (total < N && scores[total] >= minNoS) total++;
		while (S > 0 && total < N && scores[total] >= minS) {total++; S--;}

		printf("Case #%d: %d\n", t + 1, total);
	}
	return 0;
}
