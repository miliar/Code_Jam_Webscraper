#include <vector>
#include <iostream>
#include <algorithm>

struct phigh {
	int bound;
	phigh(int i) : bound(i) {}
	bool operator()( int i) { return i >= bound; }
};

int main(int argc, char * argv[])
{
	int T;
	scanf("%d\n", &T);

	for (int t = 1; t <= T; t++) {
		int N, S, P;
		int scores[200];
		scanf("%d %d %d", &N, &S, &P);

		for (int i = 0; i < N; i++) scanf("%d", &scores[i]);
		scanf("\n");

		//for (int i = 0; i < N; i++) printf("%d ", scores[i]);
		//printf("\n");

		int high = P + 2 * std::max(P-1, 0);
		int a = std::count_if(scores, scores+N, phigh(high));
		int low = P + 2 * std::max(P-2, 0);
		int b = std::count_if(scores, scores+N, phigh(low));

		printf("Case #%d: %d\n", t, a + std::min(S, b-a));
	}

	return 0;
}

