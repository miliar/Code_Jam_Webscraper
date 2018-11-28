#include <cstdio>
using namespace std;

void Solve(int test) {
	int n, k;
	scanf("%d %d", &n, &k);
	printf("Case #%d: %s\n", test, k % (1 << n) == (1 << n) - 1 ? "ON" : "OFF");
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		Solve(i);
	}
	return 0;
}
