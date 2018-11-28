#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;


int main() {
	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		int N, K;
		scanf("%d %d", &N, &K);

		printf("Case #%d: %s\n", t, ((K+1) % (int) pow(2, N) == 0)? "ON":"OFF");
	}

	return 0;
}
