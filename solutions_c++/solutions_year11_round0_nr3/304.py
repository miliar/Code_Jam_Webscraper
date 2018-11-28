#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <math.h>
using namespace std;

int T, N;

int main() {
	scanf("%d", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d", &N);
		int xo = 0, sum = 0, mi = 1000000;
		for (int i = 0; i < N; i++) {
			int a;
			scanf("%d", &a);
			xo ^= a;
			sum += a;
			mi = min(mi, a);
		}
		if (xo)
			printf("NO\n");
		else
			printf("%d\n", sum-mi);
	}
	return 0;
}
