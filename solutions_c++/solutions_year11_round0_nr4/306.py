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
		int fix = 0;
		for (int i = 0; i < N; i++) {
			int a;
			scanf("%d", &a);
			if (a == i+1)
				fix++;
		}
		printf("%d\n", N-fix);
	}
	return 0;
}
