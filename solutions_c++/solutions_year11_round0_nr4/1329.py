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
		for (int i = 0;i < N; ++i) {
			scanf("%d", &P);
			if (P != i + 1) ++result;
		}

			printf("Case #%d: %0.6lf\n", cas, (double)result);
	}


	return 0;
}
