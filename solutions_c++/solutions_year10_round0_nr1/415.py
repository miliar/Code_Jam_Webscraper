#include <cstdio>

using namespace std;

int tc() {
	int N, K;

	scanf("%d %d", &N, &K);
	int ones = 0;
	while (K&1) {
		ones++;
		K >>= 1;
	}
	return ones >= N;
}

int main() {
	int T;

	scanf("%d", &T);
	for(int i=1; i<=T; ++i)
		printf("Case #%d: %s\n", i, tc() ? "ON" : "OFF");

	return 0;
}

