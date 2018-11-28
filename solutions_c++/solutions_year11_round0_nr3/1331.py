#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <stdlib.h>

using namespace std;

int main() {
	int T, N, result;
	char R;
	int P;

	scanf (" %d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf (" %d", &N);
		result = 0;
		int mx = 0x7fffffff, sum = 0;
		for (int i = 0;i < N; ++i) {
			scanf("%d", &P);
			result ^= P;
			if (P < mx) mx = P;
			sum += P;

		}
		if (result != 0) {
			printf("Case #%d: NO\n", cas);
		}
		else {
			printf("Case #%d: %d\n", cas, sum - mx);
		}
	}


	return 0;
}
