#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
	int T, N, result;
	char R;
	int P;

	scanf (" %d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf (" %d", &N);
		result = 0;
		int b_position = 1, o_position = 1, b_rest = 0, o_rest = 0;
		for (int i = 0;i < N; ++i) {
			scanf(" %c %d", &R, &P);
			if (R == 'B') {
				int cur = abs(P - b_position) + 1 - b_rest;
				if (cur < 1) {
					cur = 1;
				}
				o_rest += cur;
				b_rest = 0;
				b_position = P;
				result += cur;
			}
			else {
				int cur = abs(P - o_position) + 1 - o_rest;
				if (cur < 1) {
					cur = 1;
				}
				b_rest += cur;
				o_rest = 0;
				o_position = P;
				result += cur;
			}
		}
		printf("Case #%d: %d\n", cas, result);
	}


	return 0;
}
