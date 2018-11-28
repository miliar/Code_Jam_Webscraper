#include <iostream>
using namespace std;

bool check(int n, int k) {
	k = k % (1<<n);
	return (1<<n)-1 == k;
}

int main() {
	freopen("../problem.in", "r", stdin);
	freopen("../problem.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tid=1; tid<=T; ++tid) {
		int n, k;
        scanf("%d %d", &n, &k);
		char * output = check(n, k) ? "ON" : "OFF";
		printf("Case #%d: %s\n", tid, output);
	}
	return 0;
}
