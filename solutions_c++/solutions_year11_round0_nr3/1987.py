#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iostream>
#include <cassert>

using namespace std;

int main() {
	int T, N;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &T);
	int k = 0;
	while (k < T) {
		int xor_ = 0, sum = 0, smallest = 1e8;
		scanf("%d", &N);
		for (size_t c_ind = 0; c_ind < N; ++c_ind) {
			int curr;
			scanf("%d", &curr);
			smallest = min(curr, smallest);
			sum += curr;
			xor_ ^= curr;
		}		

		printf("Case #%d: ", k + 1);
		if (!xor_) {
			printf("%d", sum - smallest);
		}
		else {
			printf("NO");
		}
		printf("\n");
		++k;		
	}
	return 0;
}

