#include <cstdio>
using namespace std;

int solve() {
	int N; scanf("%d", &N);
	
	int ans = 0;
	for (int i = 1; i <= N; i++) {
		int a; scanf("%d", &a);
		if (a != i) ans++;
	}

	return ans;
}

int main() {
	int T; scanf("%d", &T);

	for (int i = 1; i <= T; i++) {
		printf("Case #%d: %d\n", i, solve());
	}

	return 0;
}
