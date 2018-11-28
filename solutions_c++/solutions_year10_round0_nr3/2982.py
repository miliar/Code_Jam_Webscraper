#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;

int main() {
	int T; 
	scanf("%d", &T);
	for (int i = 0; i < T; i ++) {
		int R, N, K;
		int g[2000] = {0};
		long long sum = 0;
		scanf("%d %d %d", &R, &K, &N);
		for (int j = 0; j < N; j ++)
			scanf("%d", &g[j]);

		int now = 0, total;
		for (int j = 0; j < R; j ++) {
			total = 0;
			int a = now;
			for (;;) {
				if (total + g[a] > K)
					break;

				total += g[a];
				a = (a+1) % N;
				
				if (a == now) 
					break;
			}
			now = a;
			sum += total;
		}

		printf("Case #%d: %lld\n", i+1, sum);
	}

	return 0;
}